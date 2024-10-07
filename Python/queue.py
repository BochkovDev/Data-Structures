class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self) -> bool:
        '''Check if the queue is empty'''
        return len(self.queue) == 0

    def enqueue(self, item) -> None:
        '''Add an element to the end of the queue'''
        self.queue.append(item)

    def dequeue(self):
        '''Remove and return the element from the front of the queue'''
        if self.is_empty():
            raise IndexError('Dequeue from an empty queue')
        return self.queue.pop(0)

    def front(self):
        '''Return the element at the front of the queue without removing it'''
        if self.is_empty():
            raise IndexError('Front from an empty queue')
        return self.queue[0]

    def size(self) -> int:
        '''Return the number of elements in the queue'''
        return len(self.queue)