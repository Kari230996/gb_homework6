

'''Третье и четвертое задания'''

import json
from itertools import zip_longest

out_dict = {}


with open('users_hobby.txt', 'w', encoding='utf-8') as file, open('users.csv', encoding='utf-8') as users,\
        open('hobby.csv', encoding='utf-8') as  hobbies:

    num_lines_users = sum(1 for line in users)
    num_lines_hobbies = sum(1 for line in hobbies)

    if num_lines_users < num_lines_hobbies:
        exit(1)

    users.seek(0)
    hobbies.seek(0)

    for user_line, hobby_line in zip_longest(users, hobbies):
        out_dict[user_line.strip()] = hobby_line.strip() if hobby_line is not None else hobby_line

        file.write(f'{user_line.strip()}: {hobby_line.strip() if hobby_line is not None else hobby_line}\n' )# 4 задание



with open('users_hobbies.json', 'w', encoding='utf-8') as json_file:
    json.dump(out_dict, json_file, ensure_ascii=False)
print(out_dict)





