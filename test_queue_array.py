import unittest
from queue_array import QueueArray


class TestQueueArray(unittest.TestCase):
    def test_queue_enqueue(self):
        queue = QueueArray(5)
        self.assertTrue(queue.is_empty())
        self.assertFalse(queue.is_full())

        queue.enqueue(1)
        self.assertEqual(queue.size(), 1)
        self.assertEqual(queue.peek(), 1)
        self.assertFalse(queue.is_empty())
        self.assertFalse(queue.is_full())

        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)
        queue.enqueue(5)
        self.assertEqual(queue.size(), 5)
        self.assertEqual(queue.peek(), 1)
        self.assertFalse(queue.is_empty())
        self.assertTrue(queue.is_full())

        with self.assertRaises(IndexError):
            queue.enqueue(6)

if __name__ == '__main__':
    unittest.main()
