def dfs(G, root):
    stack = list()
    stack.append((root, None))  # stores (node, parent)
    visited = set()
    visited.add(root)
    while stack:
        current = stack.pop()
        print(current[0])
        for node in G[current[0]]:
            if node not in visited:
                visited.add(node)
                stack.append((node, current[0]))
            elif node is not current[1]:
                print("Cycle in graph at " + str((node, current[0])))

        last = current


graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6, 7],
    4: [2],
    5: [2],
    6: [3],
    7: [3, 6]
}
"""
     1
    / \
  2     3 
  /\  /  \
 4  5 6 - 7
"""
dfs(graph, 1)
