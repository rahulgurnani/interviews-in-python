import heapq

li = [3, 1, 4, 5, 0]
heapq.heapify(li)

print("initial heap")
print(li)

heapq.heappush(li, 10)
heapq.heappush(li, -1)

print("modified heap")
print(li)

print("heap sort")
for i in range(0, len(li)):
    print(heapq.heappop(li))
