import turtle

#setting the screen
wn = turtle.Screen()
wn.title("Ping Pong Game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#first paddle(player)
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=6, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#second paddle(automated)
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=6, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = -0.2

#motion of paddle_a(up)
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

#motion of paddle_a(down)
def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)

#setting score
score=0
score_display=turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0,260)
score_display.write(f"Score:0",align="center",font=("Courier",24,"normal"))


#scoring:
def update_score():
    score_display.clear()
    score_display.write(f"Score:{score}",align="center",font=("Courier",24,"normal"))

wn.listen()
wn.onkey(paddle_a_up,"Up")
wn.onkey(paddle_a_down,"Down")

while True:
    wn.update()
    #motion of the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
     # Border collision
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle collision
    if (ball.dx > 0) and (ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50) and (ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.dx < 0) and (ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50) and (ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1

    # Move paddle B COMPUTER PADDLE
    if paddle_b.ycor() < ball.ycor() and abs(paddle_b.ycor() - ball.ycor()) > 10:
        paddle_b.sety(paddle_b.ycor() + 10)
    elif paddle_b.ycor() > ball.ycor() and abs(paddle_b.ycor() - ball.ycor()) > 10:
        paddle_b.sety(paddle_b.ycor() - 10)
