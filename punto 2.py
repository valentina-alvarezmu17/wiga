from matplotlib import pyplot as plt
import math

#Entrada de variables

x1 =  float(input("Ingrese el valor de X1: "))
y1 = float(input("Ingrese el valor de Y1: "))

x2 = float(input("Ingrese el valor de X2: "))
y2 = float(input("Ingrese el valor de Y2: "))

x3 = float(input("Ingrese el valor de X3: "))
y3 = float(input("Ingrese el valor de Y3: "))

#Dibujo de puntos en el plano
plt.plot(x1,y1, marker="o", color="red")
plt.plot(x2,y2, marker="o", color="blue")
plt.plot(x3,y3, marker="o", color="black")

#Definicion de las coordenadas de X y Y de de nave 
x = (x1 + x2 + x3)/3
y = (y1 + y2 + y3)/3

#Dibujo del punto de la nave
plt.plot(x,y, marker="o", color="magenta")

print("Las coordenadas de la nave serian: ", x , y)

plt.show()