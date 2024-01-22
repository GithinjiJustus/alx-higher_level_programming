def magic_calculation(a, b):
    """
    Replicates the given Python bytecode using equivalent Python code.

    Args:
        a: First parameter.
        b: Second parameter.

    Returns:
        Result of the computation.
    """
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            result += a ** b / i
        except:
            result = b + a
            break
    return result
