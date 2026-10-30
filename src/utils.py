def merge_intervals(intervals):
    """
    重複する区間をマージし、重複のない区間リストを返す。
    ex. intervals = [[2,5], [4,8], [10,11]]
        return = [[2,8], [10,11]]

    Args:
        intervals (list[list[int]]):
            各区間の [left, right] を格納したリスト。
            閉区間 [left, right] として扱う。

    Returns:
        list[list[int]]:
            重複する区間を統合した区間リスト。
            各区間は [left, right] の形式で、
            left の昇順にソートされている。

    Time Complexity:
        O(N log N)
        N は入力区間数。ソートに O(N log N)、
        マージ処理に O(N) かかる。

    Space Complexity:
        O(N)
        マージ結果を格納するための領域。

    Example:
        >>> merge_intervals([[1, 5], [3, 7], [10, 15], [12, 20]])
        [[1, 7], [10, 20]]
    """
    if not intervals:
        return []

    intervals.sort()

    ans = []
    left, right = intervals[0]

    for l, r in intervals[1:]:
        if l <= right:
            right = max(right, r)
        else:
            ans.append([left, right])
            left, right = l, r

    ans.append([left, right])

    return ans