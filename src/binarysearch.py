def binarysearch_upperbound(lis,val):
    """
    lis[idx] <= valとなる"最大のidx"を探索.
    indexの最大値を返す.
    
    イメージ
    idx:0 1 2  3  4
    val:2 2 10 15 18

    val=1  -> idx=-1(存在しない)
    val=10 -> idx=2
    val=17 -> idx=3
    val=19 -> idx=4

    Parameters
    ----------
    lis : list
        探索対象のリスト.
        ソートされている前提.
    val : float
        探索する値.

    Returns
    ----------
    l : int
        idx
    """
    N = len(lis)
    l = 0
    r = N-1
    if val < lis[0]:
        return -1
    elif val == lis[0]:
        while l < N-1 and lis[l+1] == val:
            l += 1
        return l
    elif val == lis[N-1]:
        return N-1
    elif val > lis[N-1]:
        return N-1
    else:
        while r - l > 1:
            mid = l + (r-l)//2
            if lis[mid] == val:
                while mid < N-1 and lis[mid+1] == val:
                    mid += 1
                return mid
            elif lis[mid] < val:
                l = mid
            else:
                r = mid
        return l

def binarysearch_lowerbound(lis,val):
    """
    val <= lis[idx]となる"最小のidx"を探索.
    最小のindexを返す.
    
    イメージ
    0 1 2  3  4
    2 3 10 18 18

    val=1  -> idx=0
    val=6  -> idx=2
    val=18 -> idx=3
    val=19 -> idx=-1(存在しない)

    Parameters
    ----------
    lis : list
        探索対象のリスト.
        ソートされている前提.
    val : float
        探索する値.

    Returns
    ----------
    l : int
        idx
    """

    N = len(lis)
    l = 0
    r = N-1
    if val < lis[0]:
        return 0
    elif val == lis[0]:
        return 0
    elif val == lis[N-1]:
        while 0 < r and lis[r-1] == val:
            r -= 1
        return r
    elif val > lis[N-1]:
        return -1
    else:
        while r - l > 1:
            mid = l + (r-l)//2
            if lis[mid] == val:
                while 0 < mid and lis[mid-1] == val:
                    mid -= 1
                return mid
            elif lis[mid] < val:
                l = mid
            else:
                r = mid
        return r