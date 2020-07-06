# Uses python3
import sys

def get_majority_element(a, low, high):
    if low == high or len(a) == 0:
        return 0

    main_dict = {}
    
    for item in a:
        if item in main_dict:
            main_dict[item] = main_dict[item] + 1
            if main_dict[item] > high/2:
                return 1
        else:
            main_dict[item] = 1
    #write your code here
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(get_majority_element(a, 0, n))