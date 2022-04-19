def sqrt(n):
    x = n / 2
    # How much x shifts each iteration
    shift = x / 2
    
    i = 0
    # Number of iterations defines accuracy
    maxIterations = 10000
    # While sqrt is not found and iterations is less than maxIterations
    while (x**2 != n and i < maxIterations):
        # If x**2 is larger than n
        if (x**2 > n):
            # Lower by shift
            x -= shift
        else:
            # Otherwise increase by shift
            x += shift
        
        # Half shift
        shift /= 2
        # Increase no. iterations by 1
        i += 1

    # Return aproximated sqrt(n)
    return x
