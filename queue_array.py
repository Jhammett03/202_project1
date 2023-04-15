class QueueArray:
    """Implements an efficient first-in first-out Abstract Data Type using a Python List"""

    def __init__(self, capacity):
        """Creates an empty queue with a capacity"""
        self.capacity = capacity  # Capacity of your queue
        self.items = [None] * capacity  # initializing the queue
        self.num_items = 0  # number of elements in the queue

    def is_empty(self):
        """Returns true if the queue self is empty and false otherwise"""
        return self.num_items == 0

    def is_full(self):
        """Returns true if the queue self is full and false otherwise"""
        return self.num_items == self.capacity

    def enqueue(self, item):
        """Adds item to the queue"""
        if self.is_full():
            raise IndexError("Queue is full")
        self.items[self.num_items] = item
        self.num_items += 1

    def dequeue(self):
        """Returns the current front of the queue"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        front = self.items[0]
        for i in range(1, self.num_items):
            self.items[i-1] = self.items[i]
        self.num_items -= 1
        return front

    def peek(self):
        """Returns the value of the item at the front of the queue without removing it"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]

    def size(self):
        """Returns the number of elements currently in the queue, not the capacity"""
        return self.num_items
