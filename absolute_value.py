def absolute_value(x):
    """Returns absolute value of x.

    >>>absolute_value(4)
    4
    >>>absolute_value(-3)
    3

    """

    if x < 0:
        return -x
    elif x == 0:
        return 0
    else:
        return x
