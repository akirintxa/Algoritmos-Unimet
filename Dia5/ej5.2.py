import api_management as api
import validators

people_list = api.get_data()
# api.show_people_data(people_list)


index = input("Ingrese el número de usuario: ")

while True:
    if validators.is_number(index):
        index = int(index)
        if validators.int_in_range(index, 0, len(people_list)-1):
            break
    index = input("Ingrese el número de usuario: ")

api.show_person_data(people_list, index)
