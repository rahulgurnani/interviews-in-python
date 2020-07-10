import heapq
def shortest_distance(graph, source, dest):
    distance_heap = []
    heapq.heappush(distance_heap, (0, source))
    allocated = set()
    while len(distance_heap) > 0:
        distance, node = heapq.heappop(distance_heap)
        if node in allocated:
            continue
        allocated.add(node)
        if node == dest:
            return distance
        for neighbor, delta in graph[node]:
            if neighbor in allocated:
                continue
        heapq.heappush(distance_heap, (distance+delta, neighbor))

    return -1
graph = {(0, 0): [((1, 0), 2), ((0, 1), 5), ((0, 1), 5), ((1, 0), 2)], (1, 0): [((0, 0), 0), ((0, 0), 0), ((1, 1), 2), ((1, 1), 2)], (0, 1): [((0, 0), 0), ((0, 0), 0), ((1, 1), 0), ((1, 1), 0)], (1, 1): [((0, 1), 3), ((1, 0), 0), ((0, 1), 3), ((1, 0), 0)]}
print(shortest_distance(graph, (0,0), (1,1)))
