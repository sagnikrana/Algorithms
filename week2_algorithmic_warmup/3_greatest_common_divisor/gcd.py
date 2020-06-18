# Uses python3
import sys


def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


def find_greater_smaller(operation, x, y):
    if operation == 'smaller':
        if x < y:
            return x
        else:
            return y
    elif operation == 'bigger':
        if x > y:
            return x
        else:
            return y
    else:
        return 0


def gcd_fast(a, b):
    flag = True
    if a % b == 0 or b % a == 0:
        return find_greater_smaller('smaller', a, b)
    else:
        while (flag):
            a = find_greater_smaller('bigger', a, b)
            b = find_greater_smaller('smaller', a, b)
            remainder = a % b
            if remainder == b:
                return a
            elif remainder == 0:
                return 0
            else:
                b = remainder


if __name__ == "__main__":
    #input = sys.stdin.read()
    input_from_user = input()
    a, b = map(int, input_from_user.split())
    print(gcd_fast(a, b))

