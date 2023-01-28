def combination(n, k):
    if k == 0:
        return 1
    if n == 0:
        return 0
    return n * combination(n - 1, k - 1) // k


print(combination(7, 3))