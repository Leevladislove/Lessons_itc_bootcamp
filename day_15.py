# def into(*args):
#     for i in args:
#         if i % 2 == 0:
#             print(i)

# into(1, 2, 3, 4)


# def avg(**kwarg):
#     for i in kwarg.values():
#         print(i)

# avg(name = 'Vlad', age = 28, lang = 'python')

# a = (1, 2, 3, 4, 5)
# print(a)
# print(*a)


# def avg(*args):
#     print(args[0])

# avg(a)
# avg(*a)

# data = {'name':'Vlad', 'age' : 28, 'lang' : 'python'}

# def avg(**kwarg):
#     for i in kwarg.values():
#         print(i)

# avg(**data)



#task 1:
# def add(a: int, b: int) -> int:
#     return a + b

# def substract(a: int, b: int) -> int:
#     return a - b

# def multiply(a: int, b: int) -> int:
#     return a * b

# def divide(a: int, b: int) -> int:
#     if b == 0:
#         return 'на 0 делить нельзя'
#     return a / b

# a = 12
# b = 22

# print(add(a, b))
# print(substract(a, b))
# print(multiply(a, b))
# print(divide(a, b))


#task 2:
# def length_string(string: str) -> str:

#     count = 0
#     for i in string:
#         count += 1

#     return f'Кол-во символов в слове {string}: {count}'

# print(length_string(string = 'hello world!'))


#task 3:
# def change_dict(dict1: dict, dict2: dict) -> dict:
#     dict1.update(dict2)
#     return dict1

# dict1 = {'Alex': 30}
# dict2 = {'Vlad': 28}

# print(change_dict(dict1, dict2))


#task 4:
# def get_eat(eat: str, drink: str):
   
#     file = open('/home/lee/Desktop/menu.txt', 'a')
#     file.write(f'Блюдо: {eat}')
#     file.write('\n')
#     file.write(f'Напиток: {drink}')
#     file.write('\n')

# eat = input('>> ')
# drink = input('>> ')

# get_eat(eat, drink)


#task 5:
# def get_word_to_file(name_text: str):

#     file = open(name_text, 'a')

# name_text = input('>> ')
# get_word_to_file(name_text)


#task 6:
# def main():
#     print('main() - Я главная функция')

#     def secondary():
#         print('secondary() - Я второстепенная функция')

#     secondary()

# main()


#task 7:
# def get_dictionary(dictionary: dict) -> str:
    
#     t1 = []
#     t2 = []

#     for key, val in dictionary.items():
#         t1.append(key)
#         t2.append(val)
    
#     return f'Ключи: {tuple(t1)}, Значение: {tuple(t2)}'

# dictionary = {'Alex': 30, 'Vlad': 28, 'David': 40}
# print(get_dictionary(dictionary))


#task 8:
# def identify_simple_numbers(num: str) -> list:

#     simple_num_ls = []

#     for a in range(2, num + 1):
#         for i in range(2, a):
#             if a % i == 0:
#                 break
#         else:
#             simple_num_ls.append(a)

#     return simple_num_ls

# num = int(input('>> '))
# print(identify_simple_numbers(num))


#task 9:
# def return_list_values(val1, val2) -> list:
    
#     ls = []
#     ls.append(val1), ls.append(val2)

#     return ls

# print(return_list_values('12', True))


#task 10:
# def print_strings(count_string: int):

#     for _ in range(count_string):
#         print(count_string, end=' ')

# count_string = int(input('>> '))
# print_strings(count_string)


#task 11:
# def get_name_salary(name: str, salary: int = 5000) -> str:
#     return f'{name} - {salary}'

# name = 'Vlad'
# salary = 2000

# print(get_name_salary(name, salary))
# print(get_name_salary(name))


# from random import choice
# from string import digits

# #task 12:
# def generator_list(num: int) -> list:

#     ls = []

#     for _ in range(num):
#         ls.append(choice(digits))
    
#     return ls

# print(generator_list(6))
