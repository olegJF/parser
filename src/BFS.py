import collections

def bfs(graph, start, goal):
    # печать того, что мы нашли
    frontier = collections.deque()
    path = []
    frontier.append(start)
    path.append(start)
    visited = []
    leaves = []
    
    i=0
    
    while i<10:
        current = frontier.pop()
        visited.append(current)
        print("visited" , visited)
        if current == goal:
            print("Done" , visited)
            leaves.append(current)
            visited.remove(current)
        if current in graph:
            next_points = graph[current]
        
            for next in next_points:
                if next not in visited:
                    if next not in leaves:
                        frontier.append(next)
        else:
            leaves.append(current)
            visited.remove(current)    
        
        # print(frontier)
        
        # for next in :
        #     print(next)
        #     if next not in visited:
        #         frontier.append(next)
        #         visited[next] = current
        i+=1

graph = {
    'A': {'B':['t1'], 'C':['t3', 't7']},
    'B': {'A':['t6'], 'E':['t5'], 'D':['t2']},
    'C': {'B':['t4']},
    'D': {'E':['t6'], 'F':['t9']},
    'E': {'D':['t8']}
    
}

t = bfs(graph, 'A', 'E')