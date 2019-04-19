from queue import Queue


def bfs(G, root):
    visited = set()
    visited.add(root)
    queue = Queue()
    queue.put(root)
    while queue.qsize() > 0:
        current_node = queue.get()
        print(current_node)
        for node in G[current_node]:
            if node not in visited:
                visited.add(node)
                queue.put(node)


graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6, 7],
    4: [2],
    5: [2],
    6: [3],
    7: [3]
}

bfs(graph, 1)
