# a = []
# while True:
#     if len(a) == 5:
#         break
#     n = int(input('>>'))
#     if n % 2 == 0:
#         a.append(n)
#     else:
#         print('Please, enter even number')

# print(a)

# a = []

# c = True
# while c:
#         n = int(input('>>'))
#         if n % 2 == 0:
#             a.append(n)
#             if len(a) == 5:
#                 c = False
#         else:
#             print("Please< enter even number")

# print(a)

# import os
# import time


# for h in range(60):
#     for m in range(60):
#         for s in range(60):
#             print('{}:{}:{}'.format(h, m, s))
#             time.sleep(1)
#             os.system('clear')



# for i in range(1, 10, 3):
#     for j in range(1, 10):
#         print(f'{i}*{j} = {i * j} \t{i+1}*{j} = {(i+1)*j} \t{i+2}*{j} = {(i+2) * j}')
#     print()


# s = [i for i in range(10)]
# print(s, '\n')

# s = [i for i in range(10) if i % 2 == 0]
# print(s)

# s = ['Sultan', 'Asik', 'Mars', 'Sasha', 'ERJ', \
#      'Alibek', 'Kirill', 'Rustam', 'Janbolat', 'Vlad']

# dict_users = {i:j  for i, j in enumerate(s)}
# print(dict_users)

# #1
# n = int(input('>>'))

# if n == 0:
#     print(n)
# else:

#     factorial = 1
#     while n > 1:
#         factorial *= n
#         n -= 1

#     print(factorial)

#3
# n = int(input('>>'))

# for i in range(1, 10):
#     print(f'{n} * {i} = {n*i}')

#5
# n = int(input('>>'))
# f1 = f2 = 1

# if n == 1:
#     print(n)

# print(f1, f2, end=' ')

# for i in range(2, n):
#     f1, f2 = f2, f1 + f2
#     print(f2, end=' ')

#6
# n = input('>>')
# n1 = ''.join(reversed(n))

# if n == n1: 
#     print('Полиндром')
# else: 
#     print('Не полиндром')

# n = input('>>')
# n1 = n[::-1]

# if n == n1:
#     print('Полиндром')
# else: 
#     print('Не полиндром')
