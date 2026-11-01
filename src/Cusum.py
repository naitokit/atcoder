# -----------------------------------
# 1次元
# -----------------------------------
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

# -----------------------------------
# 2次元
# -----------------------------------
def Cusum2D(lis):
    """
    2次元累積和を計算する。

    Args:
        lis (list[list[int]]): 累積和を計算する2次元リスト。

    Returns:
        list[list[int]]: 2次元累積和のリスト。
            Cusum[i][j] は、
            lis[0][0] から lis[i][j] までの
            矩形領域の要素の総和。

    Time Complexity:
        O(H * W)
        H は入力リストの行数、W は列数。

    Space Complexity:
        O(H * W)

    Example:
        lis = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

        Cusum = [
            [1,  3,  6],
            [5, 12, 21],
            [12, 27, 45]
        ]
    """
    H = len(lis)
    W = len(lis[0])

    Cusum = [[0]*W for _ in range(H)]

    for i in range(H):
        for j in range(W):
            if i == 0 and j == 0:
                Cusum[i][j] = lis[i][j]
            elif i == 0:
                Cusum[i][j] = Cusum[i][j-1] + lis[i][j]
            elif j == 0:
                Cusum[i][j] = Cusum[i-1][j] + lis[i][j]
            else:
                Cusum[i][j] = (
                    Cusum[i-1][j]
                    + Cusum[i][j-1]
                    - Cusum[i-1][j-1]
                    + lis[i][j]
                )

    return Cusum

def GetSum2D(Cusum, x1, y1, x2, y2):
    """
    2次元累積和から矩形領域の総和を取得する。
    座標は0-indexed、両端を含む。

    Args:
        Cusum (list[list[int]]): 2次元累積和。
        x1 (int): 矩形領域の左上の行番号。
        y1 (int): 矩形領域の左上の列番号。
        x2 (int): 矩形領域の右下の行番号。
        y2 (int): 矩形領域の右下の列番号。

    Returns:
        int: 矩形領域の総和。

    Time Complexity:
        O(1)
    """
    ans = Cusum[x2][y2]

    if x1 > 0:
        ans -= Cusum[x1-1][y2]

    if y1 > 0:
        ans -= Cusum[x2][y1-1]

    if x1 > 0 and y1 > 0:
        ans += Cusum[x1-1][y1-1]

    return ans