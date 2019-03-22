def sum_array(array):

    """Return sum of all items in array

    Args:
        n (int): an array to calculate

    Returns:
        int: sum of all items in array

    Examples:
        >>> sum_array()
        1
    """
    if len(array)==0:
        return 0
    else:
        return array[0] + sum_array(array[1:])


def fibonacci(n):

    """Return nth term in fibonacci sequence

    Args:
        n (int): nth term in fibonacci sequence to calculate

    Returns:
        int: nth term of fibonacci sequence,
             equal to sum of previous two terms

    Examples:
        >>> fibonacci(1)
        1
        >> fibonacci(2)
        1
        >> fibonacci(3)
        2
    """

    if n <= 1:
        return n

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def factorial(n):

    """Return n!

    Args:
        n (int): any integer value

    Returns:
        int: factorial of an integer n, which is the product of all preceding integer values

    Examples:
        >>> factorial(1)
        1
        >> factorial(2)
        2
    """
    if n == 1:
        return n
    else:
        return n * factorial(n-1)

def reverse(word):

    """Return word in reverse

    Args:
        word (str): word to reverse

    Returns:
        str: word in reverse

    Examples:
        >>> reverse(word)
        drow
        >> reverse(play)
        yalp
    """

    if len(word) == 0:
        return word
    else:
        return reverse(word[1:]) + word[0]
