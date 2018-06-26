import unittest


class TempTracker(object):

    # Implement methods to track the max, min, mean, and mode
    max_ = -float("inf")
    min_ = float("inf")
    mean = 0
    c = 0
    mode = None
    dict_ = {}
    def insert(self, temperature):
        if temperature > self.max_ :
            self.max_ = temperature
        if temperature < self.min_ :
            self.min_ = temperature
        self.mean = (self.c * self.mean + temperature)/(self.c + 1) 
        self.c += 1         
        if not self.dict_:
            self.mode = temperature
        if temperature in self.dict_:
            self.dict_[temperature] += 1   
        else:
            self.dict_[temperature] = 1
            
        if self.dict_[temperature] > self.dict_[self.mode]:
            self.mode = temperature

    def get_max(self):
        return self.max_

    def get_min(self):
        return self.min_

    def get_mean(self):
        return self.mean

    def get_mode(self):
        return self.mode


















# Tests

class Test(unittest.TestCase):

    def test_tracker_usage(self):
        tracker = TempTracker()

        tracker.insert(50)
        msg = 'failed on first temp recorded'
        self.assertEqual(tracker.get_max(), 50, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 50.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 50, msg='mode ' + msg)

        tracker.insert(80)
        msg = 'failed on higher temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 65.0, msg='mean ' + msg)
        self.assertIn(tracker.get_mode(), [50, 80], msg='mode ' + msg)

        tracker.insert(80)
        msg = 'failed on third temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 70.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 80, msg='mode ' + msg)

        tracker.insert(30)
        msg = 'failed on lower temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 30, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 60.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 80, msg='mode ' + msg)


unittest.main(verbosity=2)