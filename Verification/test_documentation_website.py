"""Check website publication rules and dual local/online navigation.

These tests use only the standard library. They do not run the simulation.
"""
from pathlib import Path
import importlib.util
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('website', ROOT / 'Code/simulation_tools/build_documentation_website.py')
website = importlib.util.module_from_spec(spec)
spec.loader.exec_module(website)


class WebsitePublicationVerification(unittest.TestCase):
    def test_private_files_never_enter_artifact(self):
        for name in ['.git/config', '.venv/pyvenv.cfg',
                     'Documentation/References/Local_Papers/private.pdf',
                     'Data/Skeletal_Geometry/Model/meshes/bone.obj']:
            self.assertFalse(website.belongs_in_website(name))

    def test_raw_results_stay_available_without_website_duplication(self):
        raw = 'Simulation_Results/Intact_Walking/forward_simulation_timeseries.npz'
        self.assertFalse(website.belongs_in_website(raw))
        self.assertTrue(website.belongs_in_website('Simulation_Results/Intact_Walking/simulation_report.html'))
        link = website.resolve_link('Simulation_Results/index.html', 'Intact_Walking/forward_simulation_timeseries.npz',
                                    set(), {raw}, 'owner/repo', 'commit123')
        self.assertEqual(link, 'https://github.com/owner/repo/blob/commit123/' + raw)

    def test_relative_navigation_keeps_project_prefix(self):
        link = website.resolve_link('Documentation/model_methods.html', '../START_HERE.html',
                                    {'START_HERE.html'}, {'START_HERE.html'}, 'owner/repo', 'main')
        self.assertEqual(link, '../START_HERE.html')
        with self.assertRaises(ValueError):
            website.local_target('Documentation/model_methods.html', '/START_HERE.html')

    def test_missing_or_ignored_download_fails_instead_of_publishing(self):
        with self.assertRaises(ValueError):
            website.resolve_link('Documentation/index.html', 'secret.pdf', set(), set(), 'owner/repo', 'main')

    def test_inline_script_and_code_listing_are_preserved(self):
        source = '<script>const x="<a href=\"not-a-link\">";</script><pre>&lt;a href="also-not-a-link"&gt;</pre><a href="../START_HERE.html">Home</a>'
        output = website.prepare_html('Documentation/index.html', source,
                                      {'START_HERE.html'}, {'START_HERE.html'}, 'owner/repo', 'main')
        self.assertEqual(source, output)

    def test_directory_link_is_portable(self):
        self.assertEqual(website.resolve_link('Documentation/index.html', '../Data/',
                         {'Data/index.html'}, {'Data/index.html'}, 'owner/repo', 'main'), '../Data/index.html')


if __name__ == '__main__':
    unittest.main()
