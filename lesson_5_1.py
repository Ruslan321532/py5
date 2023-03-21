# 5. Структуры данных: словари, множества.
# dict - dictionary
# set - множества
# {key: value}

# menu = {
#     'plov': {'carrot', 'rice', 'meat'},
#     'shorpo': {'meat', 'potato', 'water'},
#     'cesar': {'chicken', 'cheese', 'salad'}
# }


# while True:
#     ingrs = input('ingrs: ').lower()
#     for name, ingridients in menu.items():
#         if ingrs in ingridients:
#             print(name)


# word = 'python'
# min_value = 2
#
# while True:
#     input_word = input('enter word: ')
#     if input_word == word:
#         print('ok, ', word)
#
#     elif len(set(input_word).difference(word)) <= min_value:
#         print(f'no "{input_word}" there, maybe you mean, ', word)
#     else:
#         print('no')


# plov = {'carrot', 'rice', 'meat'}
# shorpo = {'meat', 'potato', 'water'}
#
# print(plov.difference(shorpo))
# print(plov - shorpo)
#
# print(plov.union(shorpo))
# print(plov | shorpo)
#
# print(plov.intersection(shorpo))
# print(plov & shorpo)
#
# print(plov.symmetric_difference(shorpo))
# print(plov ^ shorpo)

# print(set('python'))

# lst1 = [1, 2, 3, 2, 4, 1, 3, 5]
# lst2 = {1, 2, 3, 2, 4, 1, 3, 5}
#
# print(lst1)
# print(lst2)
# print(type(lst2))

# 2: 'sdfsdf',
# 4.6: 'sdfs',
# False: 'dfgdfg',
# (1, 2, 3): 'sdfsdf'

# new = dict('python')
# new = dict([[1, 'one'], [2, 'one'], [3, 'three']])
# new = dict(enumerate('python'))
# print(new)
# print(student['name'])
# print(student['hobby'])
# new = dict(name='azamat', age=18, country='KG')
# print(new)

# data = {}
# for i in range(1, 8):
#     data[f'day {i}'] = int(input(f'expense in day {i}: '))

# data = {i: int(input(f'expense in day {i}: ')) for i in range(1, 8)}
# print(data, '\n', sum(data.values()) / len(data))


student = {
    'name': 'Jack',
    'age': 19,
    'height': 2.60,
    'married': False,
    'hobby': ['basketball', 'chess', 'english', 'books'],
    'education': ('school', 'college', 'kyrgyz courses')
}

# for k, v in student.items():
#     print(k, '=>', v)
# for i in student:
#     print(i, ':', student[i])


# print(student.keys())
# print(student.values())
# print(student.items())


# print(student.get('nam', 'нет такого ключа!'))
# print(student['nam'])


'''add'''
# student['surname'] = 'Asanov'
# student.update(new)
#
'''edit'''
# student['married'] = True
# student['age'] += 1
# student['hobby'][0] = 'football'
# student['education'] = list(student['education'])
# student['education'].append('python courses')
# student['education'] = tuple(student['education'])

'''delete'''
deleted = student.pop('married')
print(deleted)
# del student['name'], student['age']


# print(type(student))
