class UnionFind:
    """
    UnionFindのクラス.
    初期化 : O(1)
    UFを作成する途中で処理を追加するのは注意.
    クラスタの親番号が途中で切り替わる可能性あり.
    処理オブジェクト
        x : node
        root_x : xのルートnode
        parents[x] : xの親node(非負の場合) or xの要素数(負の場合)
    メソッド
        __init__(n) : 初期化(O(1)).
        find(x) : 要素xのルートnodeを探索(O(logN)).
        union(x,y) : xとyを連結させる(O(1)).
        update_parents(x) : xからroot_xまでの経路上のnodeの親をroot_xに変更.
        union2(x,y) : xとyを連結させる(O(1)).その後親を変更?

    Attributes
    ----------
    n : int
        要素数
    parents :list
        サイズはn.
        値が非負(0以上)の場合、親nodeを示す.
        値が負の場合、ルートnodeで、絶対値は自身を含む接続された要素数.
    """
    def __init__(self,n):
        """
        Parameters
        ----------
        n : int
            要素数
        """
        self.n = n
        self.parents = [-1]*n
    def find(self,x):
        """
        Parameters
        ----------
        x : int
            要素番号
        
        Returns
        ----------
        xのルートnodeの要素番号
        """
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    def union(self,x,y):
        """
        ノードxとノードyを連結させる.
        xの親(root_x)とyの親(root_y)を比較。要素数が多い方を新たな親とする.
        ここでは、root_xを新規親とする.
        root_x,root_yの処理
            parents[root_x] += parents[root_y]：root_yの要素数をroot_xへ追加
            parents[root_y] = root_x：root_yの親をroot_xへ変更
        x,yの処理
            parents[x],parents[y]：子なら変更なし。親のときのみ更新される
            親は一番最初にunionされるときに決まり、要素数が同じならxが親となる。
        """
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        if self.parents[root_x] > self.parents[root_y]:
            root_x,root_y = root_y,root_x
        self.parents[root_x] += self.parents[root_y]
        self.parents[root_y] = root_x
        return
    def update_parents(self,x):
        """
        xからroot_xまでの経路上のnodeの親をroot_xに変更する.
        この処理で、root_xの直下に経路上のnodeが接続される構造に変更.
        xが親の場合は処理なし.
        再帰処理なので、実際の更新は__rec_update_parents
        """
        if self.parents[x] < 0:
            return
        else:
            root_x = self.find(x)
            self.__rec_update_parents(x,root_x)
    def __rec_update_parents(self,x,root_x):
        parents = self.parents[x]
        if parents < 0:
            return
        else:
            self.parents[x] = root_x # xの親をroot_xに変更
            self.__rec_update_parents(parents,root_x) # xの親も同様の処理.
    def union2(self,x,y,set_node):
        """
        通常通りunionする.
        その後、xがset_nodeに含まれる場合は、root_xの親をxに変更.
        その後、yがset_nodeに含まれる場合は、root_yの親をyに変更.
        良くない？？？
        """
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        if self.parents[root_x] > self.parents[root_y]:
            root_x,root_y = root_y,root_x
        self.parents[root_x] += self.parents[root_y]
        self.parents[root_y] = root_x
        if x in set_node:
            tmp = self.parents[root_x]
            self.parents[root_x] = x # root_xの親をxに変更.
            self.parents[x] = tmp # xがルートなので、parents[x]をroot_xの要素数に変更.
        if y in set_node:
            tmp = self.parents[root_y]
            self.parents[root_y] = y # root_yの親をyに変更.
            self.parents[y] = tmp # yがルートなので、parents[y]をroot_yの要素数に変更.
        return