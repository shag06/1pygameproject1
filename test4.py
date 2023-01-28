from collections import deque


n = int(input())
lst = deque()
for i in range(n - 1):
    a, b = map(int, input().split())
    if not lst:
        lst.append(a)
        lst.append(b)
        continue
    if a in lst:
        ind = lst.index(a)
        lst.insert(ind + 1, b)
    elif b in lst:
        ind = lst.index(b)
        lst.insert(ind, a)
    else:
        lst.append(a)
        lst.append(b)
print(*list(lst))