# python3
global largest_numbers
largest_numbers = []

def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product

def find_largest_number(numbers):
    largest_num = 0
    index_first_largest = 0
    for index, num in enumerate(numbers):
        if num > largest_num:
            largest_num = num
            index_first_largest = index
    largest_numbers.append(largest_num)
    del numbers[index_first_largest]
    return numbers


def max_pairwise_product_fast(numbers):
    if len(numbers) < 2:
        return numbers[0]
    else:
        updated_numbers = find_largest_number(numbers)
        find_largest_number(updated_numbers)
        return largest_numbers[0] * largest_numbers[1]


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_fast(input_numbers))