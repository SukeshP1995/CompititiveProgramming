import unittest

dict_ = {}
c = 0

def fib(n):
    assert(n >= 0)
    # print('hi')
    # Compute the nth Fibonacci number
    if n in dict_:
        pass
    elif n == 0 or n == 1:
        dict_[n] = n
    else:
        dict_[n] = fib(n-1) + fib(n-2)
    return dict_[n]

    # if n == 0 or n == 1:
    #     return n
    # return fib(n-1) + fib(n-2)

















# Tests

class Test(unittest.TestCase):

    def test_zeroth_fibonacci(self):
        actual = fib(0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_first_fibonacci(self):
        actual = fib(1)
        expected = 1
        self.assertEqual(actual, expected)

    def test_second_fibonacci(self):
        actual = fib(2)
        expected = 1
        self.assertEqual(actual, expected)

    def test_third_fibonacci(self):
        actual = fib(3)
        expected = 2
        self.assertEqual(actual, expected)

    def test_fifth_fibonacci(self):
        actual = fib(5)
        expected = 5
        self.assertEqual(actual, expected)

    def test_tenth_fibonacci(self):
        actual = fib(10)
        expected = 55
        self.assertEqual(actual, expected)

    def test_negative_fibonacci(self):
        with self.assertRaises(Exception):
            fib(-1)


unittest.main(verbosity=2)