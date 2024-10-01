#Pago de un empleado

h=int(input("Ingrese las horas trabajadas: "))
sh=int(input("Ingrese el sueldo por hora: "))
sb=40*sh  # Sueldo base para 40 horas
horas_extra=0
pago_extra=0

# 40 horas o menos
if h<=40:
    sueldo_total=h*sh  # Si trabaja menos o igual a 40 horas, se paga normalmente
    print(f"El sueldo es: {sueldo_total} (sin horas extra)")

# Horas extras, mayores a 40
else:
    horas_extra=h-40  # Horas extras trabajadas
    pago_extra=horas_extra*(sh * 1.5)  # Pago por horas extra al 150%
    sueldo_total=sb+pago_extra  # Sueldo total es sueldo base + pago extra

    print(f"Sueldo base por 40 horas: {sb}")
    print(f"Horas extra trabajadas: {horas_extra}")
    print(f"Pago por horas extra: {pago_extra}")
    print(f"El sueldo total es: {sueldo_total}")
