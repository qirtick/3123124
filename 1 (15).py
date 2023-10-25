numbers = [1, 2, 3, 4, 5, 6]

first_half = numbers[:len(numbers)//2]
second_half = numbers[len(numbers)//2:]

sum_first_half = sum(first_half)
sum_second_half = sum(second_half)

result = sum_first_half / sum_second_half
print("Результат деления:", result)