def xor(a, b):
    global n
    ans = []
    now1 = n % 2
    now2 = m % 2
    mass = []
    l = 0
    for i in range(n - 1, -1, -1):
        mass.append(l + a[i])
        l += a[i]
    l = 0
    for i in range(m - 1, -1, -1):
        mass.append(l + b[i])
        l += b[i]
    was = 0
    mass.sort()
    print(mass)
    for i in range(len(mass)):
        ans.append(mass[i] - was)
        was = mass[i]
    if (now1 ^ now2 == 0 and (n + m) % 2 == 1) or (now1 ^ now2 == 1 and (n + m) % 2 == 0):
        del ans[-1]
    ans.reverse()
    return ans


n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(" ".join([str(elem) for elem in xor(a, b) if elem != 0]))


'''
10 8
185 95340 81798 61816 70238 48415 20900 66143 49399 25244
74246 95606 42694 80383 7139 41571 41114 51407

185 85133 10207 64039 17759 61816 16031 42694 11513 48415 20455 445 6694 41571 17878 23236 26163 25244
          10207 64039 17759 61816 16031 42694 11513 48415 20455 445 6694 41571 17878 23236 26163 25244




2 6
76506 77104
42002 74056 29055 1781 1785 8030

3099 38903 37603 36453 29055 1781 1785 8030
3099 38903 37603 36453 29055 1781 1785 8030
'''