N_MAX = 1001
factorialSum = [1]
factorial = 1
for i in range(1, N_MAX):
    factorial *= i 
    factorialSum.append(sum(map(int, str(factorial))))

T = int(raw_input())

for _ in range(T):
    test = int(raw_input())
    print factorialSum[test]
