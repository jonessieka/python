import math

t = int(input())
for _ in range(t):
    x,y = map(int,input().split())

    a = y-x
    b = math.sqrt(a)
    c = b / int(b)
    d = int(b)

    if c == 1.0:
        print(2 * d - 1)
    else:
        if a > ((d + 1) ** 2) - (d + 1):
            print(2 * (d + 1) - 1)
        elif a <= ((d + 1) ** 2) - (d + 1):
            print(2 * (d + 1) - 2)
