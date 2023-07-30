def sequencial_search(list, value):
    for i in range(0, len(list)):
        if list[i] == value:
            return i
    return -1


def main():
    number_list = [110, 222, 333, 444, 555]
    index = sequencial_search(number_list, 333)
    print(index)


main()
