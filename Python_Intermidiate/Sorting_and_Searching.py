# def swap(a, b, lists):
#     lists[a], lists[b] = lists[b], lists[a]
#
#
# class compute:
#
#     def __init__(self, value_1, value_2):
#         self.value_1 = value_1
#         self.value_2 = value_2
#
#     def __add__(self, other):
#         value_1 = self.value_1 + other.value_1
#         value_2 = self.value_2 + other.value_2
#
#         new = compute(value_1, value_2)
#         return new
#
#     def __sub__(self, other):
#         value_1 = self.value_1 - other.value_1
#         value_2 = self.value_2 - other.value_2
#
#         new = compute(value_1, value_2)
#         return new
#
#     def __mul__(self, other):
#         value_1 = self.value_1 * other.value_1
#         value_2 = self.value_2 * other.value_2
#
#         new = compute(value_1, value_2)
#         return new
#
#     def __truediv__(self, other):
#         value_1 = self.value_1 / other.value_1
#         value_2 = self.value_2 / other.value_2
#
#         new = compute(value_1, value_2)
#         return new
#
#     def __gt__(self, other):
#         value_1 = self.value_1 + self.value_2
#         value_2 = other.value_1 + other.value_2
#         if value_1 > value_2:
#             return True
#         else:
#             return False
#
#     def __lt__(self, other):
#         value_1 = self.value_1 + self.value_2
#         value_2 = other.value_1 + other.value_2
#         if value_1 < value_2:
#             return True
#         else:
#             return False
#
#     def __ge__(self, other):
#         value_1 = self.value_1 + self.value_2
#         value_2 = other.value_1 + other.value_2
#         if value_1 >= value_2:
#             return True
#         else:
#             return False
#
#     def __str__(self):
#         return '{}'.format(str(self.value_1) + ',' + str(self.value_2))
#
#     def __copy__(self):
#         value_1 = self.value_1
#         value_2 = self.value_2
#
#         new = compute(value_1, value_2)
#         return new
#
#     def __index__(self, obj_len, num):
#         value = [self.value_1, self.value_2]
#         for i in range(len(value)):
#             if num == value[i]:
#                 print("Index No.", end=" ")
#                 return i
#
#     def __and__(self, other):
#         if self.value_1 == other.value_1 and self.value_2 == other.value_2:
#             return True
#
#         else:
#             return False
#
#     def __or__(self, other):
#         if self.value_1 == other.value_1 or self.value_2 == other.value_2:
#             return True
#
#         else:
#             return False
#
#     def __del__(self, other):  # Giving Error
#         value_1 = self.value_1
#         value_2 = self.value_2
#
#         if other == value_1:
#             self.value_1 = None
#
#         elif other == value_2:
#             self.value_2 = None
#
# if __name__ == "__main__":
#     s1 = compute(94, 38)
#     s2 = compute(83, 26)
#
#     s3 = s1 + s2
#     s4 = s1 - s2
#     s5 = s3 * s4
#     s6 = s5 / s2
#     print(s3.value_1, s3.value_2)
#     print(s4.value_1, s4.value_2)
#     print(s5.value_1, s5.value_2)
#     print(s6.value_1, s6.value_2, '\n')
#
#     print(s6 > s5)
#     print(s6 < s5)
#     print(s2 >= s3)
#     print(s3 >= s1)
#     print(s1, '\n')
#
#     s7 = s1.__copy__()
#     s7.value_1 = 87
#     print(s1)
#     print(s7, '\n')
#
#     print(s2.__index__(2, 26))
#     print(s1.__or__(s7))
#     print(s1.__and__(s7))
#     # compute.__del__(s1, 38)
#     print(s1)
#
#
# # Object
# class search:
#
#     def __init__(self, *nums):
#         self.nums = nums
#
#     def linear_search(self, number):
#         value = []
#         for i in self.nums:
#             value.append(i)
#
#         count = 0
#
#         for i in range(len(value)):
#             if number == value[i]:
#                 print("Linear Search:", i, end=", ")
#                 break
#             count += 1
#
#         else:
#             print("THE NUMBER IS NOT IN THE LIST!")
#
#         print("Time Laps:", count, "\n")
#
#     # Binary Search
#     def binary_search(self, number):
#         count = 0
#
#         value = []
#         for i in self.nums:
#             value.append(i)
#
#         value.sort()
#         print(value)
#
#         low = 0
#         high = len(value)
#
#         if number in value:
#             while low < high:
#
#                 mid = int((high + low) // 2)
#
#                 if value[mid] == number:
#                     print("Binary Search:", mid, end=", ")
#                     break
#
#                 elif value[mid] > number:
#                     high = mid
#
#                 elif value[mid] < number:
#                     low = mid
#
#                 count += 1
#
#         else:
#             print("THE NUMBER IS NOT IN THE LIST")
#
#         print("Time Laps:", count)
#
#
# num = search(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
#
# num.binary_search(7)
# num.linear_search(7)
#
#
# # Bubble Sort.
# def bubble_sort(lists):
#     print("Bubble Sort:")
#     print(lists)
#     count = 0
#
#     for i in range(len(lists) - 1, 0, -1):
#
#         c = 1
#
#         for j in range(i):
#
#             if lists[j] > lists[c]:
#                 lists[j], lists[c] = lists[c], lists[j]
#                 c += 1
#
#             elif lists[j] < lists[c]:
#                 c += 1
#                 continue
#
#             count += 1
#
#             print(lists, count)
#
#     print("\n", end="")
#
#
# num = [5, 9, 3, 6, 1, 4, 8, 65, 93, 10, 37, 37, 25, 48]
# bubble_sort(num)
#
#
# # By Telus-ko
# def bubble_sort_2(lists):
#     print("Bubble Sort 2:")
#     count = 0
#
#     for i in range(len(lists) - 1, 0, -1):
#         for j in range(i):
#
#             if lists[j] > lists[j + 1]:
#                 lists[j], lists[j + 1] = lists[j + 1], lists[j]
#
#             count += 1
#
#             print(lists, count)
#
#     print("\n", end="")
#
#
# num = [5, 9, 3, 6, 1, 4, 8, 65, 93, 10, 37, 37, 25, 48]
# bubble_sort_2(num)
#
#
# def selection_sort(lists):
#     count = 0
#     print("Selection Sort:")
#     for i in range(len(lists) - 1, 0, -1):
#         max_val = i
#
#         for j in range(i):
#             if lists[max_val] < lists[j]:
#                 max_val = j
#
#             count += 1
#             print(lists, count)
#
#         lists[max_val], lists[i] = lists[i], lists[max_val]
#
#
# num = [5, 9, 3, 6, 1, 4, 8]
# selection_sort(num)
#
#
# # Quick Sort
# # Method 1.
# def quick_sort(lists):
#     if len(lists) <= 1:
#         return lists
#     else:
#         pivot = lists.pop(0)
#
#     lower = []
#     greater = []
#
#     for i in lists:
#         if pivot > i:
#             lower.append(i)
#         else:
#             greater.append(i)
#
#     return quick_sort(lower) + [pivot] + quick_sort(greater)
#
#
# num = [5, 9, 3, 6, 1, 83, 84, 9302, 4, 8]
# num = quick_sort(num)
# print("Quick Sort: ", num)
#
#
# # Method 2
# def partition(lists, start, end):
#     if len(lists) <= 1:
#         return lists
#     else:
#         pivot = start
#
#     while start < end:
#
#         while start < len(lists) and lists[start] <= lists[pivot]:  # To increase the value of start
#             start += 1                                              # till start became greater than pivot.
#
#         while lists[end] > lists[pivot]:  # To decrease the value of end till the end become less than pivot.
#             end -= 1
#
#         if start < end:
#             swap(start, end, lists)  # Swapping start and end value.
#
#     swap(end, pivot, lists)  # swapping the end value with pivot.
#
#     return end  # to get the pivot value for dividing the partitions
#
#
# def quick_sort(lists, start, end):
#     if start < end:  # For how many times we want to use the recursion.
#         pi = partition(lists, start, end)  # putting the value of the pivot.
#         quick_sort(lists, start, pi-1)  # Left Partition
#         quick_sort(lists, pi+1, end)    # Right Partition
#
#
# # Method 3
# def partition(lists, low, high):
#     if len(lists) <= 1:
#         return lists
#
#     else:
#
#         pivot = lists[high]
#
#     store = -1
#
#     for i in range(high):
#         if lists[i] < pivot:
#             store += 1
#             swap(store, i, lists)
#
#     store += 1
#     swap(store, high, lists)
#
#     return store
#
#
# def quick_sort(lists, low, high):
#     if low < high:
#         pi = partition(lists, low, high)
#         quick_sort(lists, low, pi-1)
#         quick_sort(lists, pi+1, high)
#
#
# if __name__ == "__main__":
#     num = [6, 3, 8, 9, 2, 1, 4]
#     quick_sort(num, 0, len(num)-1)
#     print("Quick Sort:", num)
