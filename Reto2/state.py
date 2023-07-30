class State:
    def __init__(self, country, name, capital, population, area):
        self.country = country
        self.name = name
        self.capital = capital
        self.population = population
        self.area = area

    def __str__(self):
        return f"Estado: {self.name}, Capital: {self.capital}, Población: {self.population}, Area: {self.area}, País: {self.country}"
