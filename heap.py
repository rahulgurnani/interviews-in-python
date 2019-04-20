# REF: https://www.cs.cmu.edu/~adamchik/15-121/lectures/Binary%20Heaps/heaps.html
class Heap:
    def __init__(self):
        self._heap = [float('inf')]
        self._size = 0

    def doubleSize(self):
        self._heap = self._heap + (self._size + 1) * [float('inf')]

    def insert(self, v):
        if self._size == len(self._heap):
            self.doubleSize()
        self._heap[self._size] = v
        i = self._size
        self._size += 1
        while i > 0:
            if self._heap[i//2] > self._heap[i]:
                self._heap[i//2], self._heap[i] = self._heap[i], self._heap[i//2]
                i = i//2
            else:
                break

    def pop(self):
        minimum = self._heap[0]
        self._heap[0] = self._heap[self._size - 1]
        self._size -= 1
        i = 0

        while 2*i < self._size:
            left = self._heap[i*2]
            right = self._heap[i*2 + 1]
            if self._heap[i] > min(left, right):
                if self._heap[i * 2] < self._heap[i*2 + 1]:
                    self._heap[i],
                    self._heap[i*2] = self._heap[i*2], self._heap[i]
                    i = i * 2
                else:
                    self._heap[i], self._heap[i*2 + 1] = self._heap[i *
                                                                    2 + 1], self._heap[i]
                    i = i*2 + 1
            else:
                break
        return minimum

    def peek(self):
        if self._size > 0:
            return self._heap[0]
        return None


heap = Heap()
heap.insert(1)
heap.insert(0)
heap.insert(10)
heap.insert(9)
heap.insert(11)
heap.insert(13)
heap.insert(2)
heap.insert(-1)
print(heap._heap)
print(heap.pop())
print(heap._heap)
