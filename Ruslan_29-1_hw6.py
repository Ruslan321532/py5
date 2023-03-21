# # 3
# print("Ноль в качестве знака операции"
#       "\nзавершит работу программы")
# while True:
#     s = input("Знак (+,-,*,/): ")
#     if s == '0':
#         break
#     if s in ('+', '-', '*', '/'):
#         x = float(input("x="))
#         y = float(input("y="))
#         if s == '+':
#             print("%.2f" % (x+y))
#         elif s == '-':
#             print("%.2f" % (x-y))
#         elif s == '*':
#             print("%.2f" % (x*y))
#         elif s == '/':
#             if y != 0:
#                 print("%.2f" % (x/y))
#             else:
#                 print("Деление на ноль")
#     else:
#         print("Неверный знак операции!")
# slovo = str(input())
# a = slovo[::-1]
# if slovo == a:
#     print("yes")
# else:
#     print("no")

# 2
# string = input('Введите слово: ')
# string_reversed = reversed(string)
# if "TRUE" == "".join(set(["TRUE" if i == j else "FALSE" for i, j in zip(string, string_reversed)])):
#     print("TRUE")
# else:
#     print("FALSE")

# /////////////////////////////////////////e////////eeee////
def multiply_numbers(*args):
    product = 1
    for num in args:
        product *= num
    return product


result = multiply_numbers(4, 30, 9, 18)
print(result)