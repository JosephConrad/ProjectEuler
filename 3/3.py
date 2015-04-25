

T = raw_input().strip().split()[0]
for i in range(int(T)):
    n = int(raw_input().strip().split()[0])
    pFactors = []
    prime = 2
    while True:
        while n % prime == 0:
            n = n/prime
            pFactors.append(prime)
        else:
            prime+=1
        if prime*prime > n:
            if n > 1: pFactors.append(n)
            break
    print pFactors[-1]
    
