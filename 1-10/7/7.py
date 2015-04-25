
N = 100000
primes  = [i for i in range(2,N)]

i=0
while primes[i]*primes[i] <= primes[-1]:
    nextPrime = primes[i]
    primes = filter(lambda x: x % nextPrime != 0 or x == nextPrime, primes)
    i+=1

T = raw_input().strip().split()[0]
for i in range(int(T)):
    n = int(raw_input().strip().split()[0])
    print primes[n-1]
