dias = float(input('Escriba la cantidad de días: '))

horas = dias * 24

minutos = horas * 60

segundos = minutos * 60

miliseg = segundos * 1000

print (f"""
{dias} días son {horas} horas
{dias} días son {minutos} minutos
{dias} días son {segundos} segundos
{dias} días son {miliseg} milisegundos

       """)