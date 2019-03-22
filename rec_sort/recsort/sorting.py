def bubble_sort(items):

    """Return array of items, sorted in ascending order

    Args:
        items (np_array): an array to calculate

    Returns:
        int: all items in array sorted in ascending order

    Examples:
        >>> bubble_sort([1,3,2])
        [1,2,3]
    """

    for i, num in enumerate(items):
        try:
            if items[i+1] < num:
                items[i] = items[i+1]
                items[i+1] = num
                bubble_sort(items)
        except IndexError:
            pass
    return items

def merge_sort(items):

    """Return array of items, sorted in ascending order

        Args:
            items (np_array): an array to calculate

        Returns:
            int: all items in array sorted in ascending order

        Examples:
            >>> merge_sort([1,3,2])
            [1,2,3]
    """

    len_i = len(items)

    if len_i == 1:
        return items

    mid_point = int(len_i / 2)

    i1 = merge_sort(items[:mid_point])
    i2 = merge_sort(items[mid_point:])

    return merge(i1, i2)

def quick_sort(items):

    """Return array of items, sorted in ascending order

            Args:
                items (np_array): an array to calculate

            Returns:
                int: all items in array sorted in ascending order

            Examples:
                >>> quick_sort([1,3,2])
                [1,2,3]
    """

    if len(items) <= 1:
        return items
    else:
        return quick_sort([e for e in items[1:] if e <= items[0]]) + [items[0]] +\
            quick_sort([e for e in items[1:] if e > items[0]])
