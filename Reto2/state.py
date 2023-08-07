class State:

    def __init__(self, country, name, capital, population, area):
        self.country = country
        self.name = name
        self.capital = capital
        self.population = population
        self.area = area

    def __str__(self):
        return f"Estado: {self.name}, Capital: {self.capital}, Población: {self.population}, Area (km²): {self.area}, País: {self.country}"

    def print_state_population(self):
        print(f"""
    Estado: {self.name}
    Población: {self.population}
    """)

    def print_state_area(self):
        print(f"""
    Estado: {self.name}
    Area (km²): {self.area}
    """)

    def show_all_states(self, states_data):
        states_list = [
            state for state in states_data
            if state["location_name"].lower() == self.country.lower()]

        return states_list

    def get_states_by_country(self, states_data):
        matching_states = []

        for state in states_data:
            if state["location_name"].lower() == self.country.lower():
                matching_states.append(state)
        # Retornamos la lista de estados que coinciden con el país de la instancia State.
        return matching_states
