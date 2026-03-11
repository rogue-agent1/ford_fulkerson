#!/usr/bin/env python3
"""Ford-Fulkerson max flow via Edmonds-Karp (BFS augmenting paths)."""
from collections import deque
import sys

class MaxFlow:
    def __init__(self, n):
        self.n = n
        self.graph = [[0]*n for _ in range(n)]
    def add_edge(self, u, v, cap):
        self.graph[u][v] += cap
    def _bfs(self, s, t, parent):
        visited = [False]*self.n; visited[s] = True
        q = deque([s])
        while q:
            u = q.popleft()
            for v in range(self.n):
                if not visited[v] and self.graph[u][v] > 0:
                    visited[v] = True; parent[v] = u; q.append(v)
                    if v == t: return True
        return False
    def max_flow(self, s, t):
        parent = [-1]*self.n; flow = 0
        while self._bfs(s, t, parent):
            path_flow = float('inf'); v = t
            while v != s:
                u = parent[v]; path_flow = min(path_flow, self.graph[u][v]); v = u
            v = t
            while v != s:
                u = parent[v]; self.graph[u][v] -= path_flow; self.graph[v][u] += path_flow; v = u
            flow += path_flow; parent = [-1]*self.n
        return flow
    def min_cut(self, s):
        visited = [False]*self.n; q = deque([s]); visited[s] = True
        while q:
            u = q.popleft()
            for v in range(self.n):
                if not visited[v] and self.graph[u][v] > 0:
                    visited[v] = True; q.append(v)
        return [(u,v) for u in range(self.n) for v in range(self.n) if visited[u] and not visited[v] and (self.graph[u][v] > 0 or self.graph[v][u] > 0)]

if __name__ == "__main__":
    mf = MaxFlow(6)
    edges = [(0,1,16),(0,2,13),(1,2,10),(1,3,12),(2,1,4),(2,4,14),(3,2,9),(3,5,20),(4,3,7),(4,5,4)]
    for u,v,c in edges: mf.add_edge(u,v,c)
    print(f"Max flow: {mf.max_flow(0, 5)}")  # 23
