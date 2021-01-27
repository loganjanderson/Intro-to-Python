from functools import reduce

num_list = [1, 2, 3, 4, 5, 6]

def addition(a, b):
    result = a + b
    return result
    
total = reduce(addition, num_list)

num_of_nums = len(num_list)

def division(x, y):
    answer = x / y
    print(answer)

division(total, num_of_nums)
