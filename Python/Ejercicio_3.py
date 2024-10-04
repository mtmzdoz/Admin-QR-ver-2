'''
3 Un robot ha sido diseñado para moverse a lo largo de una cuadrícula,
recibiendo como entrada alguna de las letras N, S, E, O, que le ordenan moverse
un metro hacia el norte, sur, este, oeste, respectivamente.

La letra F le pone fin al movimiento del robot. Escriba un programa que simule el movimiento el robot,
leyendo letras ingresadas una por una. Al finalizar el movimiento, debe imprimir la distancia recorrida  y la posición final (x,y)

Movimiento:N
Movimiento:E
Movimiento:E
Movimiento:E
Movimiento:S
Movimiento:S
Movimiento:O
Movimiento:O
Movimiento:F
Distancia recorrida: 8 mts
Posición: x= 1 , y= -1
'''
#Ny+
#Sy-
#Ox-
#Ex+

#Posición inicial
x=0
y=0
#Bandera
continuar=True
#distancia
d=0
while continuar:
    movimiento=input("Ingrese el movimiento: ")
    if movimiento!="F":
        if movimiento=="N":
            d+=1
            y+=1
        elif movimiento=="S":
            d+=1
            y-=1
        elif movimiento=="O":
            d+=1
            x-=1
        elif movimiento=="E":
            d+=1
            x+=1
    else:
        continuar=False
print("Distancia recorrida: ",d, " mts")
print("Posición: x=",x, " y=",y)


