import sys

def euler(n):
    return n*(n+1)/2

T = raw_input().strip().split()[0]
for i in range(int(T)):
    N = int(raw_input().strip().split()[0]) - 1
    print 3*euler(N/3) + 5*euler(N/5) - 15*euler(N/15)
        
