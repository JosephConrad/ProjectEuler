from math import factorial as fac

def binomial(x, y):
    try:
        binom = fac(x) // fac(y) // fac(x - y)
    except ValueError:
        binom = 0
    return binom

T = int(raw_input())
for _ in range(T):
    n,m = map(lambda x: int(x), (raw_input().split(" ")))
    print binomial(n+m, m) % 1000000007
