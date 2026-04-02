def dfs(graph, start):

    visited, stack = set(), [start]

    result = []  

    while stack:

        vertex = stack.pop()

        if vertex not in visited:

            visited.add(vertex)

            result.append(vertex)

            stack.extend(sorted(graph[vertex], reverse=True))

    return result

graph_a = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['H'],
    'F': [],
    'G': [],
    'H': []
}
print("DFS for Graph A:",(graph_a, 'A'))

