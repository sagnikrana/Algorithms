# Uses python3
import sys

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

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
        

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_fast(a, b))