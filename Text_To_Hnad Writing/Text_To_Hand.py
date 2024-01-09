import pywhatkit as pw
file = open('new_file.txt', 'r')
new_file = file.read()

pw.text_to_handwriting(new_file, "Green_color.png", rgb=(0, 122, 0))

print(new_file)
print("Done")

# from array import *
# nums = [-1, 0, 1, 2, -1, 4]
#
# for i in range(len(nums)):
#     for j in range(len(nums)):
#         for k in range(len(nums)):
#             if nums[i]+nums[j]+nums[k] == 0:
#                 print([nums[i], nums[j], nums[k]])
#     break



