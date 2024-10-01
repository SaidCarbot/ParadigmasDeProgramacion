#Cuadrantes del plano
def det_cuadrante(x, y):
    if x>0 and y>0:
        return "El punto se encuentra en el Cuadrante I."
    elif x<0 and y>0:
        return "El punto se encuentra en el Cuadrante II."
    elif x<0 and y<0:
        return "El punto se encuentra en el Cuadrante III."
    elif x>0 and y<0:
        return "El punto se encuentra en el Cuadrante IV."
    elif x==0 and y==0:
        return "El punto se encuentra en el origen."
    elif x==0:
        return "El punto se encuentra sobre el eje Y."
    elif y==0:
        return "El punto se encuentra sobre el eje X."

x=int(input("Introduzca el valor de x:"))
y=int(input("Introduzca el valor de y:"))

r= det_cuadrante(x,y)
print(r)
