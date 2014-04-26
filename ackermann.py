def φ(m, n, p):
    """The original Ackermann function."""
    if p == 0:
        return m + n
    elif (n == 0) and (p == 1):
        return 0
    elif (n == 0) and (p == 2):
        return 1
    elif (n == 0):
        assert p > 2
        return m
    else:
        assert n > 0
        assert p > 0
        return φ(m, φ(m, n-1, p), p-1)

def A(m, n):
    """The condensed Ackermann function."""
    if m == 0:
        return n + 1
    elif n == 0:
        assert m > 0
        return A(m-1, 1)
    else:
        assert m > 0
        assert n > 0
        return A(m-1, A(m, n-1))