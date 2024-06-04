def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [type, 3, 'число']
values_dict = {'a': 1, 'b': 'строка', 'c': True}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [True, 41]
print_params(*values_list_2, 42)




