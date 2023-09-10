# numbers = [1,2,3]
# n1, n2, n3 = numbers
# print(n1, n2, n3)
# numbers = [1,2,3]*1000

# n1, n2, n3 , *others= numbers
# print(n1, n2, n3)
# print(others)

# n1, *others, nn= numbers
# print(n1, nn)


# colors = ["red", "green", "blue","purple"]

# for color in colors:
#     print(color, end=" ")

# print()

# for i in range(len(colors)):
#     print(colors[i], end=" ")
# print()

# for index,val in enumerate(colors):
#     print(index, val)


# numbers = [3,5,7,8,1]
# numbers.sort(reverse=True)
# print(numbers)


# new_numbers = sorted(numbers, reverse=True)
# print(new_numbers)


# import turtle
# numbers = [1, 2, 3, 1, 1, 1, 2, 2, 1, 1, 1]
#  از لیست بالا عدد یک را حذف نمائید


# items = [("product_one", 100), ("product_two", 30),
#          ("product_three", 250), ("product_four", 130)]

# items[0], items[1] = items[1], items[0]
#  لیست بالا را براساس قیمت مرتب نمایید به صورت صعودی یعنی از کوچک به بزرگ

# def sort_item(item):
#     return item[1]

# items.sort(key=sort_item)
# print(items)

# items.sort(key=lambda item: item[1])
# print(items)


# numbers = [1, 2, 3, 1, 1, 1, 2, 2, 1, 1, 1]
# def mode(numbers):
#     number_count = {}
#     for n in numbers:
#         if n not in number_count:
#             number_count[n] = 0
#         number_count[n] += 1

#     return number_count

# print(mode(numbers))


import matplotlib.pyplot as plt


# list1 = [1, 2, 3, 4]
# list2 = ['one', 'two', 'three', 'four']

# plt.bar(list2, list1)
# plt.xlabel("dice")
# plt.ylabel("count")
# plt.title("Dice experiment")
# plt.show()

import random
counter = {}

for i in range(5):
    face = random.randint(1,6)
    if face not in counter:
        counter[face] = 0
    counter[face] += 1
print(counter)
