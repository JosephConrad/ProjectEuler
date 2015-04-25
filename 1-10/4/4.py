def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    return a*b/gcd(a,b)

def main():
    tab = [0,1]
    for i in range(2,41):
        tab.append(lcm(tab[-1], i))
    
    T = raw_input().strip().split()[0]
    for i in range(int(T)):
        n = int(raw_input().strip().split()[0])
        print tab[n]
    
main()
