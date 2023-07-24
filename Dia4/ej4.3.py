number_list = [1, 2, 3, 4, 5]
number_dict = {}
par = True

for number in number_list:
    if number % 2 == 0:
        number_dict[number] = "par"
    else:
        number_dict[number] = "impar"

print(number_dict)

for i in number_dict:
    print(f"El número {i} es {number_dict[i]}")
