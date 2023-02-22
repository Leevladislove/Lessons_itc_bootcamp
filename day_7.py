# file = open('test.txt', 'w')
# text = 'Hello, world!'
# file.write(text)
# file.write('\n')

# for i in range(1, 11):
#     file.write(str(i))
# file.write('\n')
# file.close()


# file = open('test.txt', 'r')
# text = file.read().splitlines()

# for i in text:
#     print(i)

# a = 'day'
# c = 0

# for i in text:
#     if a in i:
#         c += 1
# print(c)


# for i in text:
#     if i.startswith(a):
#         c += 1
# print(c)

# count = 0
# for i in text:
#     if i.index("day"):
#         count += 1
#     else:
#         print('Не найден')
# print(count)


# from os import system

#1
# system('ls / > directories.txt')
# file = open('directories.txt', 'r')
# text = file.read()
# print(text)


#2
# file = open('users.txt', 'a')

# login = input('Enter login: ')
# password = input('Enter password: ')

# file.write(f'login: {login}\npassword: {password}\n')
# print()

# file = open('users.txt', 'r')
# print(file.read())

#3
# text = open('users.txt', 'r')

# char = 'w'
# count = 0

# for i in text:
#     if char in i:
#         print('Yes - in the text is "w"')

#     else:
#         print('No - there is no "w"')

#4
# text = '''Python is a widely used high-level programming language for general-purpose
# programming, created by Guido van Rossum and first released in 1991. An interpreted
# language, Python has a design philosophy that emphasizes code readability (notably
# using whitespace indentation to delimit code blocks rather than curly brackets or
# keywords), and a syntax that allows programmers to express concepts in fewer lines of
# code than might be used in languages such as C++ or Java'''

# file = open('python.txt', 'w')
# file.write(text)

# t_words = []

# file = open('python.txt', 'r')
# list = file.read().split()

# for i in list:
#     if 't' in i or 'T' in i:
#         t_words.append(i)
    
# print(t_words)


# #1
# file = open('users.txt', 'r')
# text = file.read().split()
# print(text)

# login = input('Enter login: ')

# while True:
#     if login in text:
#         print('Логин уже существует, пожалуйста, авторизуйтесь!')  
#         password = input('Enter password: ')
#         break
#     else:
#         password_1 = input('Enter password: ')
#         password_2 = input('Enter again password: ')
#         if password_1 == password_2:
#             file = open('users.txt', 'a')
#             file.write('\n')
#             file.write('\n')
#             file.write(f'login: {login}\npassword: {password_1}')
#             break
#         else:
#             print('Пароль не совпал')


#City game:
print('\nWelcome to the game Cities!')

cities = []

while True:

    print('Select actions:')
    select_actions = '''
        1. Добавьте новый город
        2. Отобразить список
        3. Заменить город
        4. Удалить город
        5. Выход
        '''

    print(select_actions)
    num_actions = int(input('>> '))

    if num_actions == 1:
        enter_city = input('Enter the name of the city: ').title()
        print()

        if enter_city.isdigit() or not enter_city.isalpha():
            print('Enter a correct city name!\n')
        elif enter_city not in cities:
            cities.append(enter_city)
        else:
            print(f'Such a city already exists - {cities.index(enter_city) + 1}.{enter_city}\n')



    if num_actions == 2:
        if len(cities) == 0:
            print('List is empty!\n')
        else:
            print('List of cities:')
            print(', '.join(cities), '\n')
    

    if num_actions == 3:
        if len(cities) == 0:
            print('List is empty!\n')
        else:
            print(f'Current city: {cities[-1]}\n')
            city_replacement = input('New city: ').title()

            if city_replacement in cities:
                print(f'This city already exists - {city_replacement}')
            else:
                cities[-1] = city_replacement
                print('City replaced!\n')


    if num_actions == 4:
        if len(cities) == 0:
            print('List is empty!\n')
        else:    
            del_city = input('Delete city: ').title()
            
            if del_city not in cities:
                print('The city is missing\n')
            else:
                cities.remove(del_city)
                print('City ​​removed\n')


    if num_actions == 5:
        break


