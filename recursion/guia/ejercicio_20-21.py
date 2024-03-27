import turtle

def dibujar_hache(x:float, y:float, h:float) -> None:
    # x, y: Centro de la H
    # h: altura/base
    turtle.pu()
    turtle.goto(x-h/2,y-h/2)

    # Lado izquierdo
    turtle.pd()
    turtle.left(90)
    turtle.forward(h)
    # Centro
    turtle.left(180)
    turtle.forward(h/2)
    turtle.left(90)
    turtle.forward(h)
    # Lado derecho
    turtle.left(90)
    turtle.forward(h/2)
    turtle.left(180)
    turtle.forward(h)
    turtle.left(90)
    
    turtle.pu()

def haches(x:float, y:float, h:float, n:int) -> None:
    if n > 0:
        dibujar_hache(x,y,h)
        haches(x - h/2, y + h/2, h/2, n-1)
        haches(x - h/2, y - h/2, h/2, n-1)
        haches(x + h/2, y + h/2, h/2, n-1)
        haches(x + h/2, y - h/2, h/2, n-1)
        
    else:
        dibujar_hache(x,y,h)

# haches(0,0,100,0)

def dibujar_cuadrado(x:float, y:float, b:float) -> None:
    turtle.color("yellow","blue")
    turtle.pu()
    turtle.goto(x - b/2, y - b/2)
    turtle.pd()
    turtle.begin_fill()

    for i in range(0,4):
        turtle.forward(b)
        turtle.left(90)


    turtle.end_fill()
    turtle.pu()

def cuadrados(x:float, y:float, b:float, n:int) -> None:
    if n > 0:
        cuadrados(x - b/2, y - b/2, b/2, n - 1)
        cuadrados(x - b/2, y + b/2, b/2, n - 1)
        cuadrados(x + b/2, y + b/2, b/2, n - 1)
        cuadrados(x + b/2, y - b/2, b/2, n - 1)

        dibujar_cuadrado(x,y,b)
    else:
        dibujar_cuadrado(x,y,b)

#cuadrados(0,0,100,3)
        
def dibujar_rombo(x:float, y:float, h:float) -> None:
    turtle.pu()
    turtle.goto(x - h/2, y)
    turtle.dot()
    turtle.goto(x + h/2, y)
    turtle.dot()
    turtle.goto(x, y + h/2)
    turtle.dot()
    turtle.goto(x, y - h/2)

def rombos(x:float, y:float, h:float, n:int) -> None:
    if n > 0:
        rombos(x - h/2, y, h/4, n - 1)
        rombos(x + h/2, y, h/4, n - 1)
        rombos(x, y - h/2, h/4, n - 1)
        rombos(x, y + h/2, h/4, n - 1)
    else:
        dibujar_rombo(x,y,h)

rombos(0,0,100,4)
        