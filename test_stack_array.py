import unittest
from stack_array import StackArray

class TestStackArray(unittest.TestCase):

    def test_push_pop(self):
        # Test push() and pop()
        stack = StackArray(5)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)

    def test_peek(self):
        # Test peek()
        stack = StackArray(5)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.peek(), 3)
        self.assertEqual(stack.peek(), 3)

    def test_is_empty(self):
        # Test is_empty()
        stack = StackArray(5)
        self.assertTrue(stack.is_empty())
        stack.push(1)
        self.assertFalse(stack.is_empty())

    def test_is_full(self):
        # Test is_full()
        stack = StackArray(3)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertTrue(stack.is_full())

    def test_size(self):
        # Test size()
        stack = StackArray(5)
        self.assertEqual(stack.size(), 0)
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.size(), 2)
        stack.pop()
        self.assertEqual(stack.size(), 1)

    def test_push_full(self):
        # Test pushing to full stack
        stack = StackArray(2)
        stack.push(1)
        stack.push(2)
        with self.assertRaises(IndexError):
            stack.push(3)

    def test_pop_empty(self):
        # Test popping from empty stack
        stack = StackArray(2)
        with self.assertRaises(IndexError):
            stack.pop()

if __name__ == '__main__':
    unittest.main()
