import turtle
import random

''' Crear pestaña y modificarla '''
s = turtle.Screen()
s.title("Carrera de Tortugas")

''' Crear linea de salida '''
lineaSalida = turtle.Turtle()
lineaSalida.hideturtle()

lineaSalida.penup()
lineaSalida.goto(-300,300)
lineaSalida.right(90)
lineaSalida.pensize(9)

for i in range(23):
    lineaSalida.pendown()
    lineaSalida.fd(10)
    lineaSalida.penup()
    lineaSalida.fd(15)

lineaSalida.goto(-310,300)

for i in range(23):
    lineaSalida.fd(15)
    lineaSalida.pendown()
    lineaSalida.fd(10)
    lineaSalida.penup()
    
lineaSalida.goto(-320,300)

for i in range(23):
    lineaSalida.pendown()
    lineaSalida.fd(10)
    lineaSalida.penup()
    lineaSalida.fd(15)
    
lineaSalida.goto(-330,300)
    
for i in range(23):
    lineaSalida.fd(15)
    lineaSalida.pendown()
    lineaSalida.fd(10)
    lineaSalida.penup()
    
''' Crear jugadores y modificarlos'''
player1 = turtle.Turtle()
player2 = turtle.Turtle()

player1.hideturtle()
player1.shape("turtle")
player1.color("green", "green")
player1.shapesize(2)
player1.pensize(4)

player2.hideturtle()
player2.shape("turtle")
player2.color("blue", "blue")
player2.shapesize(2)
player2.pensize(4)

''' Crear meta '''
player1.penup()
player1.goto(250,170)
player1.pendown()
player1.circle(40)

player1.penup()
player1.goto(-250,205)
player1.showturtle()

player2.penup()
player2.goto(250,-170)
player2.pendown()
player2.circle(40)

player2.penup()
player2.goto(-250,-140)
player2.showturtle()

dado = [1,2,3,4,5,6]

''' Movimientos de la carrera '''
for i in range(20):
    if player1.pos() >= (185,170):
        print('La Torutuga Verde ha ganado')
        break
    elif player2.pos() >= (185,-170):
        print('La Torutuga Azul ha ganado')
        break
    else:
        turno1 = input("Presiona la tecla enter para avanzar la tortuga verde: ")
        turno1 = random.choice(dado) # random.choice va elejir una opcion dada la lista que le pasemos
        print('Avanzas: {} espacios'.format(turno1))
        player1.pendown()
        player1.fd(20*turno1)
        
        turno2 = input("Presiona la tecla enter para avanzar la tortuga azul: ")
        turno2 = random.choice(dado) # random.choice va elejir una opcion dada la lista que le pasemos
        print('Avanzas: {} espacios'.format(turno2))
        player2.pendown()
        player2.fd(20*turno2)
        
turtle.done()