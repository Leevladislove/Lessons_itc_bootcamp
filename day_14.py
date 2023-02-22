# from random import choice
# from string import ascii_letters, digits
# import os
# import time

# def generate_password(n: int) -> str:
#     return ''.join(choice(ascii_letters + digits) for _ in range(n))

# os.system('clear')
# print('Generating password ...')
# time.sleep(0.3)

# print(generate_password(6))


# def validate_login(login: str) -> bool:
#     for char in login:
#         if char not in ascii_letters+digits:
#             return False

#     if not login.isdigit() and login.isalpha():
#         return True
#     return False

# print(validate_login('Vlad123'))
# print(validate_login('123'))
# print(validate_login('Vlad'))

# from random import choice

# #task 1:
# def calculate_cube(number: int) -> int:
#     return number ** 2

# print(calculate_cube(5))


# #task 2:
# def list_random(ls: List[int]) -> int:
#     return choice(ls)

# print(list_random([1, 2, 3, 4, 5, 6, 7, 12, 13, 14, 10]))


# #task 3:
# def reversed_string(string: str) -> str:
#     return string[::-1]

# print(reversed_string('hello world'))


#task 4:
# def count_list(ls: list) -> int:
#     return sum(ls)

# print(count_list([1, 2, 3]))


# #task 5:
# def polindrome_string(string: str) -> bool:
#     return string == string[::-1]

# print(polindrome_string('assa'))
# print(polindrome_string('assa'))
# print(polindrome_string('Lily'))


#task 6:
# def decimal_to_binary(n):
#     if n >= 1:
#         decimal_to_binary(n//2)
#         print(n%2, end='')

# decimal_to_binary(7)

#task 7:
# def comparison_two_numbers(number1: int, number2: int) -> int:
#     if number1 > number2:
#         return 1
#     elif number1 < number2:
#         return -1
#     else:
#         return 0

# print(comparison_two_numbers(12, 10))


#task 8:
# def count_string(string: str) -> int:
#     res_string = string.split()
#     return len(res_string)

# print(count_string('hello world'))    


#task 9:
# def split_string(string: str) -> list:
#     return string.split()

# print(split_string('hello world'))



#1:
# def turn_half_list(ls: list[str]) -> list[str]:
#     mid = len(ls) // 2
#     fist_party = ls[:mid:]
#     second_party = ls[mid::]

#     return list(reversed(fist_party)) + list(reversed(second_party))

# print(turn_half_list(['12', '11', '10', '9', '19']))


#2:
# def fibbonache(num: int):
#     fib1 = fib2 = 1

#     print(0, fib1, fib2, end=' ')

#     for i in range(2, num):
#         fib1, fib2 = fib2, fib1 + fib2
#         print(fib2, end=' ')

# fibbonache(10)


#3:
# def min_num(a: int, b: int) -> int:
#     return a - b

# def sum_num(a: int, b: int) -> int:
#     return a + b


# def main(a: int, b: int):
#     print(min_num(a, b))
#     print(sum_num(a, b))

# main(12, 14)


#1.1:
# name_file = input('>> ')

# def create_file(name_file: str):
#     open(name_file, 'w')

# cf = create_file(name_file)


# from random import choice
# from string import digits

#2.2:
# def gen_number() -> str:
#     gen_phone = ''

#     for i in range(4, 11):
#         gen_phone += choice(digits)
#         if i == 6:
#             gen_phone += ' '
    
#     return f'0444 {gen_phone}'

# print(gen_number())


# n = input('>> ')
# corrector = {'Камень': ['Kamen', 'K', 'Камень', 'К'], 'Ножницы': ['Nozhnitsy', 'Nojnitsy', 'Nozhnicy', 'Nojnicy', 'N', 'Ножницы', 'Н'], 'Бумага': ['Bumaga', 'B', 'Бумага', 'Б']}

# for key, val in corrector.items():
#     if n in val:
#         pass
