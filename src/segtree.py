def segfunc(x,y):
    # return min(x,y)
    # return max(x,y)
    # return x+y
    # return x*y
    return

class Segtree:
    """
    SegmentTreeのクラス.
    init_val=[x,x,x,...,x]のN次元の配列に対し、区間[l,r]への処理をO(logN)で実行.
    処理は、segfuncで入力.
    単位元が存在、結合則が成立する処理を反映可能.
        ex. min/max/sum/掛け算
        単位元：min(無限)、max(-無限)、足し算(0)、掛け算(1) 
    """
    def __init__(self, init_val, segfunc, ide_ele):
        """
        セグ木(self.tree)の初期化.

        ini_val[i]は、tree[self.num+i]に格納.
            init_val[0] -> tree[self.num+0]
            init_val[1] -> tree[self.num+1]

        上部のNode
            tree[1] ~ tree[self.num-1]
        最下部のNode(葉の部分、配列の要素)
            tree[self.num] ~ tree[2*self.num-1].
            tree[self.num+i] = init_val[i]
            ただし、tree[self.num+N]からは、ide_valが格納.
        接続関係
            tree[i]
                tree[2*i]
                tree[2*i+1]

        ex. init_val=[a0,a1,a2,a3,a4,a5]、N=6.
            self.num = 8(=2**3 < len(A))
            tree[1]:a0-a7の処理結果
                tree[2]:a0-a3
                    tree[4]:a0-a1
                        tree[8]:a0 <- self.num
                        tree[9]:a1
                    tree[5]:a2-a3
                        tree[10]:a2
                        tree[11]:a3
                tree[3]:a4-a7
                    tree[6]:a4-a5
                        tree[12]:a4
                        tree[13]:a5
                    tree[7]:a6-a7 <- self.num-1
                        tree[14]:a6                 2の累乗になるように単位元として追加.
                        tree[15]:a7 <- 2*self.num-1 2の累乗になるように単位元として追加. 
        Parameters
        ----------
        init_val : list
            処理したい1次元の配列.
        segfunc : func
            関数
        ide_ele : val
            単位元

        Attributes
        ----------
        self.segfunc : func
            関数
        self.ide_ele : val
            単位元
        self.num : int
            init_valのサイズ以上で最小の冪乗数
            セグ木における葉の数に相当し、セグ木のサイズを規定.
            ex. N=6なら、self.num=8(=2**3)
        self.tree : list
            セグ木. 
            tree[0]は使わず、tree[1]以降が有効.
        """
        N = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (N-1).bit_length()
        self.tree = [ide_ele]*2*self.num
        """
        self.treeの初期化1. 葉の設定.
        tree[self.num] ~ tree[2*self.num-1]を更新.
            tree[self.num] ~ tree[self.num+N-1]は、配列の値を格納.
            tree[self.num+N] ~ [2*self.num-1]は、更新せずide_valを格納.
        """
        for i in range(N):
            self.tree[self.num+i] = init_val[i]
        """
        self.treeの初期化2. 枝の設定.
        tree[self.num-1] ~ tree[1]までを更新.
            tree[i] = segfunc(xs=tree[2*i], y=tree[2*i+1])
            下から更新していく.
        """
        for i in range(self.num-1, 0, -1):
            self.tree[i] = self.segfunc(x=self.tree[2*i], y=self.tree[2*i+1])
    def update(self,k,x):
        """
        init_valの要素の更新.
        init_val[k] = xにしたときにtreeを更新する.
        kは、init_val=[a0,a1,...,an-1]のindex
        計算量は、O(logN)

        Parameters
        ----------
        k : int
            配列のインデックス
        x : val
            配列の値
        """
        k += self.num
        self.tree[k] = x
        while k >= 2:
            k = k//2 # k//2とすると1つ上のNodeになる.
            self.tree[k] = self.segfunc(x=self.tree[2*k], y=self.tree[2*k+1])

    def query(self, left_target, right_target, l, r, u):
        """
        区間[left,right)のおけるsegfuncの値を計算.
        indexは、init_val=[a1,a2,...,an]として指定.
        ex init_val=[a0,a1,a2,...,ak]における、[a2,..,a5]の区間を見たい場合、
            left = 2+1 = 3(1-indexに変更)
            right = 5+1+1 = 7(1-indexに変更 & rightが開区間なので1つ増やす)
        
        Parameters
        ----------
        left_target : int
            求めたい区間におけるleft側のindex番号.
            init_valにおける1-index.
        right_target : int
            求めたい区間におけるright側のindex番号
            init_valにおける1-index.
            探索範囲にrightは含まない.
        l : int
            2分探索に使うlの値.
            初期値はleft側の全探索区間.
            1-indexなので、初期値は1
        r : int
            2分探索に使うrの値.
            初期値はright側の全探索区間.
            1-indexなのとrは開区間なので、初期値は、self.num+1
            2**N乗になるように水増しした配列であることに注意.
        u : int
            2分探索に使う値.
            a~bの区間に相当するtree番号
        """
        if (right_target <= l) or (r <= left_target):
            return self.ide_ele
        if (left_target <= l) and (r <= right_target):
            return self.tree[u]
        mid = (l+r)//2
        ansL = self.query(left_target=left_target, right_target=right_target, l=l, r=mid, u=2*u)
        ansR = self.query(left_target=left_target, right_target=right_target, l=mid, r=r, u=2*u+1)
        return self.segfunc(x=ansL, y=ansR)