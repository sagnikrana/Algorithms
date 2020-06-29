# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum%10

def get_fibonacci_fast(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
    
    return current

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


def fibonacci_partial_sum_fast(from_, to, occurence):
    sum = 0
    from_num = from_%occurence
    to_num = to%occurence
    for i in range(from_num, to_num+1):
        sum = sum + fib_list[i]
    return sum%10

if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    mod_list = list()
    fib_list = list()
    for i in range(0,63):
        mod_list.append(fibonacci_sum_naive(i))
        fib_list.append(get_fibonacci_fast(i))
        
    occurence = find_pisano_period_occurence(mod_list)

    print(fibonacci_partial_sum_fast(from_, to, occurence))