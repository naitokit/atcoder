class UnionFind:
    # UFを作成する途中で処理を追加するのは注意
    # クラスタの親番号が途中で切り替わる可能性あり。
    def __init__(self,n):
        # parents[x] --> 正:xの親のnodeの番号,負:親node.値は要素数
        # 初期状態はすべて親,要素数は自分自身で1個
        self.n = n
        self.parents = [-1]*n
    def find(self,x):
        # ノードxのルートノードを探索
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    def union(self,x,y):
        # xの親(root_x)とyの親(root_y)を比較。要素数が多い方を新たな親とする。
            # 値の更新(root_xが新規親)
            # parents[root_x] += parents[root_y]：root_yの要素数をroot_xへ追加
            # parents[root_y] = root_x：root_yの親をroot_xへ変更
            # parenst[x],parents[y]：子なら変更なし。親のときのみ更新される
            # 親は一番最初にunionされるときに決まり、要素数が同じならxが親となる。
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        if self.parents[root_x] > self.parents[root_y]:
            root_x,root_y = root_y,root_x
        self.parents[root_x] += self.parents[root_y]
        self.parents[root_y] = root_x
        return
    def run_update_parents(self,x):
        # xを始点とするときの経路上のnodeの親をroot_xに更新する。
        # 再帰処理なので、実際の更新は__rec_update_parents
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
            self.parents[x] = root_x
            self.__rec_update_parents(parents,root_x)
    def union2(self,x,y,set_node):
        # 通常通りunionする
        # ただし、xとyがset_nodeに含まれる場合は親をx or yに変更する。
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
            self.parents[root_x] = x
            self.parents[x] = tmp
        if y in set_node:
            tmp = self.parents[root_y]
            self.parents[root_y] = y
            self.parents[y] = tmp
        return