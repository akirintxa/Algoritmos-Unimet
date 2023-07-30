class Country:

    def __init__(self, name, capital, population, currency, language, states=None):
        self.name = name
        self.capital = capital
        self.population = population
        self.currency = currency
        self.language = language
        self.states = states

    def __str__(self):
        return f"País: {self.name}, Capital: {self.capital}, Población: {self.population}, Moneda: {self.currency}, Idioma: {self.language}"

    def print_country_info(self):
        print(f"""
    País: {self.name}
    Capital: {self.capital}
    Población: {self.population}
    Moneda: {self.currency}
    Idioma: {self.language}
    """)

    def add_state(self, state):
        self.states.append(state)

    def print_states_info(self):
        if not self.states:
            print(f"No hay estados para {self.name}.")
            return

        print(f"Estados de {self.name}:")
        for state in self.states:
            print(state)
