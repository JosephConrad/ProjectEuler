import bisect

def next_lower_value(values_list, input_value):
    index= bisect.bisect_left(values_list, input_value)
    if index == 0: # there's not a "next lower value"
        raise NotImplementedError # you must decide what to do here
    else:
        return values_list[index - 1]

def isPalindrome(number):
    n = str(number)
    if len(n) != 6: return False
    for i in range(0, len(n)/2):
        if n[i] != n[-i-1]: return False
    return True


mul = [i*j for i in range(100,1000) for j in range(100,1000) if isPalindrome(i*j)]
mul = sorted(mul)

T = raw_input().strip().split()[0]
for i in range(int(T)):
    n = int(raw_input().strip().split()[0])
    print next_lower_value(mul, n)
