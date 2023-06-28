import turtle

wn = turtle.Screen()
wn.title("Pong by Reis567")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)

# Raquete 1
raquete_a = turtle.Turtle()
raquete_a.speed(0)
raquete_a.shape("square")
raquete_a.color("white")
raquete_a.shapesize(stretch_wid=5,stretch_len=1)
raquete_a.penup()
raquete_a.goto(-350,0)

# Raquete 2
raquete_b = turtle.Turtle()
raquete_b.speed(0)
raquete_b.shape("square")
raquete_b.color("white")
raquete_b.shapesize(stretch_wid=5,stretch_len=1)
raquete_b.penup()
raquete_b.goto(350,0)


# BOLA

bola = turtle.Turtle()
bola.speed(0)
bola.shape("square")
bola.color("white")
bola.penup()
bola.goto(0,0)

bola.dx = 0.4
bola.dy = -0.4


# Funções

# Raquete A
def raquete_a_up():
    y = raquete_a.ycor()
    y+=20
    raquete_a.sety(y)

def raquete_a_down():
    y = raquete_a.ycor()
    y-=20
    raquete_a.sety(y)


# Raquete B
def raquete_b_up():
    y = raquete_b.ycor()
    y+=20
    raquete_b.sety(y)

def raquete_b_down():
    y = raquete_b.ycor()
    y-=20
    raquete_b.sety(y)

# Teclas vinculadas a movimento

wn.listen()

#Raquete A
wn.onkeypress(raquete_a_up,"w")
wn.onkeypress(raquete_a_down,"s")

# Raquete B

wn.onkeypress(raquete_b_up,"Up")
wn.onkeypress(raquete_b_down,"Down")

while True:
    wn.update()

    # Movimentação da bola
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    #Colisão com borda 
    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy*= -1
    
    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy*= -1

    if bola.xcor() > 390:
        bola.goto(0,0)
        bola.dx *= -1
    
    if bola.xcor() < -390:
        bola.goto(0,0)
        bola.dx *= -1
