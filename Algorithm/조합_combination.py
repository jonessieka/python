import copy

def combination(arr, r):
    a=[]
    def generate(chosen):
        if len(chosen) == r:
            print(chosen)
            b=copy.deepcopy(chosen)
            a.append(b)
            return

        start = arr.index(chosen[-1]) + 1 if chosen else 0
        for nxt in range(start, len(arr)):
            chosen.append(arr[nxt])
            generate(chosen)
            chosen.pop()
    generate([])
    return a


b=combination('ABCDE', 2)
print(b)
c=combination([1, 2, 3, 4, 5], 3)
print(c)