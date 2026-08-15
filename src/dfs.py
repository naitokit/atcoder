import sys
sys.setrecursionlimit(10**6)

# -------------------------------------------------------
# GridDFS系
# -------------------------------------------------------
class GridDFS:
    """
    Gridグラフの深さ優先探索の基本クラス.
    
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

class GridDFS_is_route:
    """
    Gridグラフに対し、startからendまでの経路が存在するかの判定.
    startとgoalをrunメソッドに渡して、dfsで探索.
    """
    def __init__(self, graph):
        self.graph = graph
        self.H = len(graph)
        self.W = len(graph[0])
        self.ans = 0
    def _Is_valid_graph(self, y, x):
        if x < 0 or  self.W <= x or y < 0 or self.H <= y:
            return 0
        elif self.visited[y][x] == 1:
            return 0
        elif self.graph[y][x] == '#':
            return 0
        else:
            return 1
    def _dfs(self, x, y):
        self.visited[y][x] = 1
        if y == self.goal_y and x == self.goal_x:
            self.ans = 1
        for dx, dy in self.Dxy:
            nx = x + dx
            ny = y + dy
            if self._Is_valid_graph(ny, nx) == 0:
                continue
            else:
                self._dfs(nx, ny)
    def run_dfs(self, start_x, start_y, goal_x, goal_y, Dxy):
        self.visited = [[-1]*self.W for _ in range(self.H)]
        self.Dxy = Dxy
        self.goal_x = goal_x
        self.goal_y = goal_y
        self._dfs(start_x, start_y)

# -------------------------------------------------------
# NodeDFS系
# -------------------------------------------------------
class NodeDFS:
    """
    Nodeグラフの深さ優先探索の基本クラス.
    
    Attributes
    ----------
    graph : list
        対象のNodeグラフ.
    N : int
        グラフのnode数.
    visited : list
        graph[node]が探索済みか.
    """
    def __init__(self, N, graph):
        """
        Parameters
        ----------
        graph : list
            対象のNodeグラフ.
            N個のnodeで構成.
            graph = [[0番目のnodeに接続されるnode番号],[1番目のnodeに接続されるnode番号],[2番目のnodeに接続されるnode番号],...]
        """
        self.N = N
        self.graph = graph

    def _dfs(self, node):
        # ----------------------------------------
        # nodeに来たときの、最初の処理.
        # 最初の1度だけ処理される.
        # visitedの更新など.
        self.visited[node] = 1
        # ----------------------------------------
        for nv in self.graph[node]:
            # ----------------------------------------
            # nodeに来たときの次の処理
            # 最初に加え、戻ってきたときにも処理される.
            # 次の座標更新など.
            # ----------------------------------------
            if self.visited[nv] == 0:
                self._dfs(nv)
                # ----------------------------------------
                # nodeに戻ってきたときの処理.
                # 戻ってくると、self._dfsから再開される.
                # self.visited[node]=0などの再探索の初期化など.
                # ----------------------------------------
    def run_dfs(self, start):
        """
        dfsの実行.

        Parameters
        ----------
        start : int
            探索開始するnode番号
        """
        self.visited = [0]*self.N
        if self.visited[start] == 1:
            return
        else:
            self._dfs(start)

class NodeDFS_cnt_connect:
    """
    Nodeグラフにて、連結成分を数え上げるクラス.
    各nodeに対し、
        探索ずみ -> continue
        未探索 -> cnt++して、dfsでvisitedを更新.
    """
    def __init__(self, N, graph):
        self.N = N
        self.graph = graph
    def _dfs(self, node):
        self.visited[node] = 1
        for nv in self.graph[node]:
            if self.visited[nv] == 0:
                self._dfs(nv)
    def run_dfs(self):
        self.visited = [0]*self.N
        self.cnt = 0
        for i in range(self.N):
            if self.visited[i] == 1:
                continue
            else:
                self.cnt += 1
                self._dfs(i)

class NodeDFS_calc_maxcost:
    """
    Nodeグラフの深さ優先探索で、最大コストを計算するクラス.
    _dfs(now,pre,now_cost)の引数は各Nodeに対して割り当てることが可能.
    now_cost
        selfにする場合：Nodeに戻ってきたときに戻す必要あり.
        引数にする場合：各Nodeごとに割り当て割れるので、戻す必要なし.
    
    Attributes
    ----------
    graph : list
        対象のNodeグラフ.
    N : int
        グラフのnode数.
    visited : list
        graph[node]が探索済みか.
    max_cost : int
        最大のコスト.
    """
    def __init__(self, N, graph):
        """
        Parameters
        ----------
        graph : list
            対象のNodeグラフ.
            N個のnodeで構成.
            graph = [[[node,cost],[node,cost]...],[[node,cost],[node,cost]...],[[node,cost],[node,cost]...]
        """
        self.N = N
        self.graph = graph
    def _dfs(self, now, pre, now_cost):
        """
        Parameters
        ----------
        now : int
            現在のNode番号.
        pre : int
            1つ前のNode番号
        now_cost : int
            startからnowまでのコストの合計.
            selfではなく、通常の変数にすることで、各Nodeごとにnow_costが割り当てられる.
        """
        # ----------------------------------------
        # nodeに来たときの、最初の処理.
        # 最初の1度だけ処理される.
        # visitedの更新とmax_costの更新
        self.visited[now] = 1
        self.max_cost = max(self.max_cost, now_cost)
        # ----------------------------------------
        for to,cost in self.graph[now]:
            # ----------------------------------------
            # nodeに来たときの次の処理
            # 最初に加え、戻ってきたときにも処理される.
            # 次の座標更新など.
            # ----------------------------------------
            if to != pre and self.visited[to] == 0:
                self._dfs(now=to, pre=now, now_cost=now_cost+cost)
                # ----------------------------------------
                # nodeに戻ってきたときの処理.
                # 戻ってくると、self._dfsから再開される.
                # self.visited[node]=0などの再探索の初期化など.
                # ----------------------------------------
                self.visited[to] = 0

    def run_dfs_maxcost(self, start):
        """
        dfsの実行.
        startから出発して、取りうる最大のコストを計算.
        self.max_costに格納.

        Parameters
        ----------
        start : int
            探索開始するnode番号
        """
        self.visited = [0]*self.N
        self.max_cost = 0

        if self.visited[start] == 1:
            return -1
        else:
            self._dfs(now=start, pre=-1, now_cost=0)