class CircularQueue:
    def __init__(self, size):
        self._items = []
        self.size = size
        self.first = None
        self.last = None

    def isEmpty(self):
        return len(self._items) == 0

    def __len__(self):
        return len(self._items)

    def enqueue(self, item):
        assert not len(self) >= self.size, "Maximum size exceeded! Cannot enqueue more elements in to the queue."
        node = _CircularQueueNode(item)
        if self.isEmpty():
            node.behind = node
            node.front = node
            self.first = node
        else:
            node.behind = self.first
            node.front = self.last
            if len(self) == 1:
                self.first.behind = node
            self.last.behind = node
        self.last = node
        self.first.front = self.last
        self._items.append(item)

    def dequeue(self):
        assert not self.isEmpty(), "Cannot dequeue from an empty queue"
        # removed = self.first
        if len(self) == 1:
            self.first = None
            self.last = None
        self.first = self.first.behind
        self.first.front = self.last
        self.last.behind = self.first
        return self._items.pop(0)


class _CircularQueueNode:
    def __init__(self, item):
        self.item = item
        self.front = None
        self.behind = None

# create a queue of size 3
cQ = CircularQueue(3)
# added 3 elements
cQ.enqueue("A")
cQ.enqueue("B")
cQ.enqueue("C")
# see how the queue goes from the first element in a circle
print("See how the queue goes from the first element in a circle")
print(cQ.first.item)
print(cQ.first.behind.item)
print(cQ.first.behind.behind.item)
print(cQ.first.behind.behind.behind.item)
print(cQ.first.behind.behind.behind.behind.item)
# see how the queue goes from the last element in a reverse-circle
print("See how the queue goes from the last element in a reverse-circle")
print(cQ.last.item)
print(cQ.last.front.item)
print(cQ.last.front.front.item)
print(cQ.last.front.front.front.item)
print(cQ.last.front.front.front.front.item)
# remove an element from the queue
print("Remove an element from the queue")
dequeued = cQ.dequeue()
print(dequeued)

        
        





    

