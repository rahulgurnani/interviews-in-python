import heapq


class MaxHeap:
    def __init__(self):
        self.heap = []
        heapq.heapify(self.heap)

    def push(self, a):
        heapq.heappush(self.heap, -a)

    def pop(self):
        return -heapq.heappop(self.heap)

    def peek(self):
        return -self.heap[0]

    def size(self):
        return len(self.heap)
