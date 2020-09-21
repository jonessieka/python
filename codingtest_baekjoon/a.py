import math
a=int(input())
b=math.sqrt(a)
c= b/ int(b)
d=int(b)


if c== 1.0:
    print(2*d-1)
else:
    if a>((d+1)**2)-(d+1):
        print(2*(d+1)-1)
    elif a<=((d+1)**2)-(d+1):
        print(2*(d+1)-2)