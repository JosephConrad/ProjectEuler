def processNumber(numnber, n, k):
    mul = 1 
    maks = 1
    i = 0
    length = 0
    maksSet = False
    while i < n:
        if number[i] == "0":
            mul = 1
            length = 0
        else:
            mul *= int(number[i])
            length+=1
            if length > k:
                mul /= int(number[i-k])
                length-=1
            if length == k:
                if mul > maks: 
                    maksSet = True
                    maks = mul
        i+=1
    return maks if maksSet else 0
    
 

T = raw_input().strip().split()[0]
for i in range(int(T)):
    n, k = raw_input().strip().split()
    number = raw_input().strip().split()[0]
    print processNumber(number, int(n), int(k))
