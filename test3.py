n = int(input())
lst = [i for i in range(1, n + 1)]
ind1 = 0
ind2 = 0
summ = 0
ans = lst[0]
while ind1 < n and ind2 < n:
    if summ == n:
        ans += 1
    if summ <= n:
        summ += lst[ind2]
        ind2 += 1
    else:
        summ -= lst[ind1]
        ind1 += 1
print(ans)