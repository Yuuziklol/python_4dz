# 1.Вычислить число c заданной точностью d
# Пример:
# при $d = 0.001, π = 3.141

# import math
# def find_number(k):
#     p = math.pi
#     print(p * 10 ** (k+1) //10 / 10**(k))
# d = 3
# find_number(d)

# 2.Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# "20" -> [2, 2, 5]

# def find_ele(k):
#     my_list = []
#     i = 2
#     while i <= k:
#         if k % i == 0:
#             my_list.append(i)
#             k //= i
#             i = 2
#         else:
#             i += 1
#     return my_list
# N = 20
# print(find_ele(N))


# 3.Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]

# def rewrite_list(first_list):
#     second_list = []
#     for i in range(0,len(first_list)):
#         help = 1
#         for k in range(0,len(first_list)):
#             if i != k:
#                 if first_list[i] == first_list[k]:
#                     help += 1
#                     break
#         if help == 1:
#             second_list.append(first_list[i])
#     return second_list
# my_list = [1, 1, 2, 3, 4, 5, 5, 6, 8, 10, 1, 2, 3]
# print(rewrite_list(my_list))

# 4.Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# from random import randint
# def formation(k, dict):
#     a = randint(1, 101)
#     # print('x'+ dict[k] + f' - {a} = 0')
#     f = open('file.txt', 'w')
#     f.write(str(f'x^{k} - {a} = 0'))
# k = 2
# dict_ = {
#     0: "\u2070",
#     1: "\u00B9",
#     2: "\u00B2",
#     3: "\u00B3",
#     4: "\u2074",
#     5: "\u2075",
#     6: "\u2076",
#     7: "\u2077",
#     8: "\u2078",
#     9: "\u2079"
# }
# formation(k, dict_)

# 5.Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# with open('input1.txt','r') as file:
#     poly_1 = file.readline()
#     list_poly_1 = poly_1.split()
# with open('input2.txt','r') as file:
#     poly_2 = file.readline()
#     list_poly_2 = poly_2.split()
# with open('output.txt','w') as file:
#     file.write(f'{list_poly_1} + {list_poly_2}')

