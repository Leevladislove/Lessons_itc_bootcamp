#task 1:
# values = ("Razakov 32", 10, 1005, ["tables", "chairs"], 23.00)
# convectr = set()

# ls_bool = []

# for val in values:
#     try:
#         convectr.add(val)
#         ls_bool.append(True)

#     except TypeError:
#         print(f'{val} - unhashable type: "list"')
#         ls_bool.append(False)

# print(convectr)
# print(all(ls_bool))


#task 2:
# num_five = input('>> ').split()
# set_nums = set()

# for i in num_five:
#     set_nums.add(int(i))

# print(min(set_nums))


#task 3:
# python_functions = input('>> ')
# print(eval(python_functions))


#task4:
# while True:
#     sum_credit = int(input('>> '))
#     procent = 3.47

#     if sum_credit < 50000:
#         print('Сумма меньше 50 тыс.')
#     else:
#         print(round(sum_credit * (procent / 100), 2))



#task 1.1
# try:
#     pass

# except(TypeError, IndexError, NameError):
#     pass

#task 2.1:
# try:
#     at = 10
#     in = 15
#     wo = 20

#     for e in range(-at, at):
#         print(wo / e)
#         if at > '5':
#             print("at > 5)

# except  (SyntaxError, NameError, TypeError, ZeroDivisionError)
#         print('Error')


#task 3.1:
# lst = []
# for i in range(10):
#     lst.append(i)

# a = list(reversed(lst))
# sls_obj = slice(0, 8)
# print(a[sls_obj])


#task 4.1
# a = 0
# b = 1
# numbers = []

# while b > a:
#     numbers.append(b)
#     b -= 1

# print(numbers)


#task 1/1:
# dict_ = {'name': 'john', 'last': 12, 12:'age'}

# for key in dict_.keys():
#     try:
#         key + 'abc'
#     except TypeError:
#         print(f'Error: {key} is int')

# print(dict_)

