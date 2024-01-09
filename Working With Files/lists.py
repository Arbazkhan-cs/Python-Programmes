# from array import *
#
# num = list()
# f_name = open('file.txt', 'r')
# for lines in f_name:
#     lines = lines.strip()
#     lines_1 = lines.split()
#     for i in range(len(lines_1)):
#         if lines_1[i] not in num:
#             num.append(lines_1[i])
#
# num.sort()
# print(num)
#
# # Opening File and Finding The words which are start from "FROM:".
# f_name = open('First_file', 'r')
# num = []
# count = 0
# for lines in f_name:
#     lines = lines.strip()
#     if lines.startswith('From: '):
#         f_line = lines.split()
#         print(f_line[1])
#         count += 1
#
# print("There were", count, "lines in the file with From as the first word")
#
#
# # Opening File and Finding The words which are start from "FROM:".
# file = open('First_file', 'r')
# count = 0
# for lines in file:
#     lines = lines.strip()
#     if lines.startswith('From: '):
#         file = lines.split()
#         print(file[1])
#         count += 1
# print("There is", count, 'line in this file.')
#
# # Binary Search
# num = array('i', [])
# j = 0
#
# num1 = int(input("Enter the length of the array). "))
# while j < num1:
#     j += 1
#     num.append(j)
# print(num)
#
# value = int(input("Enter the number which you want to find its index no. in the given array!!! "))
#
# low = 0
#
# high = len(num) + 1
#
# while low <= high:
#     x = int((high + low) / 2)
#
#     try:
#         if num[x] == value:
#             print("index no.", x)
#             break
#
#     except IndexError as i:
#         print("the error is index", i)
#         quit()
#
#     if num[x] < value:
#         low = x
#
#     elif num[x] > value:
#         high = x
#
#     print("steps:", x)
#
# print("\U0001F931")
# print("\U0001F928")
# print("\U0001F929")
# print("\U0001F932")
# print("\U0001F970")
