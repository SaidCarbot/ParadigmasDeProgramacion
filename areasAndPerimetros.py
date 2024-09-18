# 17 de septiembre de 2024
# Ejercicio de Lab1: Programación estructurada parte I
''' Instrucciones: Parte I.
Elabora uno o varios programas que realice al menos 5 fórmulas de perímetros y áreas. 
Los valores introducidos serán en m y tendrán que ser convertidos a cm. '''

import math

def main():
    print("Este es un programa que calcula el área y el perímetro de 5 figuras")

    while True:
        # Menú de opciones
        print("Por favor selecciona el número de la figura con la cual deseas trabajar o 0 para salir:")
        print("1. Círculo")
        print("2. Cuadrado")
        print("3. Rectángulo")
        print("4. Triángulo")
        print("5. Semicírculo")
        print("0. Salir")
        
        figura = int(input())

        if figura == 0:
            print("Saliendo del programa...")
            break

        if figura == 1:  # Círculo
            radioMetros = float(input("Ingresa el radio del círculo en metros: "))
            radioCm = radioMetros * 100  # Convertir a cm
            areaCirculo = math.pi * math.pow(radioCm, 2)
            perimetroCirculo = 2 * math.pi * radioCm
            print(f"El área del círculo es: {areaCirculo:.2f} cm^2")
            print(f"El perímetro del círculo es: {perimetroCirculo:.2f} cm")

        elif figura == 2:  # Cuadrado
            ladoMetros = float(input("Ingresa el lado del cuadrado en metros: "))
            ladoCm = ladoMetros * 100  # Convertir a cm
            areaCuadrado = math.pow(ladoCm, 2)
            perimetroCuadrado = 4 * ladoCm
            print(f"El área del cuadrado es: {areaCuadrado:.2f} cm^2")
            print(f"El perímetro del cuadrado es: {perimetroCuadrado:.2f} cm")

        elif figura == 3:  # Rectángulo
            baseMetros = float(input("Ingresa la base del rectángulo en metros: "))
            alturaMetros = float(input("Ingresa la altura del rectángulo en metros: "))
            baseCm = baseMetros * 100  # Convertir a cm
            alturaCm = alturaMetros * 100  # Convertir a cm
            areaRectangulo = baseCm * alturaCm
            perimetroRectangulo = 2 * (baseCm + alturaCm)
            print(f"El área del rectángulo es: {areaRectangulo:.2f} cm^2")
            print(f"El perímetro del rectángulo es: {perimetroRectangulo:.2f} cm")

        elif figura == 4:  # Triángulo
            baseTrianguloMetros = float(input("Ingresa la base del triángulo en metros: "))
            alturaTrianguloMetros = float(input("Ingresa la altura del triángulo en metros: "))
            baseTrianguloCm = baseTrianguloMetros * 100  # Convertir a cm
            alturaTrianguloCm = alturaTrianguloMetros * 100  # Convertir a cm
            areaTriangulo = (baseTrianguloCm * alturaTrianguloCm) / 2
            print(f"El área del triángulo es: {areaTriangulo:.2f} cm^2")
            # El perímetro depende de si es equilátero o no, podrías pedir más datos.

        elif figura == 5:  # Semicírculo
            halfradioMetros = float(input("Ingresa el radio del semicírculo en metros: "))
            halfradioCm = halfradioMetros * 100  # Convertir a cm
            halfareaCirculo = (math.pi * math.pow(halfradioCm, 2)) / 2
            halfperimetroCirculo = math.pi * halfradioCm + 2 * halfradioCm
            print(f"El área del semicírculo es: {halfareaCirculo:.2f} cm^2")
            print(f"El perímetro del semicírculo es: {halfperimetroCirculo:.2f} cm")

        else:# la condición del else es mas sencilla, pues todo lo qu eno sea lo de arriba es falso
            print("Opción inválida, por favor intenta nuevamente.")

if __name__ == "__main__":# Esta es la parte que más cambia
    main()
# Por Said Carbot y Elian, ESCOM-IPN-MEX