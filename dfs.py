def dfs_recursive(G, root):
    visited = set()
    def dfs_helper(G, node):
        print(node)
        for neighbor in G[node]:
            if neighbor not in visited:
                dfs_helper(G, neighbor)
    dfs_helper(G, root)
    
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


def dfs2(G, root):
    # this implementation is more efficient
    stack = list()
    visited = set()

    indices = dict()
    for node in G:
        indices[node] = -1

    stack.append((root, None))
    while stack:
        p = stack[-1]
        current = p[0]
        parent = p[1]
        if indices[current] == -1:
            indices[current] += 1
            print(current)
        if indices[current] < len(G[current]):
            if G[current][indices[current]] != parent:
                stack.append((G[current][indices[current]], current))
            indices[current] += 1
        else:
            stack.pop()


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
dfs2(graph, 1)
