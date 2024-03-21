import turtle
import math

def dibujar_triangulo(x, y, b):
    # Base = Altura * 2
    turtle.pu()
    turtle.goto(x,y)
    turtle.pd()

    # Base (hipotenusa)
    turtle.forward(b)
    turtle.left(135)
    # Cateto derecho
    turtle.forward(math.sqrt(2*pow(b/2,2)))
    turtle.left(90)
    # Cateto izquierdo
    turtle.forward(math.sqrt(2*pow(b/2,2)))
    turtle.left(135)
    
    turtle.pu()

def sierpinsky(x, y, b, n):
    # x, y: posicion absoluta
    # b: longitud de la base del triangulo
    # n: nivel del triangulo

    if (n > 0):
        # Triangulo inferior izquierdo
        sierpinsky(x, y, b/2, n-1)
        # Triangulo inferior derecho
        sierpinsky(x + b/2, y, b/2, n-1)
        # Triangulo superior
        sierpinsky(x + b/4, y + b/4, b/2, n-1)
    else:
        dibujar_triangulo(x,y,b)

#sierpinsky(-250,0,500,4)

def curvas(longitud, n:int):
    if n == 0:
        turtle.forward(longitud)
    else:
        longitud /= 3.0
        curvas(longitud, n-1)
        turtle.left(60)
        curvas(longitud, n-1)
        turtle.right(120)
        curvas(longitud, n-1)
        turtle.left(60)
        curvas(longitud, n-1)

curvas(200,3)