"""
while True:
    my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
    a = 0
    print(len(my_list[0:13]))
    if my_list > 0:
        continue
    print('Положительное число')
        break
"""

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0

while i < len(my_list):
    if my_list[i] > 0:
        print(my_list[i])
    elif my_list[i] < 0:
        break
    i += 1