class Measurement:

    def __init__(self, location_name, temperature, humidity, wind_speed, date):
        self.location_name = location_name
        self.temperature = temperature
        self.humidity = humidity
        self.wind_speed = wind_speed
        self.date = date

    def __str__(self):
        return f"País: {self.location_name}, Temperatura (°C): {self.temperature}, Humedad (%): {self.humidity}, Velocidad del viento (Km/h): {self.wind_speed}, Fecha: {self.date}"
