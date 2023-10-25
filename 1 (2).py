import random

def fill_list(n, start, end):
    result = []
    previous_number = None
    for _ in range(n):
        number = random.randint(start, end)
        while number == previous_number:
            number = random.randint(start, end)
        result.append(number)
        previous_number = number
    return result

n = 10
start = 1
end = 5
result = fill_list(n, start, end)
print(result)