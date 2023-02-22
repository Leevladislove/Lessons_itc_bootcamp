#Problem 0:
string = input('Введите пердложение: ')
len_str = len(string)

left = string[:int(len_str / 2):1]
right = string[int(len_str / 2)::]

print(f'{left.lower()}{right.upper()}\n')

#Problem 1:
a = True
a1 = str(a)
print(a1, ' is str\n')


#Problem 2:
char = input('Введите символ: ')
data = 'Пережевывай непоколебимый эпатаж братьев и сестер'

res_data = data.split(char)
print(res_data, '\n')


#Problem 3:
d = 'Пережевывай непоколебимый эпатаж братьев и сестер'
res = d.replace('е', '3')
print(res, '\n')


#Problem 4:
name = input('Введите имя: ')
age = int(input('Ваш возраст: '))
movie = input('Любимы фильм: ')

print(f'Hello {name.title()}, cool movie is {movie}!\n')


#Problem 5
data = 'Пережевывай непоколебимый эпатаж братьев и сестер'
coun_t = data.split()
print(len(coun_t), '- кол-во слов', '\n')


#Problem 6
data = 'Пережевывай непоколебимый эпатаж братьев и сестер'
print('|'.join(data), '\n')


#Problem 7
data = 'Пережевывай непоколебимый эпатаж братьев и сестер'
print(data.title())
