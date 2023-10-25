import random

def get_random_color():
    colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'pink']
    return random.choice(colors)

random_color = get_random_color()
print(random_color)