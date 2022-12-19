# Реализуйте алгоритм перемешивания списка.

n = int(input('Введите количество элементов списка: \n'))
new_list = []
from random import randint
for i in range(1, n + 1):    
    new_list.append(randint(1,100))
print(new_list)
import random
random.shuffle(new_list)
print(new_list)
