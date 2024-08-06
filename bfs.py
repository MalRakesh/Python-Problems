'''Write a program to implement breadth first search algorithm.'''

from collections import deque
# Define the graph
graph1 = {
    'A': set(['B', 'C']),
    'B': set(['A', 'D', 'E']),
    'C': set(['A', 'F']),
    'D': set(['B']),
    'E': set(['B', 'F']),
    'F': set(['C', 'E'])
}
# Define the BFS function
def bfs(graph, start_node):
    visited = []
    queue = deque([start_node])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node] - set(visited))
    return visited
# Perform BFS starting from node 'A'
visited_bfs = bfs(graph1, 'A')
print("Result of BFS:", visited_bfs)
