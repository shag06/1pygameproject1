n = int(input())
lst = list(map(int, input().split()))
INF = max(lst) + 1
l = [0] * INF
for el in lst:
    l[el - 1] += el
dp = [l[0], l[1]]
for i in range(2, INF):
    dp.append(max(dp[-1], dp[-2] + l[i]))
print(dp[-1])