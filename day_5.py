# a = [10, 12, 11]
# b = [12]
# c = [11, 12, 13]

# ls = []
# a = (*a, *b, *c)

# ls.append(a)
# print(ls)

# s = {1, 12, 3}
# s.discard(122)

# print(s)

# #Problem 0:
# dates_of_birth = {3,10,11,7,31,21,1,10,3,5,6,6}
# dates_of_birth.remove(7)
# print(dates_of_birth)

# #Problem 1:
# farm_1 = {"dog", "cat", "mouse", "sheep"}
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}

# print(farm_1.intersection(farm_2))

# #Problem 2:
# farm_1 = {"dog", "cat", "mouse", "sheep"}
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}

# print(farm_2.difference(farm_1))

# #Problem 3:
# s = {1, 2, 3, 4, 5}
# s.add(12)
# s.pop()
# print(s)



# #Problem 000:
# menu = {'lagman': 120, 'plov': '120', 'borsh': 100}

# menu.update({'besh_barmak' : 130})
# menu['lagman'] = 135
# menu.pop('borsh')

# print(menu)

# #Problem 10:
# menu = {'lagman': 120, 'plov': '120', 'borsh': 100}

# menu.update({'drinks' : ['Coca-Cola', 'Sprite', 'Fanta']})
# print(menu)

# #Problem 020:
# s = {'add()', 'pop()', 'difference()'}
# d = {'pop()', 'clear()'}

# print(s.intersection(d))

# #Problem 31:
# d = {
#     input('name: ') : input('pass: '),
#     input('name: ') : input('pass: '),
# }

# print(d)

# #Problem 27:
# name_prof = {
#     'Vlad': 'developer',
#     'Alex': 'designer',
#     'John': 'QA'
# }

# for i, j in name_prof.items():
#     print(f'Hello, {i}. Прекрасная профессия - {j}!')

#Problem 22:
# s = set()
# for i in range(0, 2):
#     num = int(input('Enter num: '))
#     s.add(num)
# print(tuple(s))


# #Problem 11:
# south_american_countries = [    
#                                 'Argentina', 
#                                 'Bolivia',
#                                 'Brazil',
#                                 'Chile',
#                                 'Colombia',
#                                 'Ecuador',
#                                 'Guyana',
#                                 'Paraguay',
#                                 'Peru',
#                                 'Suriname',
#                                 'Suriname'
#                             ]

# res_country = list(set(south_american_countries))
# print(res_country)

# #Problem 101:
# suitcase = []
# items = ['зонт', 'ручка', 'шарф', 'перчатки']

# for i in items:
#     suitcase.append(i)

# print(suitcase)
# suitcase.pop(-1)
# print(suitcase)


# #Problem 001:
# farm_1 = {"dog", "cat", "mouse", "sheep"}
# farm_2 = {"cow", "horse", "cat", "dog"}

# res_farm = farm_1.intersection(farm_2)
# print(res_farm)

# #Problem 100:
# farm_1 = {"dog", "cat", "mouse", "sheep"}
# farm_2 = {"cow", "horse", "cat", "dog"}

# res_farm = farm_2.difference(farm_1)
#print(res_farm)
