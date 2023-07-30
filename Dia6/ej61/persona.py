class Persona:

    def __init__(self, name, lastname, age, height, weight):
        self.__name = name  # atributo privado que indica que solo se puede modificar desde la clase
        self.lastname = lastname
        self.age = age
        self.height = height
        self.weight = weight

    def __str__(self):
        return f"El ciudadano {self.getFullname()} tiene {self.age} años"

    def getName(self):
        return self.__name

    def setName(self, new_name):
        self.__name = new_name

    def getFullname(self):
        return f"{self.__name} {self.lastname}"

    def calculate_bmi(self):
        return self.weight / (self.height ** 2)

    def is_adult(self):
        return self.age >= 18
        # if self.age >= 18:
        #     return True
        # else:
        #     return False
