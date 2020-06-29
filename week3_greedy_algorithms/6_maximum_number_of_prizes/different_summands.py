# Uses python3
import sys

def optimal_summands(n):
    summands = []
    #write your code here
    current_num = n
    for summand in range(1, n+1):
        current_num = current_num - summand
        if current_num not in summands and summand not in summands and current_num != summand:
            summands.append(summand)
        else:
            current_num = current_num + summand
        if current_num == 0:
            break
            
            
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')