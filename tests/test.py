from recsort import myFunction

def test_sum_array():
    """
    make sure sum_array works correctly
    """
    assert myFunction.sum_array([1,3,2]) == 6, 'incorrect')

def test_fibonacci():
    """
    make sure fibonacci works correctly
    """
    assert myFunction.fibonacci(3) == 2, 'incorrect'

def test_factorial():
    """
    make sure factorial works correctly
    """
    assert myFunction.factorial(3) == 6, 'incorrect'

def test_reverse():
    """
    make sure reverse works correctly
    """
    assert myFunction.reverse('athena') == 'anehta', 'incorrect'

def test_bubble_sort():
    """
    make sure bubble_sort works correctly
    """
    assert myFunction.bubble_sort([1,3,2]) == [1, 2, 3], 'incorrect'

def test_merge_sort():
    """
    make sure merge_sort works correctly
    """
    assert myFunction.merge_sort([1,3,2]) == [1, 2, 3], 'incorrect'

def test_quick_sort():
    """
    make sure quick_sort works correctly
    """
    assert myFunction.quick_sort([1,3,2]) == [1, 2, 3], 'incorrect'
