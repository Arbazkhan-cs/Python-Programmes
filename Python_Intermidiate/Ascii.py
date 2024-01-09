import random as r
#
# while True:
#     try:
#         nums = r.randrange(32, 78894, 1)  # Last Range Of The Chr() = 78894
#         print(chr(nums), nums)
#     except:
#         continue
#
#     ask = input("If Done Enter done: ")
#     if ask == 'done':
#         print("Thanks")
#         break
#     else:
#         continue

num = 31

while num <= 78894:
    num += 1
    try:
        print(chr(num), num)
    except:
        continue
