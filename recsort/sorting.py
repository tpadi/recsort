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


def merge_lists(left_sublist,right_sublist):
    """Return array of items, sorted in ascending order

        Args:
            items (np_array): an array to calculate

        Returns:
            int: all items in array sorted in ascending order

        Examples:
            >>> merge_sort([1,3,2])
            [1,2,3]
            """

    i,j = 0,0
    result = []
    #iterate through both left and right sublist
    while i<len(left_sublist) and j<len(right_sublist):
        #if left value is lower than right then append it to the result
        if left_sublist[i] <= right_sublist[j]:
            result.append(left_sublist[i])
            i += 1
        else:
            #if right value is lower than left then append it to the result
            result.append(right_sublist[j])
            j += 1
    #concatenate the rest of the left and right sublists
    result += left_sublist[i:]
    result += right_sublist[j:]
    #return the result
    return result

def merge_sort(items):
    #if list contains only 1 element return it
    if len(items ) <= 1:
        return items
    else:
        #split the lists into two sublists and recursively split sublists
        midpoint = int(len(items)/2)
        left_sublist = merge_sort(items[:midpoint])
        right_sublist = merge_sort(items[midpoint:])
        #return the merged list using the merge_list function above
        return merge_lists(left_sublist,right_sublist)


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
