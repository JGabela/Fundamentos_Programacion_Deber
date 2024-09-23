print("Convertidor de unidades de temperatura")
print('')

unidadOrigen = input("Ingrese una unidad de temperatura: ")
unidadMeta = input("Ingrese a que unidad quiere cambiar: ")
temp = input("Ingrese la temperatura que quiere cambiar: ")

try:
    temp = int(temp)
except:
    print("la temperatura que quiere cambiar no es valida")

#Celsius a Fahrenheit
if unidadOrigen == "Celsius" and unidadMeta == "Fahrenheit":
    temp = (1.8 * temp) + 32
    print("Su temperatura es", temp, "°F")

#Kelvin a Fahrenheit
if unidadOrigen == "Kelvin" and unidadMeta == "Fahrenheit":
    temp = (1.8 * (temp -   273)) + 32
    print("Su temperatura es", temp, "°F")

#Fahrenheit a Celsius
if unidadOrigen == "Fahrenheit" and unidadMeta == "Celsius":
    temp = 0.555555 * (temp - 32)
    print("Su temperatura es", temp, "°C")

#Celsius a Kelvin
if unidadOrigen == "Celsius" and unidadMeta == "Kelvin":
    temp = temp + 273
    print("Su temperatura es", temp, "K")

#Kelvin a Celsius
if unidadOrigen == "Kelvin" and unidadMeta == "Celsius":
    temp = temp - 273
    print("Su temperatura es", temp, "°C")

#Fahrenheit a Kelvin
if unidadOrigen == "Fahrenheit" and unidadMeta == "Kelvin":
    temp = (0.555555 * (temp - 32)) + 273
    print("Su temperatura es", temp, "K")
