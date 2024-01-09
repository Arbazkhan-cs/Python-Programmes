# f = open('F_Copy.txt', 'r')
#
# dic = {}
# count = 0
# x = None
#
# for lines in f:
#     line = lines.strip()
#
#     if not line.startswith('From'):
#         continue
#
#     line = line.split()
#     x = line[1]
#
#     # if x in dic:
#     #     dic[x] = dic[x] + 1
#     # else:
#     #     dic[x] = 1
#     dic[x] = dic.get(x, 0) + 1  # Or we Can use this method except using the above method.
#
#
# c = 0
# for key in dic:
#     if c < dic[key]:
#         c = dic[key]
#         x = key
#
# print(x, c)
