import unittest
from stack_linked_list import StackLinkedList


class TestStackLinkedList(unittest.TestCase):
    def test_push_and_peek(self):
        stack = StackLinkedList(5)
        self.assertTrue(stack.is_empty())
        stack.push(1)
        self.assertEqual(stack.peek(), 1)
        stack.push(2)
        self.assertEqual(stack.peek(), 2)
        stack.push(3)
        self.assertEqual(stack.peek(), 3)
        stack.push(4)
        self.assertEqual(stack.peek(), 4)
        stack.push(5)
        self.assertEqual(stack.peek(), 5)
        self.assertTrue(stack.is_full())
        with self.assertRaises(IndexError):
            stack.push(6)

    def test_pop(self):
        stack = StackLinkedList(5)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        self.assertTrue(stack.is_empty())
        with self.assertRaises(IndexError):
            stack.pop()

    def test_size(self):
        stack = StackLinkedList(5)
        self.assertEqual(stack.size(), 0)
        stack.push(1)
        self.assertEqual(stack.size(), 1)
        stack.push(2)
        self.assertEqual(stack.size(), 2)
        stack.push(3)
        self.assertEqual(stack.size(), 3)
        stack.pop()
        self.assertEqual(stack.size(), 2)
        stack.pop()
        self.assertEqual(stack.size(), 1)
        stack.pop()
        self.assertEqual(stack.size(), 0)


if __name__ == '__main__':
    unittest.main()
