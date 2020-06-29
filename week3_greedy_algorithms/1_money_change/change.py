# Uses python3
import sys

def get_change(m):
    #write your code here
    total_changes = 0
    change_list = [10,5,1]
    for change in change_list:
        quot = m//change
        if quot == 0:
            continue
        else:
            total_changes = total_changes + quot
            m = m - (change * quot)
    return total_changes

if __name__ == '__main__':
    m = int(sys.stdin.read())
#     m = int(input())
    print(get_change(m))