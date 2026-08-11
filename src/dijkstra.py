import heapq
class Dijkstra:
    def __init__(self,N,graph):
        self.N = N
        self.graph = graph
        self.road = [-1]*N
        self.cur = [10**20]*N
    def run(self,start_node):
        self._dijkstra(start_node)
    def _dijkstra(self,start_node):
        Que = []
        heapq.heapify(Que)
        kakutei = [0]*self.N
        self.cur[start_node] = 0
        heapq.heappush(Que,[self.cur[start_node],start_node])
        while Que:
            now = heapq.heappop(Que)[1]
            if kakutei[now] == 1:
                continue
            else:
                kakutei[now] = 1
                for i in range(len(self.graph[now])):
                    to = self.graph[now][i][0]
                    cost = self.graph[now][i][1]
                    if self.cur[now]+cost < self.cur[to]:
                        self.cur[to] = self.cur[now]+cost
                        self.road[to] = now
                        heapq.heappush(Que,[self.cur[to],to])