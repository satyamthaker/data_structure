class ArrayQueue:
    DEFAULT_CAPACITY = 10
    def __init__(self):
        self.item = [] * ArrayQueue.DEFAULT_CAPACITY

    def isEmpty(self):
        return self.item == []

    def enqueueFront(self, item):
        self.item.append(item)

    def enqueueBack(self, item):
        self.item.insert(0,item)

    def dequeueFront(self):
        return self.item.pop()

    def dequeueBack(self):
        return self.item.pop(0)

    def size(self):
        return len(self.item)

dq=ArrayQueue()
print(dq.isEmpty())
dq.enqueueBack(9)
dq.enqueueBack('satyam')
dq.enqueueFront('thaker')
dq.enqueueFront(True)
print(dq.size())
print(dq.isEmpty())
dq.enqueueBack(9.9)
print(dq.dequeueBack())
print(dq.dequeueFront())
