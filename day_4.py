# #Problem 0:
# ls = []
# a = (1, 2, 3)
# b = (4, 5, 6)

# ls.append(a)
# ls.append(b)
# print(f'{ls}\n')

# #Problem 1:
# a = (1, 2, 3)
# print(f'{a[0]}\n{a[1]}\n{a[2]}\n')

# #Problem 2:
# a = True
# b = 10
# c = 'Hello'
# d = 12.5

# ls = []
# ls.append(a)
# ls.append(b)
# ls.append(c)
# ls.append(d)

# print(f'{ls}\n')

# #Problem 3:
# ls = ['Alex', 'John', 'Jack', 'Anton', 'Liza']
# a = ''
# res = 'a, '.join(ls)
# print(f'{res}\n')


# #Problem 4:
# a = [1, 2, 4, 5]
# b = [0, 3, 6]

# a.extend(b)
# print(f'{a}\n')

# #Problem 7:
# ls = []

# name = 'Vlad'
# year = 1994
# lang_prog = 'Python'

# ls.append(name)
# ls.append(year)
# ls.append(lang_prog)

# print(f'{ls}\n')


# #1
# list_1 = []
# list_2 = []

# num = int(input('Enter num: '))
# print('\n')

# if num % 2 == 0:
#     list_1.append(num)
# else:
#     list_2.append(num)


# print(f'{list_1} - list1')
# print(f'{list_2} - list2\n')


# #2
# ls = []
# numb1 = int(input('Enter 1 num: '))
# numb2 = int(input('Enter 2 num: '))
# numb3 = int(input('Enter 3 num: '))

# print('\n')

# ls.append(numb1)
# ls.append(numb2)
# ls.append(numb3)

# ls.sort()
# print(f'{ls[0]} - min\n{ls[-1]} - max\n{(ls[0] + ls[1] + ls[2]) / len(ls)} - arithmetic mean\n')


# #3
# products = [
#   'яблоко', 
#   'груша', 
#   'арбуз',
#   'банан', 
#   'мандарин'
# ]

# print(products)
# ind = int(input('Enter index: '))

# if ind >= len(products):
#     print('Нет такого значения\n')
# else:
#     products.pop(ind)
#     print(f'{products}\n')


#4
points = 0

print('Сколько океанов в мире?')
print('1.Пять  2.Четыре  3.Два\n')
ans = int(input('Enter num answer: '))
print('\n')

if ans == 1:
    points += 1

print('Столица Аргентины?')
print('1.Рим  2.Буэнос-Айрес  3.Париж\n')
ans = int(input('Enter num answer: '))
print('\n')

if ans == 2:
    points += 1

print('Наука о вселенной?')
print('1.Астрология  2.Космология  3.Астрономия\n')
ans = int(input('Enter num answer: '))
print('\n')

if ans == 3:
    points += 1

print(f'{points} - кол-во правильных ответов')
if points >= 3:
    print("Вы прошли тест!\n")
elif points == 1 or points == 2:
    print("Вы провалили тест попробуйте след раз\n")
else:
    print("Вы не от ветили ни на один вопрос\n")

# #5
# ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# numb = int(input('Enter num: '))
# print('\n')

# print(f'{ls[numb::]}\n')


# #6
# a = True
# while a: 

#     print('Авторизация\n')

#     login = input('Введите логин:\n')
#     print('\n')

#     if login == '' or " " in login or '\t' in login:
#         print('Логин пустой или содержит пробелы!\n')

#     elif not login.isdigit() and not login.isalpha():
#         print('Логин +\n')

#         password = input('Введите пароль:\n')
#         password_again = input('Подтвердите пароль:\n')
#         print('\n')

#         if password == password_again:
#             print('Пароль совпал!\n')
#             a = False
#         else:
#             print('Пароль не совпал!')
#     else:
#         print('Логин должен содержать буквы и цифры!')
