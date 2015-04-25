result = [1]
number = 1
for i in range(1, 10001):
    number = number * 2
    result.append(sum(map(lambda x: int(x), str(number))))

T = int(raw_input())
for _ in range(T):
    test = int(raw_input())
    print result[test]
