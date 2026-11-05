import unittest
from tool_result_dependency_cut.core import run
class DomainTests(unittest.TestCase):
 def test_transitive(self):
  x=run({'nodes':[dict(id='a',status='unknown',depends_on=[]),dict(id='b',status='valid',depends_on=['a']),dict(id='c',status='valid',depends_on=['b'])]});self.assertEqual(x['results'][-1]['blocking_roots'],['a'])
 def test_cycle(self):
  with self.assertRaises(ValueError):run({'nodes':[dict(id='a',status='valid',depends_on=['a'])]})
 def test_independent(self):self.assertTrue(run({'nodes':[dict(id='a',status='valid',depends_on=[])]})['results'][0]['usable'])
