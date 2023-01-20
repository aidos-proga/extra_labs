n = int(input())
m = int(input())
v = int(input())

if n+m <= v or m+v <= n or v+n <= m:
    print("NO")
else:
    print("YES") 