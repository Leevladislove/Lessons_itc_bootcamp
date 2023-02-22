#task 1:
while True:
    b = input("""
    Выберите действие
    +
    -
    *
    **
    //
    %
    /
    8: Выключить Калькулятор
    >>> """)

    if b == '8':
        break
    a = int(input('введите цифру:'))
    c = int(input('введите цифру:'))

    if b == '+':
        print('Результат = ',a + c)
    elif b == '-':
        print('Результат = ',a - c)
    elif b == '*':
        print('Результат = ',a * c)
    elif b == '/':
        if c == 0 or a == 0:
            print('нельзя делить на 0')
        else:
            print('Результат = ',a / c)
    elif b == '**':
        print('Результат = ', a ** c)
    elif b == '%':
        print('Результат = ', a % c)
    elif b == '//':
        print ('Результат = ', a // c)
    else:
        print('неверное выбранное действие')


#task 2:
users = [ ]
a=input('Login:')
b=input('Password:')
users.append(f'{a,b}')
print(users)

print('Пожалуйста войдите в свой аккаунт')
c=input('Login:')
d=input('Password:')

if c == a and d == b:
    print('Добро пожаловать')
else:
    print('НЕПРАВИЛЬНЫЙ ЛОГИН ИЛИ ПАРОЛЬ')


#task 2.1
users = [ ]

a = input("Login: ")
b = input("Password: ")
users.append({"login": a, "password": b})
print("Регистрация прошла успешно")

a = input("Login: ")
b = input("Password: ")
for i in users:
    if i["login"] == a and i["password"] == b:
        print("ДОБРО ПОЖАЛОВАТЬ")
        break
else:
    print("НЕПРАВИЛЬНЫЙ ЛОГИН ИЛИ ПАРОЛЬ")


#task 3:
dict1 = {'a': 5, 'b': 3, 'c': 10, 'd': 15, 'e': 20, 'f':30, 'g': 42, 'h': 50}

for i, j in dict1.items():
    if j % 3 == 0:
        print(f'{i} = Hi')
    elif j % 5 == 0:
        print(f'{i} = Bye')


#task 4:
list = []
diapazon = int(input('ot 0 do >>  '))
result = 0
for i in range(diapazon):
    if i % 3 == 0 or i % 5 == 0:
        list.append(i)

for j in range(len(list)):
    result += j

print(result)


#task 5:
n = list(map(int, input('>> ')))
res_num = 0
for i in n:
    res_num += i
print(res_num)


#task 6:
vvod = input('vvedite datu v formate yyyy-mm-dd hh:mm   ')

date, time = vvod.split()
year, month, day = date.split('-')
hour, minute = time.split(':')

dct = {
    'god' : year,
    'mesyac' : month,
    'den' : day,
    'chas' : hour,
    'minuty' : minute
}

print(dct)


#task 7:
words = ['Anna', 'civic', 'kayak', 'Level', 'Madam', 'Mom', 'Noon', 'Racecar', 'Radar', 'еще', 'кабак', 'шалаш', 'лишил','language', 'which', 'means', 'vendor', 'слова', 'фраза', 'введите', 'слово', 'кнопку',]
for i in words:
    if i[::-1] == i:
        print(f'{i} - полиндром')
    else:
        print(f'{i} - не полиндром')


#task 8:
a = input("Введите строку: ")
b = a.split()
c = max(len(word) for word in b)
d = [word for word in b if len(word) == c]
print("Самые длинные слова:", d)


#task 9:
n = int(input('Number: '))
for a in range(2,n + 1 ):
    for i in range(2,a):
        if a % i == 0:
            break
    else:
        print(a)


#task 10:
n = input(">> ").split()
n1 = []
a = set()

for i in n:
    if i not in a and n.count(i) == 1:
        a.add(i)
        n1.append(int(i))

print("Уникальные числа: ", n1)


#task 10.1:
n = input(">> ")
n1 = []
a = set()

for i in n:
    if i in a and i not in n1:
        n1.append(i) 
    else:
        a.add(i)  

print("Уникальные числа: ", n1)


#task 10.2:
lst = input('vvedi stroku  ')
b = []

for i in lst:
    if lst.count(i) > 1 and i not in b:
        b.append(i)
print(b)


#task 11:
a = input('Введите строку:')
b = input('Введите символ:')

c = a.count(b)

print(f"Количество вхождений символа:{b} {c}")


#task 12:
a = int(input("Number1:"))
b = int(input("Number2:"))

c=max(a,b)

while True:
    if c % a == 0 and c % b == 0:
        print(f"Наименьшее общее кратное: {c}")
        break
    c += 1


#task 13:
lst = input('vvedite chisla cherez probel  ').split()
b = []

for i in lst:
    if lst.count(i) == 1:
        b.append(int(i))

print(b)


#task 14:
a = input('Введите строку:')
b = set()

for i in a.lower():
    if i.isalpha() and i.lower() in "abcdefghijklmnopqrstuvwxyz":
        b.add(i)

if len(b) == 26:
    print("Содержит все англиские буквы")
else:
    print("Содержит не все англиские буквы")


#task 15:
a = input('vvodi cherez probel  ')
b = input('vvodi cherez probel  ')

lst1 = a.split()
lst2 = b.split()

lst3 = list(set(lst1).intersection(lst2))
print(lst1)
print(lst2)
print('peresechenie spiskov', lst3)
