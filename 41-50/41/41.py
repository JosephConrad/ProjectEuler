import itertools

def sieve(n):
    m = (n-1) // 2
    b = [True]*m
    i,p,ps = 0,3,[2]
    while p*p < n:
        if b[i]:
            ps.append(p)
            j = 2*i*i + 6*i + 3
            while j < m:
                b[j] = False
                j = j + 2*i + 3
        i+=1; p+=2
    while i < m:
        if b[i]:
            ps.append(p)
        i+=1; p+=2
    return ps

def isPrime(number):
    for i in primes:
        if i*i > number: return True
        if number % i == 0: return False
    return True 

primes = sieve(100000)
allPrimes = []

for i in range(2,10):
    perms = itertools.permutations(range(1, i+1))
    perms = map(lambda x: int(''.join(map(str,x))), perms)
    pprimes = filter(isPrime, perms)
    allPrimes.extend(pprimes)

allPrimes.sort()

T = int(raw_input())
for _ in range(T):
    test = int(raw_input())
    done = False
    for elt in reversed(allPrimes):
        if elt <= test:
            done = True
            print elt
            break 
    if not done:
        print -1  
