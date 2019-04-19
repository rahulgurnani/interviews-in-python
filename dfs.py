def dfs(G, root):
    stack = list()
    stack.append(root)
    visited = set()
    visited.add(root)
    while stack:
        current = stack.pop()
        print(current)
        for node in G[current]:
            if node not in visited:
                visited.add(node)
                stack.append(node)


graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6, 7],
    4: [2],
    5: [2],
    6: [3],
    7: [3]
}

dfs(graph, 1)
