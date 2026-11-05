"""Existing public CLI coverage, deliberately lacking the empty-input case."""
import subprocess
import sys
import unittest


class PopulatedExport(unittest.TestCase):
    # Why: populated CSV is an existing public contract.
    # What: quoting, order and amounts survive export.
    # How: send JSON to the public executable and assert its emitted bytes.
    def test_populated_export(self):
        result = subprocess.run([sys.executable, "export.py"],
                                input='[{"id":"a,b","total":12.5}]',
                                text=True, capture_output=True, check=True)
        self.assertEqual(result.stdout, 'id,total\n"a,b",12.5\n')
