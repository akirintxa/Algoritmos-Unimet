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
    number_list = [110, 222, 333, 444, 555]
    index = sequencial_search(number_list, 333)
    print("sequencial search:", index)
    print("binary search:", index)


main()
