calificacion = input("Ingrese la calificacion: ")

#Verifica que la calificacion ingresada sea un numero valido
try:
    calificacion = int(calificacion)
    if calificacion < 0 or calificacion > 100:
        print("Error")
    if 90 <= calificacion <= 100:
            print("Su calificacion es A")
    if 80 <= calificacion < 90:
        print("Su calificacion es B")
    if 70 <= calificacion < 80:
            print("Su calificacion es C")
    if 60 <= calificacion < 70:
        print("Su calificacion es D")
    if 0 <= calificacion < 60:
            print("Su calificacion es F")
except:
    print("Error, no es una calificacion")
