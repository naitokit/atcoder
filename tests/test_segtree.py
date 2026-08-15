from src.segtree import Segtree

def test_segtree_query():

    lis_test = [0,2,5,7,9,10]
    def segfunc(x,y):
        return max(x,y)
    
    segtree = Segtree(init_val=lis_test, segfunc=segfunc, ide_ele=-1e-10)
    res = segtree.query(left_target=1, right_target=4, l=1, r=segtree.num+1, u=1)
    assert res == 5