#Uses python3

import sys

def max_dot_product(a, b):
    #write your code here
    revenue = 0

    for _ in range(len(a)):
        max_cost = max(a)
        max_click = max(b)
        revenue = revenue + (max_cost * max_click)
        del a[a.index(max_cost)]
        del b[b.index(max_click)]
    return revenue
        

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))