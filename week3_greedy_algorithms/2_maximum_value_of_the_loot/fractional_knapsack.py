# Uses python3
import sys
import operator

def get_optimal_value(capacity, weights, values):
    capacity_left = capacity
    optimal_value = 0
    per_unit_value = {}
    for index, value in enumerate(values):
        per_unit_value[weights[index]] = value/weights[index]

    # Sorting the dictionary by the value per weight
    per_unit_value = {k: v for k, v in sorted(per_unit_value.items(), key=lambda item: item[1], reverse = True)}

    for weight in per_unit_value.keys():
        if (capacity_left - weight) >= 0:
            optimal_value = optimal_value + (per_unit_value[weight] * weight)
            capacity_left = capacity_left - weight
        else:
            optimal_value = optimal_value + (per_unit_value[weight] * capacity_left)
            capacity_left = capacity_left - capacity_left
            
    return optimal_value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))