def print_params (a = 1, b = 'Строка', c = True):
    print(a, b, c)

print_params(1), print_params(2, 2), print_params(3, 'оно', False)
print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = ['Это строка', 45.6, True]
values_dict = {'a': 52, 'b': "Это не int", 'c': False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']

print_params(*values_list_2, 42)