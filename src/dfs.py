import sys
sys.setrecursionlimit(10**6)

class GridDFS:
    """
    Gridグラフの深さ優先探索.
    
    Attributes
    ----------
    graph : list
        対象のGridグラフ.
    H : int
        graphの行数
    W : int
        graphの列数
    visited : list
        graph[y][x]が探索済みか.
    Dxy : list
        移動方向.
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
    def _Is_valid_graph(self, y, x):
        """
        (x,y)が有効な座標か判定.判定は次の3つ.
        graphの内部か、探索済みか、壁か、
        
        Parameters
        ----------
        x : int
        y : int
        """
        if x < 0 or  self.W <= x or y < 0 or self.H <= y:
            return 0
        elif self.visited[y][x] == 1:
            return 0
        elif self.graph[y][x] == '#':
            return 0
        else:
            return 1
    def _dfs(self, x, y):
        """
        dfsの処理.
        
        Parameters
        ----------
        x : int
        y : int
        """
        # ----------------------------------------
        # (x,y)に来たときの、最初の処理.
        # 最初の1度だけ処理される.
        # visitedの更新など.
        self.visited[y][x] = 1
        # ----------------------------------------
        for dx, dy in self.Dxy:
            # ----------------------------------------
            # (x,y)に来たときに処理
            # 最初のときと、戻ってきたときに処理される.
            # 次の座標更新など.
            nx = x + dx
            ny = y + dy
            # ----------------------------------------
            if self._Is_valid_graph(ny, nx) == 0:
                continue
            else:
                self._dfs(nx, ny)
                # ----------------------------------------
                # (x,y)に戻ってきたときの処理.
                # 戻ってくると、self._dfsから再開される.
                # self.visited[ny][nx]=0などの再探索の初期化など.
                # ----------------------------------------

    def run_dfs(self, start_x, start_y, Dxy):
        """
        dfsの実行.

        Parameters
        ----------
        start_x : int
        start_y : int
        Dxy : list
            縦横のみ -> Dxy=[[1,0],[-1,0],[0,1],[0,-1]]
            縦横斜め -> Dxy=[[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,1],[1,-1],[-1,-1]]
        """
        self.visited = [[-1]*self.W for _ in range(self.H)]
        self.Dxy = Dxy
        self._dfs(start_x, start_y)
