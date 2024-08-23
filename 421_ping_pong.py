"""
@Author: Pratik Pramod Alkutkar
@Goal: To make a two player pig pong game.
@Controlls:- (Player 1 - W for Up and S for down) & (Player 2 - Up arrorw for Up and Down arrow for Down)
"""
import turtle
win = turtle.Screen()
win.title("Ping Pong Game by Pratik Alkutkar")
win.bgcolor("black")
win.tracer(0)
win.setup(width=800, height=600)

#score
score_a = 0
score_b=0

#paddle a
paddle_a=turtle.Turtle()
paddle_a.speed(0) #speed of animation 
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(5,1)
paddle_a.penup()
paddle_a.goto(-350,0)

#paddle b
paddle_b=turtle.Turtle()
paddle_b.speed(0) #speed of animation 
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(5,1)
paddle_b.penup()
paddle_b.goto(350,0)

#ball
ball=turtle.Turtle()
ball.speed(0) #speed of animation 
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(0,0)
ball.dx = 0.1
ball.dy = -0.1

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0".format(score_a,score_b), align="center", font=("Times new roman", 24, "normal"))

#function
def paddle_a_up():
    y = paddle_a.ycor()
    y +=20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -=20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y +=20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -=20
    paddle_b.sety(y)

# keyboard binding 
win.listen()
win.onkeypress(paddle_a_up,"w")
win.onkeypress(paddle_a_down,"s") 
win.onkeypress(paddle_b_up,"Up")
win.onkeypress(paddle_b_down,"Down") 

#main game loop 

while True:
    win.update()
    #move the ball 
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy) 

    #border checking 
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1 #reverse direction 
        
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1 #reverse direction 

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a +=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b), align="center", font=("Times new roman", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b +=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b), align="center", font=("Times new roman", 24, "normal"))

    #paddle and ball collisions 
    if (ball.xcor()>340 and ball.xcor()< 350) and (ball.ycor()<paddle_b.ycor()+40 and ball.ycor()> paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor()< -340 and ball.xcor()> -350) and (ball.ycor()<paddle_a.ycor()+40 and ball.ycor()> paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1