employee_list = {"Juan": 2500, "María": 3000,
                 "Pedro": 4000, "Ana": 3500, "Luis": 2000}

print(employee_list.get("Luis"))

for key in employee_list:
    print(f"{key} gana {employee_list[key]} al mes")
