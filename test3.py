t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    if 0 in [n % m, m % n]:
        print(max(m, n) - 1)
        if m == max(m, n):
            for j in range(max(m, n) - 1):
                print(-1, end=" ")
        else:
            for j in range(max(m, n) - 1):
                print(1, end=" ")
    elif min(n, m) == 2:
        print(max(m, n))
        if m == max(m, n):
            for j in range(max(m, n)):
                if j % 2 == 0:
                    print(3, end=" ")
                else:
                    print(-4, end=" ")
        else:
            for j in range(max(m, n)):
                if j % 2 == 0:
                    print(-3, end=" ")
                else:
                    print(4, end=" ")
    print()