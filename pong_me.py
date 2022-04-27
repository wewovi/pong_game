import turtle
#screen for the game
window = turtle.Screen()
window.title("Pong game by @Hein_jo_rich")
window.bgcolor("black")
window.setup(width = 800, height =600)
window.tracer(0)

#left paddle
l_paddle = turtle.Turtle()
l_paddle .speed(0)
l_paddle.shape("square")
l_paddle.color("white")
l_paddle.shapesize(stretch_wid=5,stretch_len=1)
l_paddle.penup()
l_paddle.goto(-350,0)
#right paddle
r_paddle = turtle.Turtle()
r_paddle .speed(0)
r_paddle.shape("square")
r_paddle.color("white")
r_paddle.shapesize(stretch_wid=5,stretch_len=1)
r_paddle.penup()
r_paddle.goto(350,0)
#ball
ball_paddle = turtle.Turtle()
ball_paddle.speed(0)
ball_paddle.shape("square")
ball_paddle.color("white")
ball_paddle.penup()
ball_paddle.goto(0,0)
ball_paddle.dx = 2
ball_paddle.dy = 2

#Functions for left paddle
#left paddle moving up
def l_paddle_up():
    y = l_paddle.ycor()
    y += 20
    l_paddle.sety(y)
#left paddle moving down
def l_paddle_down():
    y= l_paddle.ycor()
    y -=20
    l_paddle.sety(y)
#left paddle moving left
def l_paddle_left():
    x = l_paddle.xcor()
    x -= 20
    l_paddle.setx(x)
#left paddle moving right
def l_paddle_right():
    x = l_paddle.xcor()
    x += 20
    l_paddle.setx(x)
#Functions for right paddle
#right paddle up
def r_paddle_up():
    y = r_paddle.ycor()
    y += 20
    r_paddle.sety(y)
#right paddle down
def r_paddle_down():
    y= r_paddle.ycor()
    y -=20
    r_paddle.sety(y)
#right paddle move left
def r_paddle_left():
    x = r_paddle.xcor()
    x -= 20
    r_paddle.setx(x)
#right paddle move right
def r_paddle_right():
    x = r_paddle.xcor()
    x += 20
    r_paddle.setx(x)
#keybord binding
window.listen()
window.onkeypress(r_paddle_up, "o")
window.onkeypress(r_paddle_down, "l")
window.onkeypress(r_paddle_left, "k")
window.onkeypress(r_paddle_right, "p")
window.onkeypress(l_paddle_up, " w")
window.onkeypress(l_paddle_down, "s")
window.onkeypress(l_paddle_left, "a")
window.onkeypress(l_paddle_right, "d")
#main game loop
while True:
    window.update()
    #move the ball_paddle
    ball_paddle.setx(ball_paddle.xcor() + ball_paddle.dx)
    ball_paddle.sety(ball_paddle.ycor() + ball_paddle.dy)
    #border checking
    if ball_paddle.ycor() > 290:
        ball_paddle.sety(290)
        ball_paddle.dy *= -1

    if ball_paddle.ycor() < -290:
        ball_paddle.sety(-290)
        ball_paddle.dy *= -1

    if ball_paddle.xcor()>390:
        ball_paddle.goto(0,0)
        ball_paddle.dx *= -1

    if ball_paddle.xcor() < -390:
        ball_paddle.goto(0,0)
        ball_paddle.dx *= -1