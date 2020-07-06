# Uses python3
import sys
import math


def binary_search(a, low, high, x):
    # write your code here
    mid = low + math.floor((high - low) / 2)

    if len(a) == 1:
        if a[0] == x:
            return 0
        else:
            return -1

    elif a[mid] == x:
        return mid

    elif mid == low and a[mid] != x:
        if a[high] == x:
            return high
        else:
            return -1

    elif a[mid] < x:
        low = mid
        return binary_search(a, low, high, x)

    elif a[mid] > x:
        high = mid
        return binary_search(a, low, high, x)


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1: n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, 0, len(a)-1, x), end=' ')
        
    # inputs
    # 5 1 5 8 12 13 5 8 1 23 1 11
    # 5 1 5 8 12 13 1 23
    # 1 1 1 0