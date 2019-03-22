from recsort import myFunction

def test_sum_array():
    """
    make sure sum_array works correctly
    """
    assert myFunction.sum_array([1, 1, 1, 1, 1]) == 5, 'incorrect'
    assert myFunction.sum_array([3]) == 3, 'incorrect'
    assert myFunction.sum_array([-1, -1, -1]) == -3, 'incorrect'

def test_fibonacci():
    """
    make sure fibonacci works correctly
    """
    assert myFunction.fibonacci([0]) == 0, 'incorrect'
    assert myFunction.fibonacci([1]) == 1, 'incorrect'
    assert myFunction.fibonacci([2]) == 1, 'incorrect'
    assert myFunction.fibonacci([3]) == 2, 'incorrect'
    assert myFunction.fibonacci([4]) == 3, 'incorrect'
    assert myFunction.fibonacci([5]) == 5, 'incorrect'
    assert myFunction.fibonacci([10]) == 55, 'incorrect'

def test_factorial():
    """
    make sure factorial works correctly
    """
    assert myFunction.factorial([0]) == 0, 'incorrect'
    assert myFunction.factorial([1]) == 1, 'incorrect'
    assert myFunction.factorial([2]) == 2, 'incorrect'
    assert myFunction.factorial([3]) == 6, 'incorrect'
    assert myFunction.factorial([8]) == 40320, 'incorrect'

def test_reverse():
    """
    make sure reverse works correctly
    """
    assert myFunction.reverse(['word']) == 'drow', 'incorrect'
    assert myFunction.reverse(['reverse this']) == 'siht esrever', 'incorrect'
    assert myFunction.reverse(['this is a longer sentence that you will need to reverse']) == 'esrever ot deen lliw uoy taht ecnetnes regnol a si siht', 'incorrect'

def test_bubble_sort():
    """
    make sure bubble_sort works correctly
    """
    assert myFunction.bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5], 'incorrect'
    assert myFunction.bubble_sort([10, 91, 2, 13, 3, 1]) == [1, 2, 3, 10, 13, 91], 'incorrect'

def test_merge_sort():
    """
    make sure merge_sort works correctly
    """
    assert myFunction.merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5], 'incorrect'
    assert myFunction.merge_sort([10, 91, 2, 13, 3, 1]) == [1, 2, 3, 10, 13, 91], 'incorrect'

def test_quick_sort():
    """
    make sure quick_sort works correctly
    """
    assert myFunction.quick_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5], 'incorrect'
    assert myFunction.quick_sort([10, 91, 2, 13, 3, 1]) == [1, 2, 3, 10, 13, 91], 'incorrect'
