import unittest
import math

def find_rotation_point(words):

    # if('ptolemaic' < 'xenoepist'):
    #     print('yo')
    # Find the rotation point in the list
    l = 0
    r = len(words)-1
    first = words[0]
    while l <= r:
        # print(words[l:r])
        print (words[l:r+1])
        if words[l] <= words[r]:
            return (r + 1)%len(words)
        mid = math.ceil(l + (r - l)/2)
        print(mid)
        if words[mid] <= words[l]:
            r = mid - 1
        elif words[mid] > words[l]:
            l = mid



















# Tests

class Test(unittest.TestCase):

    def test_small_list(self):
        actual = find_rotation_point(['cape', 'cake'])
        expected = 1
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_rotation_point(['grape', 'orange', 'plum',
                                      'radish', 'apple'])
        expected = 4
        self.assertEqual(actual, expected)

    def test_large_list(self):
        actual = find_rotation_point(['ptolemaic', 'retrograde', 'supplant',
                                      'undulate', 'xenoepist', 'asymptote',
                                      'babka', 'banoffee', 'engender',
                                      'karpatka', 'othellolagkage'])
        expected = 5
        self.assertEqual(actual, expected)


    # Are we missing any edge cases?


unittest.main(verbosity=2)