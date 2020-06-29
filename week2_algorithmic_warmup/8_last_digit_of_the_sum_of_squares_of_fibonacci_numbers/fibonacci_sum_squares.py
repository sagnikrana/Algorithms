# Uses python3
import sys

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10

def find_pisano_period_occurence(mod_list):
    found_occurence_counter = 0
    for index in range(2,len(mod_list)):
        found_occurence_counter = found_occurence_counter + 1
        if mod_list[index] == 0:
            if mod_list[index+1] == 1 and mod_list[index+2] == 2:
                break
    
    if found_occurence_counter == len(mod_list) - 2:
        return 0
    else:
        return index

def fibonacci_sum_fast(n, occurence, mod_list):
    return mod_list[n%occurence]

if __name__ == '__main__':
    n = int(sys.stdin.read())
    mod_list = list()
    for i in range(0,63):
        mod_list.append(fibonacci_sum_squares_naive(i))
    occurence = find_pisano_period_occurence(mod_list)
    print(fibonacci_sum_fast(n, occurence, mod_list))