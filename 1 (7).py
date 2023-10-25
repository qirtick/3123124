def find_max_min(numbers):
    if numbers:
        return {
            'max': max(numbers),
            'min': min(numbers)
        }
    else:
        return {}

numbers_list = [1, 4, 9, 2, 7]
result = find_max_min(numbers_list)
print(result)