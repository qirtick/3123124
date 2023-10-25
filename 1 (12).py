string = '12,34,56'

numbers = string.split(',')
sum_of_numbers = sum([int(num) for num in numbers])

print("Сумма чисел:", sum_of_numbers)