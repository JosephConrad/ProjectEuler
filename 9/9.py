
MAX = 3001

result = [-1] * MAX
for a in range(1, MAX):
    a2 = pow(a, 2)
    for b in range(a+1, MAX):
        b2 = b*b;
        c2 = a2 + b2;
        c=int(c2**(1.0/2.0))
        if b > c:
            continue
        n = a + b + c
        if pow(c,2) == c2 and n < MAX:
            result[n] = max(result[n], a*b*c )

T = raw_input()
for t in range(0,int(T)):
    test = raw_input()
    print result[int(test)]
