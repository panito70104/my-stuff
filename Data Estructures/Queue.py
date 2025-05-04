class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise IndexError("dequeue from an empty queue")

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("peek from an empty queue")
        
s = Queue()
s.enqueue("Juan")
s.enqueue("Ana")
s.enqueue("Luis")
#print(s.queue)
print(s.peek())
s.dequeue()
print(s.queue)
