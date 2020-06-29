# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def find_greater_smaller(operation,x,y):
    if operation == 'smaller':
        if x<y:
            return x
        else:
            return y
    elif operation == 'bigger':
        if x>y:
            return x
        else:
            return y
    else:
        return 0

def gcd_fast(a, b):
    if a % b == 0 or b % a == 0:
        return find_greater_smaller('smaller', a, b)
    else:
        while (True):
            big_num = find_greater_smaller('bigger', a, b)
            small_num = find_greater_smaller('smaller', a, b)
            remainder = big_num % small_num
            if remainder == 0:
                return small_num
            elif remainder == 1:
                return 1
            else:
                a = small_num
                b = remainder
            
def lcm_fast(a,b):
    gcd = gcd_fast(a,b)
    if gcd == 1:
        return a*b
    else:
        return int(gcd * (a/gcd) * (b/gcd))
    

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_fast(a, b))