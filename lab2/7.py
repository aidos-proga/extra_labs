def Election(x,y,z):
    cntT = 0
    cntF = 0
    a = [x,y,z]
    for i in range(3):
        if a[i] == False: cntF += 1
        else: cntT += 1 
    if cntT >= cntF:
        print(1)
    else: print(0)

x,y,z = map(int, input().split())
x = bool(x)
y = bool(y)
z = bool(z)
Election(x,y,z)

