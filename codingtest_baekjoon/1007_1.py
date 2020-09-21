import sys
input = sys.stdin.readline
import copy
import math

def combination(arr, r):
    a=[]
    def generate(chosen):
        if len(chosen) == r:
            b=copy.deepcopy(chosen)
            a.append(b)
            return

        start = arr.index(chosen[-1]) + 1 if chosen else 0   # 중복된 값의 인댁스를 찾을때 예를들면(5,-5,5)에서 첫번째 5와 세번째 5 문제가됨
        for nxt in range(start, len(arr)):
                chosen.append(arr[nxt])
                generate(chosen)
                chosen.pop()
    generate([])
    return a

t = int(input())

for _ in range(t):
    n = int(input())
    total_x = 0
    total_y = 0
    arr_x = []
    arr_y = []
    cho_x=[]
    cho_y=[]
    nn=n/2

    result = math.inf
    for _ in range(n):
        x, y= map(int, input().split())

        total_x += x
        total_y += y

        arr_x.append(x)
        arr_y.append(y)

    cho_x=copy.deepcopy(combination(arr_x, nn))
    cho_y=copy.deepcopy(combination(arr_y, nn))
    cho_xy=[]

    for i in range(len(cho_x)):
        sumx=0
        sumy=0
        for j in range(int(nn)):
            sumx += cho_x[i][j]
            sumy += cho_y[i][j]
        result = min(result, math.sqrt((sumx - (total_x - sumx)) ** 2 + (sumy - (total_y - sumy)) ** 2))



    print(result)