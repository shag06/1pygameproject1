n = int(input())
lst = [list(map(int, input().split())) for i in range(n)]
l = []
for i in range(n):
    elem = lst[i]
    for j in range(3):
        l.append(sorted([[elem[2 * j], elem[2 * j + 1]]]))
flag = False
for elem in l[:3]:
    flag = flag or l.count(elem) >= n
if flag:
    for row in lst:
        for elem in row:
            print(elem, end=" ")
        print()
else:
    print("NO")