
def accumu(lis):
    total = 0
    for x in lis:
        total += x
        yield total

x=int(raw_input())
fibo=[0,1]

limit = 10**17
last=fibo[-1]

while last<limit:
    fibo.append(fibo[-1]+fibo[-2])
    last=fibo[-1]

fibo = filter(lambda x: x%2==0, fibo)
res = list(accumu(fibo))


for i in range(x):
    n = int(raw_input())
    i=0
    while fibo[i]<=n: 
        i+=1
    print res[i-1]    
