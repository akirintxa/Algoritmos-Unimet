import requests


def get_data():
    url = 'https://raw.githubusercontent.com/Andresarl16/API-Retos/main/people-api.json'
    response = requests.get(url)
    data = response.json()
    return data


def show_people_data(data_list):
    for people in data_list:
        print(f"""
    El ciudadano {people['first_name']} {people['second_name']} tiene cédula de identidad {people['id']}, 
    es propietario del número de teléfono {people['phone_number']} y cumple años el {people['date_of_birth']}
    """)


def show_person_data(data_list, index):
    person = data_list[index]
    print(f"""
    El ciudadano {person['first_name']} {person['second_name']} tiene cédula de identidad {person['id']}, 
    es propietario del número de teléfono {person['phone_number']} y cumple años el {person['date_of_birth']}
    """)
