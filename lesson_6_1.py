# функции, аргументы *args, **kwargs
# DRY - don't repeat yourself
# def - definition
# sequence - последовательность

# определение наименование(параметры):
#     тело функции
#     возврат значения
#
# наименование(аргументы) # вызов функции


# students = ['danil', 'aijamal', 'askhat']
#
# def add(name):
#     students.append(name)
#
#
# def delete(name=None, index=None):
#     if name:
#         students.remove(name)
#     else:
#         del students[index]
#
# while True:
#     print(students)
#     command = input('1) add\n'
#                     '2) delete\n'
#                     'else break')
#     if command == '1':
#         add(name=input('enter name: '))
#     elif command == '2':
#         answer = input('1) name or 2) index: ')
#         if answer == '1':
#             delete(name=input('name: '))
#         else:
#             delete(index=int(input(f'index: {list(range(len(students)))}')))
#     else:
#         break

# def menu(**kwargs):
#     return kwargs
#
# monday = menu(eat='sandwich', drink='cola')
# tuesday = menu(eat='pizza', drink='juice', dessert='cake')
# print(monday)
# print(tuesday)


# def sum1(a, b=5, *args):
#     # print(a, b, args)
#     return sum(args)
#
# print(sum1(1, 2, 3, 56, 12, 34, 4, 12, 345, 567))


# word = 'python'
#
# def len1(sequence):
#     count = 0
#     for i in sequence:
#         count += 1
#     return count
#
# print(len1([1, 2, 3, 4, 5, 6, 7]))
# print(len1(list(range(100))))

# print(len(word) + 4)


# number = len(word)
# print(number + 4)


# def greet(name, surname='unknown'):  # обязательный позиционный параметр: 'name'
#     print(f'name: {name}, surname: {surname}')
#
#
# greet("азамат", 'ulanov')
# greet(surname='samatov', name="samat")  # keyword arguments
# greet('bruce')


# greet("kairat")



def get_square(length, width):
    return length * width

print(get_square(
    length=int(input('length: ')),
    width=int(input('width: ')))
    )


# square_2 = get_square(9, 7)
# square_hall = get_square(20, 10)
# print(square_2, square_hall, sep='\n')

# length = 9
# width = 7
# square_2 = length * width
# print(square_2)
#
# length = 20
# width = 10
# square_hall = length * width
# print(square_hall)
