a = []
for x in range(9, 18):
    a.append(x)

n = int(input())
print(a[n - 1], end = " ")
c = (45 - (int(n/2)*10))
print(f'{c:02}')