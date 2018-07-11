import unittest


def find_repeat(the_list):
    f = 1
    c = len(the_list) - 1

    while f < c:
        
        mid = f + ((c- f) // 2)
        lrf, lrc = f, mid
        urf, urc = mid+1, c

        itemslr= 0
        for item in the_list:
            if item >= lrf and item <= lrc:
                itemslr += 1

        dlr = (lrc- lrf+ 1)

        if itemslr > dlr:
            
            f, c = lrf, lrc
        else:
            
            f, c = urf, urc


    return f


















# Tests

class Test(unittest.TestCase):

    def test_just_the_repeated_number(self):
        actual = find_repeat([1, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_short_list(self):
        actual = find_repeat([1, 2, 3, 2])
        expected = 2
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_repeat([1, 2, 5, 5, 5, 5])
        expected = 5
        self.assertEqual(actual, expected)

    def test_long_list(self):
        actual = find_repeat([4, 1, 4, 8, 3, 2, 7, 6, 5])
        expected = 4
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)