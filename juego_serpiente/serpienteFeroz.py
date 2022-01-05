import turtle
import time
import random
 
#variables marcador
puntuacion = 0
mejor_puntuacion = 0

#ventana
ventana = turtle.Screen()
ventana.title("Serpiente Feroz")
ventana.bgcolor("black")
ventana.setup(width=900, height=600)
ventana.tracer(0)

#cabeza de la serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("#229954")   
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"

#comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(random.randint(-280, 280), random.randint(-280, 280))

#cuerpo
cuerpo = []

#arbustos
for i in range(30):
    arbusto = turtle.Turtle()
    arbusto.speed(0)
    arbusto.shape("square")
    arbusto.color("#82E0AA")
    arbusto.penup()
    arbusto.goto(random.randint(-300, 240), random.randint(-300, 240))

#marcador
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Puntuación: 0              Mejor puntuación: 0", align="center", font=("Arial", 20, "normal"))


#funciones
def arriba():
    cabeza.direction = "up"

def abajo():
    cabeza.direction = "down"

def izquierda():
    cabeza.direction = "left"

def derecha():
    cabeza.direction = "right"

def movimiento():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)
    
    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)
    
    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)
    
    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)


#teclado

ventana.listen()
ventana.onkeypress(arriba, "Up")
ventana.onkeypress(abajo, "Down")
ventana.onkeypress(izquierda, "Left")
ventana.onkeypress(derecha, "Right")

while True:
    ventana.update()

    #colición con paredes
    if cabeza.xcor()>420 or cabeza.xcor()<-420 or cabeza.ycor()>280 or cabeza.ycor()<-280:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction = "stop"

        # esconder segmentos
        for partes in cuerpo:
            partes.goto(1000, 1000)
        
        #limpiar lista
        cuerpo.clear()

        #resetear puntuación
        puntuacion = 0
        texto.clear()
        texto.write("Puntuación: {}         Mejor puntuación: {}".format(puntuacion, mejor_puntuacion), align="center", font=("Arial", 20, "normal"))

    #colición con comida
    if cabeza.distance(comida) < 17:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        comida.goto(x,y)

        #agregar cuerpo
        nuevo_cuerpo = turtle.Turtle()
        nuevo_cuerpo.speed(0)
        nuevo_cuerpo.shape("square")
        nuevo_cuerpo.color("#27AE60")
        nuevo_cuerpo.penup()
        cuerpo.append(nuevo_cuerpo)

        #aumentar puntuación
        puntuacion += 10

        if puntuacion > mejor_puntuacion:
            mejor_puntuacion = puntuacion
        
        texto.clear()
        texto.write("Puntuación: {}     Mejor puntuación: {}".format(puntuacion, mejor_puntuacion), align="center", font=("Arial", 20, "normal"))

    #colición con cuerpo

    for partes in cuerpo:
        if partes.distance(cabeza) < 17:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction = "stop"

            for partes in cuerpo:
                partes.goto(1000, 1000)

            cuerpo.clear()
        
            puntuacion = 0
            texto.clear()
            texto.write("Puntuación: {}     Mejor puntuación: {}".format(puntuacion, mejor_puntuacion), align="center", font=("Arial", 20, "normal"))

    #mover cuerpo
    largo_cuerpo = len(cuerpo)
    for i in range(largo_cuerpo-1, 0, -1):
        x = cuerpo[i-1].xcor()
        y = cuerpo[i-1].ycor()
        cuerpo[i].goto(x,y)

    if largo_cuerpo > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        cuerpo[0].goto(x,y)

    #Incremento de velocidad
    if puntuacion > 100:
        movimiento()
        time.sleep(0.2)
    elif puntuacion > 200:
        movimiento()
        time.sleep(0.15)
    elif puntuacion > 300:
        movimiento()
        time.sleep(0.1)
    elif puntuacion > 500:
        movimiento()
        time.sleep(0.05)
    else:
        movimiento()
        time.sleep(0.25)

