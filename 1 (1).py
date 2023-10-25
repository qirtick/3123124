def get_divisors(numbers):
    result = []
    for number in numbers:
        divisors = []
        for i in range(1, number+1):
            if number % i == 0:
                divisors.append(i)
        result.append(divisors)
    return result

numbers_list = [12, 6, 8, 9]
result = get_divisors(numbers_list)
print(result)