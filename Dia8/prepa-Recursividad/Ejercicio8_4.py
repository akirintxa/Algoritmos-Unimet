def sum_list(number_list):
    if len(number_list) > 0 :
        number = number_list.pop()
        return number + sum_list(number_list)
    else:
        return 0

def start():
    numbers = [1,2,3,4,5,6,7,8,9,10]
    print(sum(numbers))

    print(sum_list(numbers))

start()