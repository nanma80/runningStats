from runningstats import RunningStats
import unittest

class TestRunningStats(unittest.TestCase):
  def test_empty_case(self):
    stats = RunningStats()
    self.assertEqual(0, stats.average())
    self.assertEqual(0, stats.variance())

  def test_single_value(self):
    stats = RunningStats()
    stats.add(4)
    self.assertEqual(4, stats.average())
    self.assertEqual(0, stats.variance())

  def test_two_values(self):
    stats = RunningStats()
    stats.add(4)
    stats.add(6)
    self.assertEqual(5, stats.average())
    self.assertEqual(1, stats.variance())


if __name__ == '__main__':
  unittest.main()
