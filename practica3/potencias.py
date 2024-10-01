#Potencia mas proxima
def potencia_de_2(n):
    potencia=1  # Iniciamos con 2^0 que es 1
    while potencia*2<=n:  # Seguimos multiplicando por 2 hasta que sea mayor que n
        potencia*=2
    return potencia


num=int(input("Ingrese un número positivo: "))

if num<=0:
    print("El número debe ser positivo.")
else:
    r=potencia_de_2(num)
    print(f"La potencia de 2 más cercana y menor o igual a {num} es: {r}")
