import turtle
import random

# Configuração da tela
wn = turtle.Screen()
wn.title("Pong by Reis567")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Pontuação variáveis
score_a = 0
score_b = 0

# Raquete 1
raquete_a = turtle.Turtle()
raquete_a.speed(0)
raquete_a.shape("square")
raquete_a.color("white")
raquete_a.shapesize(stretch_wid=5, stretch_len=1)
raquete_a.penup()
raquete_a.goto(-350, 0)

# Raquete 2
raquete_b = turtle.Turtle()
raquete_b.speed(0)
raquete_b.shape("square")
raquete_b.color("white")
raquete_b.shapesize(stretch_wid=5, stretch_len=1)
raquete_b.penup()
raquete_b.goto(350, 0)

# Bola
bola = turtle.Turtle()
bola.speed(0)
bola.shape("square")
bola.color("white")
bola.penup()
bola.goto(0, 0)
bola.dx = 0.2
bola.dy = -0.2

# Pontuação
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Jogador 1: 0   Jogador 2: 0", align="center", font=("Courier", 24, "normal"))

# Variável de pausa
is_paused = False

# Função para pausar o jogo
def pause_game():
    global is_paused
    if is_paused:
        is_paused = False
        # Remove a tela de pausa quando o jogo é retomado
        pause_text.clear()
        continue_button.clear()
        continue_button.onclick(None)  # Remove o evento de clique do botão
    else:
        is_paused = True
        # Exibe a tela de pausa quando o jogo é pausado
        pause_text.write("Jogo pausado", align="center", font=("Courier", 24, "normal"))
        continue_button.goto(0, -50)
        continue_button.write("Pressione esc para continuar", align="center", font=("Courier", 18, "normal"))
        continue_button.onclick(continue_game)  # Associa a função continue_game ao clique do botão

# Função para continuar o jogo
def continue_game(x, y):
    global is_paused
    is_paused = False
    # Remove a tela de pausa quando o jogo é retomado
    pause_text.clear()

# Criação do objeto de texto para a mensagem de pausa
pause_text = turtle.Turtle()
pause_text.speed(0)
pause_text.color("white")
pause_text.penup()
pause_text.hideturtle()
pause_text.goto(0, 0)

# Criação do objeto de texto para o botão "Continuar"
continue_button = turtle.Turtle()
continue_button.speed(0)
continue_button.color("white")
continue_button.penup()
continue_button.hideturtle()
continue_button.goto(0, -50)


# Teclas vinculadas a movimento
wn.listen()
wn.onkeypress(pause_game, "Escape")

# Funções de movimento das raquetes
def raquete_a_up():
    y = raquete_a.ycor()
    if y < 250:
        y += 20
    raquete_a.sety(y)

def raquete_a_down():
    y = raquete_a.ycor()
    if y > -240:
        y -= 20
    raquete_a.sety(y)

def raquete_b_up():
    y = raquete_b.ycor()
    if y < 250:
        y += 20
    raquete_b.sety(y)

def raquete_b_down():
    y = raquete_b.ycor()
    if y > -240:
        y -= 20
    raquete_b.sety(y)

# Vinculando as teclas aos movimentos das raquetes
wn.onkeypress(raquete_a_up, "w")
wn.onkeypress(raquete_a_down, "s")
wn.onkeypress(raquete_b_up, "Up")
wn.onkeypress(raquete_b_down, "Down")

# Loop principal do jogo
while True:
    wn.update()

    if not is_paused:
        # Movimentação da bola
        bola.setx(bola.xcor() + bola.dx)
        bola.sety(bola.ycor() + bola.dy)

        # Verificação de colisão com as bordas
        if bola.ycor() > 290:
            bola.sety(290)
            bola.dy *= -1

        if bola.ycor() < -290:
            bola.sety(-290)
            bola.dy *= -1

        if bola.xcor() > 390:
            bola.goto(0, 0)
            bola.dx *= -1
            score_a += 1
            pen.clear()
            pen.write("Jogador 1: {}   Jogador 2: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

        if bola.xcor() < -390:
            bola.goto(0, 0)
            bola.dx *= -1
            score_b += 1
            pen.clear()
            pen.write("Jogador 1: {}   Jogador 2: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

        # Verificação de colisão com as raquetes
        if (bola.xcor() > 340 and bola.xcor() < 350) and (bola.ycor() < raquete_b.ycor() + 50 and bola.ycor() > raquete_b.ycor() - 50):
            bola.setx(340)
            bola.dx *= -1

        if (bola.xcor() < -340 and bola.xcor() > -350) and (bola.ycor() < raquete_a.ycor() + 50 and bola.ycor() > raquete_a.ycor() - 50):
            bola.setx(-340)
            bola.dx *= -1

    # Mantém o jogo em pausa até que seja retomado
    while is_paused:
        wn.update()
