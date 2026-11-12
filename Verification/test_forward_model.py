"""Mechanics and numerical regression tests; no fitting or GUI is performed.

Run from the repository root: python -m unittest discover -s Verification -v
The reference test compares a fresh short trajectory with the released baseline.
"""
from pathlib import Path
import json, shutil, sys, tempfile, unittest
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'Code'))
from neuromechanics.load_model_configuration import load_model_configuration
from neuromechanics.initialize_neuromechanical_model import initialize_neuromechanical_model
from neuromechanics.simulate_forward_dynamics import simulate_forward_dynamics
from neuromechanics.elastic_tendon_force import elastic_tendon_force
from neuromechanics.elastic_tendon_transition import elastic_tendon_transition
from neuromechanics.muscle_excitation import muscle_excitation
from neuromechanics.load_parameter_file import load_parameter_file
from neuromechanics.viscoelastic_paw_pad import viscoelastic_paw_pad
from neuromechanics.muscle_force_length_velocity import muscle_force_length_velocity
from neuromechanics.muscle_force_curve_derivatives import muscle_force_curve_derivatives
from neuromechanics.solve_elastic_muscle_equilibrium import solve_elastic_muscle_equilibrium


class ForwardModelVerification(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cfg=load_model_configuration(ROOT/'Data/Model_Parameters')
        cls.state=initialize_neuromechanical_model(cls.cfg)

    def test_passive_fiber_is_enabled_for_every_limb(self):
        self.assertEqual(len(self.state['names']),104)
        np.testing.assert_array_equal(self.state['muscle_params'][:,13],np.ones(104))

    def test_published_passive_curve_and_derivative(self):
        # Independent formula: Prilutsky 2016 Table 10.3, tension-only adaptation.
        p=self.state['muscle_params'][list(self.state['names']).index('R_VL')]
        for length in [0.6,1.0,1.1,1.2,1.5]:
            expected=max(0.,0.0075/11.6*np.expm1(11.6*(length-1)))
            self.assertAlmostEqual(muscle_force_length_velocity(length,0.,p)[2],expected,places=13)
        length=1.2
        h=1e-6
        numerical=(muscle_force_length_velocity(length+h,0,p)[2]-muscle_force_length_velocity(length-h,0,p)[2])/(2*h)
        self.assertAlmostEqual(muscle_force_curve_derivatives(length,0,p)[5],numerical,places=9)

    def test_unactivated_stretched_fiber_transmits_passive_tendon_force(self):
        # Construct a static series equilibrium: a=0, fiber velocity=0.
        # Tendon and parallel elastic tissue must carry the same positive force.
        s=self.state
        i=list(s['names']).index('R_VL')
        p=s['muscle_params'][i:i+1]
        length=1.2*s['lopt'][i]
        passive=0.0075/11.6*np.expm1(11.6*0.2)
        low,high=0.,float(s['e0'][i])
        for _ in range(70):
            middle=(low+high)/2
            if elastic_tendon_force(middle,s['e0'][i])<passive:low=middle
            else:high=middle
        total=length*p[0,9]+s['slack'][i]*(1+(low+high)/2)
        lf,v,force,residual,bound=solve_elastic_muscle_equilibrium(
            np.array([total]),np.array([length]),np.zeros(1),s['lopt'][i:i+1],
            s['slack'][i:i+1],p,s['e0'][i:i+1],np.array([0.05]),0.000125)
        self.assertGreater(force[0],0.)
        self.assertAlmostEqual(force[0],p[0,2]*passive,places=8)
        self.assertAlmostEqual(v[0],0.,places=8)
        self.assertLess(abs(residual[0]),1e-7)
        self.assertEqual(bound[0],0)

    def test_tendon_calibration_and_continuity(self):
        e0=0.04
        toe=elastic_tendon_transition(e0)
        self.assertEqual(elastic_tendon_force(-0.01,e0),0)
        self.assertAlmostEqual(elastic_tendon_force(e0,e0),1,places=12)
        self.assertAlmostEqual(elastic_tendon_force(toe,e0),0.33,places=12)
        h=1e-7
        left=(elastic_tendon_force(toe,e0)-elastic_tendon_force(toe-h,e0))/h
        right=(elastic_tendon_force(toe+h,e0)-elastic_tendon_force(toe,e0))/h
        self.assertAlmostEqual(left,right,delta=0.001)

    def test_input_repeats_without_mechanical_feedback(self):
        state = self.state
        period = state['settings']['period_s']
        initial_input = muscle_excitation(state, 0.17)
        np.testing.assert_allclose(initial_input, muscle_excitation(state, 0.17 + period), atol=1e-12)
        # Changing a recorded force must not change this prescribed motor input.
        old_force = state['grf'].copy()
        state['grf'][:] = 100.0
        np.testing.assert_array_equal(initial_input, muscle_excitation(state, 0.17))
        state['grf'][:] = old_force

    def test_contact_cannot_pull_and_obeys_friction_limit(self):
        p=self.state['contact_parameters'][0]
        f,_,_=viscoelastic_paw_pad(0,np.array([1.,0.,0.]),np.zeros(2),0.000125,p)
        np.testing.assert_array_equal(f,np.zeros(3))
        f,_,_=viscoelastic_paw_pad(0.002,np.array([1.,0.,-0.1]),np.zeros(2),0.000125,p)
        self.assertGreaterEqual(f[2],0)
        self.assertLessEqual(np.linalg.norm(f[:2]),p[4]*f[2]+1e-12)
        self.assertLess(f[0],0)

    def test_edited_mass_is_actually_applied(self):
        with tempfile.TemporaryDirectory(prefix='cat_parameter_test_') as temp:
            folder=Path(temp)/'parameters'
            shutil.copytree(ROOT/'Data/Model_Parameters',folder,ignore=shutil.ignore_patterns('*.html'))
            data=load_parameter_file(folder/'bodies.py')
            key=next(iter(data))
            old=float(data[key]['mass_kg'])
            data[key]['mass_kg']=old*1.01
            (folder/'bodies.py').write_text('PARAMETERS = '+repr(data),encoding='utf-8')
            s=initialize_neuromechanical_model(load_model_configuration(folder))
            self.assertAlmostEqual(s['model'].body(key).mass[0],old*1.01,places=12)

    def test_short_forward_reproduces_release(self):
        s=initialize_neuromechanical_model(self.cfg)
        result,_=simulate_forward_dynamics({'seconds':0.05},state=s)
        with np.load(ROOT/'Simulation_Results/Intact_Walking/forward_simulation_timeseries.npz') as baseline:
            n=len(result['time'])
            for key in ['qpos','qvel','activation','excitation','force','fiber_length','grf']:
                np.testing.assert_allclose(result[key],baseline[key][:n],rtol=1e-7,atol=1e-8,err_msg=key)
        self.assertEqual(str(result['failure']),'')


if __name__=='__main__':
    unittest.main()
