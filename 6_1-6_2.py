import requests

'''Первое задание'''

# with open('nginx_logs.txt', 'w') as file:
#     response = requests.get('https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs').text
#     print(file.write(response))
#
# with open('nginx_logs.txt') as read_file:
#     list_1 = []
#     for line in read_file:
#         r_file = line.split()
#         text = (r_file[0], r_file[5][1:], r_file[6])
#         list_1.append(text)
#
# print(list_1)

'''Второе задание'''

with open('nginx_logs.txt') as read_file:
    spammer_dict = {}
    list_1 = []
    for line in read_file:
        r_file = line.split()
        text = (r_file[0], r_file[5][1:], r_file[6])
        list_1.append(text)
        spammer_dict.setdefault(r_file[0], 0)
        spammer_dict[r_file[0]] += 1

print(spammer_dict)




















