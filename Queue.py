class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.isEmpty():
            self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

q = Queue()
q.enqueue(4)
q.enqueue('dog')
q.enqueue(True)
print(q.size())
print(q.isEmpty())
print(q.enqueue(8.4))
print q.items
print(q.dequeue())
print(q.dequeue())
print(q.size())
