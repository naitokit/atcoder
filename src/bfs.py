from collections import deque

class NodeBFS:
    def __init__(self,N,graph):
        self.N = N
        self.graph = graph
    def run(self, start):
        self.que = deque()
        self.dist = [-1]*self.N
        self._bfs(start)
    def _bfs(self,start):
        self.que.appendleft(start)
        self.dist[start] = 0
        while self.que:
            now = self.que.pop()
            for to in self.graph[now]:
                if self.dist[to] != -1:
                    continue
                self.que.appendleft(to)
                self.dist[to] = self.dist[now]+1