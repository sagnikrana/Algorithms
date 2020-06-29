# python3
import sys

def compute_min_refills(distance, tank, stops):
    # write your code here
    running_tank = tank
    refills = 0
    car_index = 0
    stops.append(distance)
    check_diff = 0
    diff_list = list()
    
    for index, stop in enumerate(stops):
        if index == len(stops) - 1:
            break
        if (stops[index+1] - stop) > tank:
            return -1
    
    for index, stop in enumerate(stops):
        dist_left = running_tank - stop
        if dist_left < 0:
            refills = refills + 1
            running_tank = running_tank  + tank
            
    return refills

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
#     d, m, _, *stops = map(int, input().split())
    print(compute_min_refills(d, m, stops))