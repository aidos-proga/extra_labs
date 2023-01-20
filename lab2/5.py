b = int(input())

num = 0
i = 1
while b != 0:
    r = b % 10
    num = num + (r*i)
    i = i*2
    b = int(b/10)

print(num)
# 1001