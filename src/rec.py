import sys
sys.setrecursionlimit(10**6)

class Reclist:
    """
    与えられた配列から重複を許して配列を作成し、条件を満たす配列の個数を出力.
    ex. lis_Inp = [0,1], N = 3, 2**3=8通り.
    --> lis_Out = [[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],...]

    Attributes
    ----------
    lis_Inp : list
        重複配列の元となる配列.
    N       : int
        作成する重複配列の大きさ.
    lis_tmp : list
        再帰処理で重複配列を作るときの一時配列.
        このオブジェクトに値を追加していく.
    lis_Out : list
        再帰処理で作成した重複配列のリスト.
    """
    def __init__(self,lis_Inp,N):
        """
        初期化.

        Parameters
        ----------
        lis_Inp : list
            重複配列の元となる配列.
        N       ： Int
            作成する重複配列の大きさ.
        """
        self.lis_Inp = lis_Inp
        self.N = N
        return
    def _myfunc(self,lis_tmp):
        """
        作成した重複配列が条件を満たすか判定.

        Parameters
        ----------
        lis_tmp : list
            再帰処理で作成した重複配列.

        Returns
        -------
        flag : Int
        """
        flag = 0
        return flag
    def run(self):
        """
        再帰処理の実行.

        Returns
        -------
        ans : 条件を満たす配列の個数.
        """
        self.ans = 0
        self.lis_tmp = []
        self.lis_Out = []
        self._rec()
        return self.ans
    def run_outlist(self):
        """
        再帰処理の実行.
        重複配列のリストを出力.

        Returns
        -------
        lis_Out : list
            重複配列のリスト.
        """
        self.ans = 0
        self.lis_tmp = []
        self.lis_Out = []
        self._rec()
        return self.lis_Out

    def _rec(self):
        if len(self.lis_tmp) == self.N:
            ### 各重複配列への処理.
            lis_tmp_copy = list(self.lis_tmp) # lis_tmpをlis_outへ値渡し
            self.lis_Out.append(lis_tmp_copy)
            self.ans += self._myfunc(self.lis_tmp)
            return
        for i in range(len(self.lis_Inp)):
            self.lis_tmp.append(self.lis_Inp[i])
            self._rec()
            self.lis_tmp.pop()
        return

class Rec:
    # listの中身を連結した文字の配列を作成
    # ex. lis_Inp=['a','bd','c'] --> ['a','bd','c','abd','ac',...]
    # 連結した文字の大きさはN以下
    def __init__(self,lis_Inp,N):
        self.lis_Inp = lis_Inp
        self.N = N
        return
    def run(self):
        self.set_Out = set() # 重複削除のため、set型
        self._rec('')
        return self.set_Out
    def _rec(self,now):
        if len(now) > self.N:
            return
        self.set_Out.add(now)
        for i in range(len(self.lis_Inp)):
            nex = now + self.lis_Inp[i]
            self._rec(nex)
        return