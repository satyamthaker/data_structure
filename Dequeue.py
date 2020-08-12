class ArrayQueue:
    DEFAULT_CAPACITY = 10
    def __init__(self):
        self.data = [None] * ArrayQueue.DEFAULT_CAPACITY

    def isEmpty(self):
        return self.size == 0

    def enqueueFront(self, data):
        self.data.append(data)

    def enqueueBack(self, data):
        self.data.insert(0,data)

    def dequeueFront(self):
        return self.data.pop()

    def dequeueBack(self):
        return self.data.pop(0)

    def size(self):
        return len(self.data)

dq=ArrayQueue()
dq.enqueueBack('thaker')
dq.enqueueFront('satyam')
print(dq.dequeueBack())
print(dq.dequeueFront())
print(dq.size())
print(dq.isEmpty())
