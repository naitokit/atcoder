def Cusum1D(lis):
    """
    1次元累積和を計算する。

    Args:
        lis (list[int]): 累積和を計算する数列。

    Returns:
        list[int]: 累積和のリスト。
            Cusum[i] = lis[0] + lis[1] + ... + lis[i]

    Time Complexity:
        O(N)
        N は入力リストの要素数。

    Space Complexity:
        O(N)

    Example:
        lis = [1, 2, 3, 4, 5]
        Cusum = [1, 3, 6, 10, 15]
    """
    Cusum = [0]*(len(lis))
    for i in range(len(lis)):
        if i == 0:
            Cusum[i] = lis[i]
        else:
            Cusum[i] = Cusum[i-1]+lis[i]
    return Cusum

def imos1D(lisLR,N):
    """
    1次元imos法(閉区間)

    Args:
        lisLR: [left, right] の区間リスト（0-indexed）
        N: 配列の長さ

    Returns:
        各位置が区間に含まれる回数
    """
    lis_imos = [0] * N
    for i in range(len(lisLR)):
        left = lisLR[i][0]
        right = lisLR[i][1]
        lis_imos[left] += 1
        if right != N-1:
            lis_imos[right+1] -= 1
    return Cusum1D(lis=lis_imos)