#Imported turtle module
import turtle
wind=turtle.Screen()#intialize screen
wind.title("Bing Bong Game")#set the title of the window
wind.bgcolor("black")#set the back ground color
wind.setup(width=800,height=600)
wind.tracer(0)#stops the window from updating automatically

    #madrab1
madrab1=turtle.Turtle()#intializes turtle object(shape)
madrab1.speed(0)#set the speed of the animation
madrab1.shape("square")#set the shape of the object
madrab1.color("blue")#set the color of the shape
madrab1.shapesize(stretch_wid=5,stretch_len=1)#stretches the shape to meet the size
madrab1.penup()#stops the object from drawing lines
madrab1.goto(-350,0)#set the position of the object
    #madrab2
madrab2=turtle.Turtle()
madrab2.speed(0)
madrab2.shape("square")
madrab2.color("red")
madrab2.shapesize(stretch_wid=5,stretch_len=1)
madrab2.penup()
madrab2.goto(350,0)
    #ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=0.3
ball.dy=0.3


#score
score1=0
score2=0
score=turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("Blue Player: 0 Red Player:0",align="center",font=("Courier",24,"normal"))
#Developers
dev=turtle.Turtle()
dev.speed(0)
dev.color("purple")
dev.penup()
dev.hideturtle()
dev.goto(0,-260)
dev.write("This Game Developed By (Ahmad Alkhudr)",align="center",font=("Courier",12,"normal"))

#functions
def madrab1_up():
    y=madrab1.ycor()#get the y coordinate of the madrab1
    y+=40#set the y to increase be 20
    madrab1.sety(y)#set the y of the madrab1 to the new y coordinate
def madrab1_down():
    y=madrab1.ycor()
    y-=40
    madrab1.sety(y)
def madrab2_up():
    y=madrab2.ycor()
    y+=40
    
    madrab2.sety(y)
def madrab2_down():
    y=madrab2.ycor()
    y-=40
    madrab2.sety(y)

#keyboard bindings
wind.listen()#tell the window to expect keyboard input
wind.onkeypress(madrab1_up,"w")#when pressing w the function madrab1_up is invoked
wind.onkeypress(madrab1_down,"s")
wind.onkeypress(madrab2_up,"Up")
wind.onkeypress(madrab2_down,"Down")
#main game loop
while True:
    wind.update()#updates the screen every time the loop run

    #move the ball
    ball.setx(ball.xcor()+ball.dx)#ball starts at 0 and everytime loops run--->+2 xaxis
    ball.sety(ball.ycor()+ball.dy)#ball starts at 0 and everytime loops run--->+2 yaxis

    #border check , top border +300px , bottom border -300px , ball is 20 px
    if ball.ycor()>290:#if ball is at top border
        ball.sety(290)#set y coordinate +290
        ball.dy*=-1#reverse direction , making +2.5--->-2.5
    
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx*=-1
        score1 +=1
        score.clear()
        score.write("Blue Player: {} Red Player:{}".format(score1,score2),align="center",font=("Courier",24,"normal"))
    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx*=-1
        score2 +=1
        score.clear()
        score.write("Blue Player: {} Red Player:{}".format(score1,score2),align="center",font=("Courier",24,"normal"))
    #border check for madrab
    if madrab1.ycor()>280:
        madrab1.sety(-280)
    if madrab1.ycor()<-280:
        madrab1.sety(280)
    if madrab2.ycor()>280:
        madrab2.sety(-280)
    if madrab2.ycor()<-280:
        madrab2.sety(280)
    #tasadom madrab and ball
    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<madrab2.ycor()+40 and ball.ycor()>madrab2.ycor()-40):
        ball.setx(340)
        ball.dx*=-1
    if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<madrab1.ycor()+40 and ball.ycor()>madrab1.ycor()-40):
        ball.setx(-340)
        ball.dx*=-1

