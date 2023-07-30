import random


def generate_ramdom_list(start, end, quantity):
    # Generate 5 random numbers between 10 and 30
    randomlist = random.sample(range(start, end), quantity)
    return randomlist


def sequencial_search(list, value):
    for i in range(0, len(list)):
        if list[i] == value:
            return i
    return -1


def binary_search(list, value, bottom, top):
    if top > bottom:
        mid = (bottom + top) // 2
        if list[mid] == value:
            return mid
        elif value > list[mid]:
            return binary_search(list, value, mid + 1, top)
        else:
            return binary_search(list, value, bottom, mid - 1)
    else:
        if list[top] == value:
            return top
        else:
            return -1


def main():
    number_list = generate_ramdom_list(1, 50, 20)
    number_list.sort()
    # number_list = [111, 222, 333, 444, 555]
    search_value = 40
    print(number_list)

    index1 = sequencial_search(number_list, search_value)
    index2 = binary_search(
        number_list, search_value, 0, len(number_list)-1)
    print("sequencial search:", index1)
    print("binary search:", index2)

    # test = True
    # for i in range(1, 10000):
    # if == -1:
    #     test = False


main()
