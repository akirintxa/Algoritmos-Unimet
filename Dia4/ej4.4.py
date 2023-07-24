section_list = [['Pedro', 'Jose', 'Ana', 'Valeria'],
                ['Juan', 'Laura', 'Daniela', 'Federico']]

for section in section_list:
    student_string = ""
    for student in section:
        student_string += ", " + student
    print(f"Los estudiantes de la section son: {student_string}")
