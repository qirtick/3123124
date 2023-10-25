import random

def shuffle_list(lst):
    random.shuffle(lst)
    return lst

my_list = [1, 2, 3, 4, 5]
shuffled_list = shuffle_list(my_list)
print(shuffled_list)