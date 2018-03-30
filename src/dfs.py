graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['B']),
         'D': set(['E']),
         'E': set(['D'])}

# def dfs_paths(graph, start, goal):
#     stack = [(start, [start])]
#     while stack:
#         (vertex, path) = stack.pop()
#         print(vertex, path)
#         for next in graph[vertex] - set(path):
#             if next == goal:
#                 yield path + [next]
#             else:
#                 stack.append((next, path + [next]))
                
                
def dfs_paths(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        yield path
    for next in graph[start] - set(path):
        yield from dfs_paths(graph, next, goal, path + [next])


print(list(dfs_paths(graph, 'A', 'E')))