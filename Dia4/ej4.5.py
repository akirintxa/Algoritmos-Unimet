student_list = [{"name": "Pedro", "age": 19, "average": 14.3},
                {"name": "Juan", "age": 21, "average": 17.7},
                {"name": "Andrea", "age": 18, "average": 15.1}]

for student in student_list:
    print(
        f"El estudiante {student['name']} tiene {student['age']} años y su promedio es {student['average']}")
