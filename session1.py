# def is_ascending(items):
#     for i in range(len(items) - 1):
#         if items[i] >= items[i+1]:
#             return False

#     return True


# seq1= [1,2,3,4,5,6]
# seq2 = [1,2,0,4]
# print(is_ascending(seq1))
# print(is_ascending(seq2))

# def get_all_digits(number):
#     while number:
#         print(number % 10, end=" ")
#         number //= 10


# get_all_digits(3456789)


def get_all_digits(number):
    number = str(number)
    # TODO   حلقه برعکس
