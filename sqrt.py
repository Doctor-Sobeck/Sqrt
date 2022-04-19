def sqrt(n):
    x = n / 2
    shift = x / 2
    
    i = 0
    # Number of iterations defines accuracy
    maxIterations = 10000
    while (x**2 != n and i < maxIterations):
        if (x**2 > n):
            x -= shift
        else:
            x += shift

        shift /= 2
        i += 1

    return x
