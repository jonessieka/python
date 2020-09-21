import sys
input = sys.stdin.readline
import copy
import math
import itertools

t = int(input())

for _ in range(t):
    n = int(input())
    total_x = 0
    total_y = 0
    arr_xy= []
    cho_xy=[]
    nn=n/2

    result = math.inf
    for _ in range(n):
        x, y= map(int, input().split())

        total_x += x
        total_y += y

        arr_xy.append([x,y])

    cho_xy=list(itertools.combinations(arr_xy, int(nn)))

    for i in list(cho_xy):
        sumx=0
        sumy=0
        for j in i:
            sumx += j[0]
            sumy += j[1]
        result = min(result, math.sqrt((sumx - (total_x - sumx)) ** 2 + (sumy - (total_y - sumy)) ** 2))



    print(result)