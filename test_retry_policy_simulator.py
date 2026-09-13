import unittest
from retry_policy_simulator import schedule
class TestSchedule(unittest.TestCase):
 def test_cap(self): self.assertEqual(schedule(5,2,10),[2,4,8,10,10])
if __name__=='__main__': unittest.main()
