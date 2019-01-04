import heapq
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        print(heapq.heappop(self._queue)[-1])

    @staticmethod
    def wanghm():
        print("wanghm is handsome")
class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Item({0})".format(self.name)

q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
q.pop()
q.pop()
q.pop()
PriorityQueue.wanghm()
