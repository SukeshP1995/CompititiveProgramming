import unittest

class Stack(object):

    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push new item to stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        """See what the last item is"""
        if not self.items:
            return None
        return self.items[-1]

class QueueTwoStacks(object):

    # Implement the enqueue and dequeue methods
    
    def __init__(self):
        self.stack = Stack()
        self.c = 0

    def enqueue(self, item):
        stack = Stack()
        for _ in range(self.c):
            stack.push(self.stack.pop())
        self.stack.push(item)
        for _ in range(self.c):
            self.stack.push(stack.pop())
        self.c += 1

    def dequeue(self):
        if self.c == 0:
            raise Exception('exception')
        self.c -= 1
        return self.stack.pop()


















# Tests

class Test(unittest.TestCase):

    def test_queue_usage(self):
        queue = QueueTwoStacks()

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        actual = queue.dequeue()
        expected = 1
        self.assertEqual(actual, expected)

        actual = queue.dequeue()
        expected = 2
        self.assertEqual(actual, expected)

        queue.enqueue(4)

        actual = queue.dequeue()
        expected = 3
        self.assertEqual(actual, expected)

        actual = queue.dequeue()
        expected = 4
        self.assertEqual(actual, expected)

        with self.assertRaises(Exception):
            queue.dequeue()


unittest.main(verbosity=2)