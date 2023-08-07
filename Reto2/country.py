class Country:

    def __init__(self, name, capital, population, area, currency, language):
        self.name = name
        self.capital = capital
        self.population = population
        self.area = area
        self.currency = currency
        self.language = language

    def __str__(self):
        return f"País: {self.name}, Capital: {self.capital}, Población: {self.population}, Area (km²): {self.area}, Moneda: {self.currency}, Idioma: {self.language}"

    def print_country_info(self):
        print(f"""
    País: {self.name}
    Capital: {self.capital}
    Población: {self.population}
    Area (km²): {self.area}
    Moneda: {self.currency}
    Idioma: {self.language}
    """)
