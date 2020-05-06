from collections import deque, defaultdict
inf = float('inf')

class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.SIZE = len(graph)

    def bfs(self, s, t, parent):
        visited = [False] * self.SIZE
        queue = deque([s])
        visited[s] = True
        while queue:
            u = queue.popleft()
            for idx, val in enumerate(self.graph[u]):
                if not visited[idx] and val > 0:
                    queue.append(idx)
                    visited[idx] = True
                    parent[idx] = u
        return visited[t]

    def edmonds_karp(self, source, sink):
        parent = [-1] * self.SIZE
        max_f = 0
        while self.bfs(source, sink, parent):
            path_flow = inf
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]
            max_f += path_flow
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
        return max_f

def add_supers(ents, exits, paths):
    total = sum(map(sum, paths))
    deeper = [[0 for _ in paths[0]]] + paths + [[0 for _ in paths[0]]]
    wider = map(lambda row: [0] + row + [0], deeper)
    for e in ents:
        wider[0][e + 1] = total
    for e in exits:
        wider[e + 1][-1] = total
    return wider

def solution(ents, exits, paths):
    supers = add_supers(ents, exits, paths)
    return Graph(supers).edmonds_karp(0, len(supers) - 1)

print solution([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 
0, 0, 0], [0, 0, 0, 0, 0, 0]])

print solution([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]])
