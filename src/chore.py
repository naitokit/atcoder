# --------------------------------------------------
# ABC470-D Inverse and Swap で作成.
# 配列の入れ替えや、index/valueの入れ替えを、O(1)で行う.
# --------------------------------------------------
from collections import defaultdict
def mk_dict_index2val_val2index(target_list):
    """
    Create two dictionaries for bidirectional mapping between indices and values.

    The indices are 1-indexed.

    Parameters
    ----------
    target_list : list
        A list of values to be mapped.

    Returns
    -------
    tuple
        A tuple containing two defaultdict objects:

        - index_to_value : defaultdict
            Maps indices to values.
        - value_to_index : defaultdict
            Maps values to indices.

    Notes
    -----
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    index_to_value = defaultdict(int)
    value_to_index = defaultdict(int)

    for i in range(len(target_list)):
        index = i+1
        value = target_list[i]
        index_to_value[index] = value
        value_to_index[value] = index

    return index_to_value, value_to_index


def swap_dict(index_to_value, value_to_index, index1, index2):
    """
    Swap the values at two specified indices and update both dictionaries.
    配列は参照渡しなので、元の配列も変更されることに注意.
    この関数は、元の配列を変更するためのもの.

    Parameters
    ----------
    index_to_value : defaultdict
        Dictionary mapping indices to values.
    value_to_index : defaultdict
        Dictionary mapping values to indices.
    index1 : int
        The first index (1-indexed).
    index2 : int
        The second index (1-indexed).

    Notes
    -----
    Both dictionaries are modified in place.

    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    val1, val2 = index_to_value[index1], index_to_value[index2]
    index_to_value[index1] = val2
    index_to_value[index2] = val1
    value_to_index[val1] = index2
    value_to_index[val2] = index1