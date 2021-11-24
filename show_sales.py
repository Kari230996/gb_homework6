'''Шестое задание'''

import sys

show_nums = sys.argv[1:]

with open('bakery.csv', encoding='utf-8') as file:

    if len(show_nums) > 1:    # Для два аргумента
        start = int(show_nums[0])
        end = int(show_nums[1])
    elif len(show_nums) == 0:
        start = 0
        end = sum(1 for line in file) # Без аргумента
        file.seek(0)
    else:
        start = int(show_nums[0])
        end = sum(1 for line in file) # для одного аргумента
        file.seek(0)

    for index, line in enumerate(file):
        if start <= index + 1 <= end:
            print(line.strip())




