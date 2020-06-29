# Uses python3
import sys

global index
index = 0
def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

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
            if mod_list[index+1] == 1 and mod_list[index+2] == 1:
                break
    
    if found_occurence_counter == len(mod_list) - 2:
        return 0
    else:
        return index

def find_occurence(m):
    mod_list = list()
    n = 0
    n1 = 1000
    
    while(True):
        fibonacci_index = [i for i in range(n, n1)]
        mod_list.clear()
        for index in fibonacci_index:
            mod_list.append(get_fibonacci_fast(index)%m)

        if find_pisano_period_occurence(mod_list) == 0:
            n, n1 = n1, n1 + 1000
        else:
            index = n + find_pisano_period_occurence(mod_list)
            return index
        
def get_fibonacci_huge_fast(n, m):
    pisano_period_occurence = find_occurence(m)
    return get_fibonacci_fast(n%pisano_period_occurence)%m

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_fast(n, m))