"""Create readable late-trial comparison figures from saved forward results.

This is postprocessing only: it never changes inputs, states, force values or
time alignment. The last four seconds show the waveform detail. A separate
last-ten-second table reports RMSE against the same fixed-clock references.
Run from the root with: python Code/simulation_tools/create_release_figures.py
"""
from pathlib import Path
import json
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Resolve the repository from the script, so the working directory is irrelevant.
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'Code'))
from neuromechanics.experimental_comparison_targets import experimental_comparison_targets
from neuromechanics.emg_comparison_cycles import emg_comparison_cycles


def create_release_figures():
    """Save all-joint, all-paw, all available EMG, and intervention comparisons."""
    folder=ROOT/'Simulation_Results/Intact_Walking'
    output=ROOT/'Documentation/Figures_and_Videos'
    output.mkdir(parents=True,exist_ok=True)
    with np.load(folder/'forward_simulation_timeseries.npz') as stored:
        result={key:stored[key] for key in stored.files}
    settings=json.loads((folder/'settings.json').read_text())
    times=result['time']
    late=times>=times[-1]-4
    score=times>=times[-1]-10
    target=experimental_comparison_targets(times,settings['period_s'],settings.get('reference_table_dir'))
    limb_labels=['LH · assumed mirror','RH · measured','LF · separate study','RF · separate study']
    joints=[['Hip','Knee','Ankle','MTP']]*2+[['Shoulder','Elbow','Wrist','MCP']]*2
    plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})
    fig,axes=plt.subplots(4,4,figsize=(16,10),sharex=True)
    for side in range(4):
        signs=np.array([-1,1,-1,-1]) if side<2 else np.array([1,-1,-1,-1])
        offset=np.array([0,np.pi,np.pi,np.pi]) if side<2 else np.full(4,np.pi)
        for j in range(4):
            a=axes[side,j]
            a.plot(times[late],np.rad2deg(offset[j]+signs[j]*target['joint_q'][late,side,j]),'k--',lw=1.2,label='Reference')
            a.plot(times[late],np.rad2deg(offset[j]+signs[j]*result['joint_q'][late,side,j]),color='#067f97',lw=1.4,label='Forward')
            a.set_title(limb_labels[side]+' · '+joints[side][j],fontsize=10)
            a.grid(alpha=.18)
        axes[side,0].set_ylabel('Anatomical angle (deg)')
    axes[0,0].legend(fontsize=8)
    for a in axes[-1]:a.set_xlabel('Simulation time (s)')
    fig.suptitle('All 16 joints · same anatomical conventions and fixed reference clocks\nLate four-second interval; no time warping',fontsize=15)
    fig.tight_layout(rect=(0,0,1,.94));fig.savefig(output/'joint_comparison.png',dpi=140);plt.close(fig)
    fig,axes=plt.subplots(4,2,figsize=(12,10),sharex=True)
    for side in range(4):
        for col,k in enumerate([0,2]):
            a=axes[side,col]
            a.plot(times[late],target['grf'][late,side,k],'k--',lw=1.2,label='Reference')
            a.plot(times[late],result['grf'][late,side,k],color='#067f97',lw=1.4,label='Raw contact force')
            a.set_title(limb_labels[side]+(' · anterior–posterior (AP) Fx' if k==0 else ' · vertical Fz'))
            a.set_ylabel('Force (N)');a.grid(alpha=.18)
            if k==0:a.axhline(0,color='gray',lw=.5)
    axes[0,0].legend(fontsize=8)
    for a in axes[-1]:a.set_xlabel('Simulation time (s)')
    fig.suptitle('Paw Ground_Reaction_Forces · unfiltered forward contact forces',fontsize=16)
    fig.tight_layout(rect=(0,0,1,.96));fig.savefig(output/'grf_comparison.png',dpi=150);plt.close(fig)
    pairs=emg_comparison_cycles(result['names'],settings)
    for prefix in ['L','R','FL','FR']:
        selected=[p for p in pairs if p['limb']==prefix]
        fig,axes=plt.subplots(2,4,figsize=(14,6),sharex=True,sharey=True)
        for a,pair in zip(axes.flat,selected):
            phase=np.arange(len(pair['reference']))/len(pair['reference'])
            a.plot(phase*100,pair['reference'],'k--',label='EMG reference')
            a.plot(phase*100,pair['excitation'],color='#067f97',label='Excitation / cycle peak')
            a.set_title(pair['channel']);a.grid(alpha=.18)
        for a in list(axes.flat)[len(selected):]:a.set_visible(False)
        axes[0,0].legend(fontsize=8)
        for a in axes[-1]:a.set_xlabel('Input cycle (%)')
        for a in axes[:,0]:a.set_ylabel('Peak-normalized shape')
        scope='measured RH EMG' if prefix=='R' else 'assumed from RH' if prefix=='L' else 'pooled forelimb EMG'
        fig.suptitle(prefix+' · '+scope+'\nShape normalization is for comparison only; raw excitation is unchanged.',fontsize=14)
        fig.tight_layout(rect=(0,0,1,.91));fig.savefig(output/('emg_'+prefix+'.png'),dpi=140);plt.close(fig)
    report={'window_start_s':float(times[score][0]),'window_end_s':float(times[-1]),'joint_RMSE_deg':np.sqrt(np.mean(np.rad2deg(result['joint_q'][score]-target['joint_q'][score])**2,axis=0)).tolist(),'GRF_RMSE_N':np.sqrt(np.mean((result['grf'][score]-target['grf'][score])**2,axis=0)).tolist()}
    (ROOT/'Simulation_Results/Intact_Walking/late_window_metrics.json').write_text(json.dumps(report,indent=2))
    print('Comparison figures and fixed-clock metrics saved.')


if __name__=='__main__':
    create_release_figures()
