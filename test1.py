n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
num1 = ""
for i in range(n):
    now = "1" if i % 2 == 0 else "0"
    num1 += now * a[i]
num2 = ""
for i in range(m):
    now = "1" if i % 2 == 0 else "0"
    num2 += now * b[i]
num1 = int(num1, 2)
num2 = int(num2, 2)
num3 = num1 ^ num2
num3 = bin(num3)[2:]
ans = ""
now = "1"
cnt = 0
for elem in num3:
    if now == elem:
        cnt += 1
    else:
        ans += str(cnt) + " "
        cnt = 1
        now = elem
ans += str(cnt)
print(ans)