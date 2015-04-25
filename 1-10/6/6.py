

a = [[0] * 10001 for i in range(3)]

a[0][1]=1
a[1][1]=1
a[2][1]=1
for i in range(2, 10001):
    a[0][i]=a[0][i-1]+pow(i, 2)
    a[1][i]=a[1][i-1]+i
    a[2][i]=pow(a[1][i], 2)
 

T = raw_input().strip().split()[0]
for i in range(int(T)):
    n = int(raw_input().strip().split()[0])
    print a[2][n] - a[0][n]
