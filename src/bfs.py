from collections import deque

# -------------------------------------------------------
# GridBFS系
# -------------------------------------------------------
class GridBFS:
    """
    Gridグラフの幅優先探索の基本クラス.
    始点に近いところから順に探索して距離をfixしていく.
    Gridグラフに対し、start位置を入力して、各マス目までの最短距離を計算.
    距離は、self.distに格納.
    
    Attributes
    ----------
    graph : list
        対象のGridグラフ.
    H : int
        graphの行数
    W : int
        graphの列数
    dist : list
        各マス目における(start_x,start_y)からの距離.
    Dxy : list
        移動方向.
    que : deque
        (x,y)を格納するque.
    """
    def __init__(self, graph):
        """
        Parameters
        ----------
        graph : list
            対象のGridグラフ.縦にH行、横にW列.
            graph[y][x]
            0<=y<=H-1
            0<=x<=W-1
            例:H=4, W=3
                graph = [[x,x,x],[x,x,x],[x,x,x],[x,x,x]]
        H : int
            graphの行数
        W : int
            graphの列数
        """
        self.graph = graph
        self.H = len(graph)
        self.W = len(graph[0])
    def _is_valid_graph(self, y, x):
        """
        (x,y)が有効な座標かの判定.判定は次の3つ.
        graphの内部か、探索済みか、壁か。
        bfsは近い距離から探索するので、探索済みは最短距離としてfixしている.
        
        Parameters
        ----------
        x : int
        y : int
        """
        if x < 0 or  self.W <= x or y < 0 or self.H <= y:
            return 0
        elif self.dist[y][x] != -1:
            return 0
        elif self.graph[y][x] == '#':
            return 0
        else:
            return 1
    def run_bfs(self, start_x, start_y, Dxy):
        """
        bfsの実行.

        Parameters
        ----------
        start_x : int
        start_y : int
        Dxy : list
            縦横のみ -> Dxy=[[1,0],[-1,0],[0,1],[0,-1]]
            縦横斜め -> Dxy=[[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,1],[1,-1],[-1,-1]]
        """
        self.que = deque()
        self.dist = [[-1]*self.W for _ in range(self.H)]
        self.Dxy = Dxy
        self._bfs(start_x, start_y)
    def _bfs(self, start_x, start_y):
        """
        bfsの処理.
        
        Parameters
        ----------
        start_x : int
        start_y : int
        """
        self.que.append((start_x, start_y))
        self.dist[start_y][start_x] = 0
        while self.que:
            x,y = self.que.popleft()
            for dx, dy in self.Dxy:
                nx, ny = x+dx, y+dy
                if self._is_valid_graph(y=ny, x=nx) == 1:
                    self.que.append((nx, ny))
                    self.dist[ny][nx] = self.dist[y][x]+1
class GridMultiStartBFS:
    """
    Gridグラフの多始点BFS.
    初期化時に複数の始点をqueに追加してBFS.
    各マス目に対し、最短となる始点までの距離を計算する.
    近い点から距離が決まり、決まった点はqueに追加しないので計算量はO(HxW).
    距離は、self.distに格納.
    
    Attributes
    ----------
    graph : list
        対象のGridグラフ.
    H : int
        graphの行数
    W : int
        graphの列数
    dist : list
        各マス目における最も近い始点からの距離.
    Dxy : list
        移動方向.
    que : deque
        (x,y)を格納するque.
    """
    def __init__(self, graph):
        """
        Parameters
        ----------
        graph : list
            対象のGridグラフ.縦にH行、横にW列.
            graph[y][x]
            0<=y<=H-1
            0<=x<=W-1
            例:H=4, W=3
                graph = [[x,x,x],[x,x,x],[x,x,x],[x,x,x]]
        H : int
            graphの行数
        W : int
            graphの列数
        """
        self.graph = graph
        self.H = len(graph)
        self.W = len(graph[0])
    def _is_valid_graph(self, y, x):
        """
        (x,y)が有効な座標かの判定.判定は次の3つ.
        graphの内部か、探索済みか、壁か。
        bfsは近い距離から探索するので、探索済みは最短距離としてfixしている.
        
        Parameters
        ----------
        x : int
        y : int
        """
        if x < 0 or  self.W <= x or y < 0 or self.H <= y:
            return 0
        elif self.dist[y][x] != -1:
            return 0
        elif self.graph[y][x] == '#':
            return 0
        else:
            return 1
    def run_bfs(self, lis_start, Dxy):
        """
        bfsの実行.

        Parameters
        ----------
        lis_start : list
            始点の候補点.
            1つなら通常のBFS.
            [[x1,y1],[x2,y2],...,[xn,yn]]として入力.
        Dxy : list
            縦横のみ -> Dxy=[[1,0],[-1,0],[0,1],[0,-1]]
            縦横斜め -> Dxy=[[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,1],[1,-1],[-1,-1]]
        """
        self.que = deque()
        self.dist = [[-1]*self.W for _ in range(self.H)]
        self.Dxy = Dxy
        for x,y in lis_start:
            self.que.append((x,y))
            self.dist[y][x] = 0
        self._bfs()
    def _bfs(self):
        """
        bfsの処理.
        """
        while self.que:
            x,y = self.que.popleft()
            for dx, dy in self.Dxy:
                nx, ny = x+dx, y+dy
                if self._is_valid_graph(y=ny, x=nx) == 1:
                    self.que.append((nx, ny))
                    self.dist[ny][nx] = self.dist[y][x]+1
# -------------------------------------------------------
# NodeBFS系
# -------------------------------------------------------
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