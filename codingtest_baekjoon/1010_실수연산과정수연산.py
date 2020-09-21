def fac(n) :
    ans = 1
    if n == 0 :
        return 1
    else :
        for i in range(1, n + 1) :
            ans = ans * i
        return ans

def com(n, r) :
    return fac(n) // fac(r) // fac(n - r)


t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    c = com(b,a)
    print(c)