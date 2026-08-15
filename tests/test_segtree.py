from src.segtree import Segtree

# =========================
# Simpleなテスト
# =========================
def test_segtree_simple():
    """
    segfunc=maxのサンプル
    """
    lis_test = [0,2,5,7,9,10]
    def segfunc(x,y):
        return max(x,y)
    segtree = Segtree(init_val=lis_test, segfunc=segfunc, ide_ele=-1e-10)
    assert segtree.tree[1] == 10 # 全体のmax

    segtree.update(k=5, x=100) # ここは、lis=[a0,a1,a2,...,an-1]のindex
    assert segtree.tree[1] == 100 # 全体のmax. # lis_test = [0,2,5,7,9,100]

    # ここは、lis=[a1,a2,...,an]のindex
    # rightは開区間に注意
    res = segtree.query(left_target=1, right_target=4, l=1, r=segtree.num+1, u=1) 
    assert res == 5

def range_query(seg, left, right):
    """
    queryメソッドのラッパー
    引数(l,r,u)を固定して、left,rightのみinputとする.
    queryではなく、range_queryからqueryを呼ぶ.
    """
    return seg.query(
        left_target=left,
        right_target=right,
        l=1,
        r=seg.num + 1,
        u=1,
    )

# =========================
# sum
# =========================
def test_sum_initialization():
    def segfunc(x,y):
        return x+y
    seg = Segtree(
        init_val=[1, 2, 3, 4, 5],
        segfunc=segfunc,
        ide_ele=0,
    )
    assert seg.tree[1] == 15

def test_sum_query():
    def segfunc(x,y):
        return x+y
    seg = Segtree(
        init_val=[1, 2, 3, 4, 5],
        segfunc=segfunc,
        ide_ele=0,
    )
    assert range_query(seg, 1, 6) == 15
    assert range_query(seg, 1, 2) == 1
    assert range_query(seg, 2, 4) == 5
    assert range_query(seg, 3, 6) == 12
    assert range_query(seg, 4, 5) == 4
def test_sum_query_empty():
    def segfunc(x,y):
        return x+y
    seg = Segtree(
        init_val=[1, 2, 3, 4, 5],
        segfunc=segfunc,
        ide_ele=0,
    )
    assert range_query(seg, 3, 3) == 0
def test_sum_update():
    def segfunc(x,y):
        return x+y
    seg = Segtree(
        init_val=[1, 2, 3, 4, 5],
        segfunc=segfunc,
        ide_ele=0,
    )
    seg.update(2, 10) # [1,2,10,4,5]
    assert range_query(seg, 1, 6) == 22
    assert range_query(seg, 3, 4) == 10
    assert range_query(seg, 2, 5) == 16

# =========================
# min
# =========================
def test_min_query():
    def segfunc(x,y):
        return min(x,y)
    seg = Segtree(
        init_val=[5, 2, 8, 1, 7],
        segfunc=segfunc,
        ide_ele=float("inf"),
    )
    assert range_query(seg, 1, 6) == 1
    assert range_query(seg, 1, 3) == 2
    assert range_query(seg, 2, 5) == 1
    assert range_query(seg, 3, 6) == 1
def test_min_update():
    def segfunc(x,y):
        return min(x,y)
    seg = Segtree(
        init_val=[5, 2, 8, 1, 7],
        segfunc=segfunc,
        ide_ele=float("inf"),
    )
    seg.update(2, 0)
    assert range_query(seg, 1, 6) == 0
    assert range_query(seg, 3, 4) == 0

# =========================
# max
# =========================
def test_max_query():
    def segfunc(x,y):
        return max(x,y)
    seg = Segtree(
        init_val=[5, 2, 8, 1, 7],
        segfunc=segfunc,
        ide_ele=-float("inf"),
    )
    assert range_query(seg, 1, 6) == 8
    assert range_query(seg, 1, 3) == 5
    assert range_query(seg, 2, 5) == 8
def test_max_update():
    def segfunc(x,y):
        return max(x,y)
    seg = Segtree(
        init_val=[5, 2, 8, 1, 7],
        segfunc=segfunc,
        ide_ele=-float("inf"),
    )
    seg.update(3, 100)
    assert range_query(seg, 1, 6) == 100
    assert range_query(seg, 4, 5) == 100