import turtle 
import random

''' 
#How to play-
#use space bar to shoot
#use arrow keys to turn

'''
def lvlStart():
  global level
  global criminals
  global counter
  global deadcounter
  x = 30
  y = 200
  criminals = []
  deadcounter = 0
  for i in range(level):
    #reseting the rows
    x -= 30
    y += 30
    for j in range(i + 1):
      #this populates the column 
      c = turtle.Turtle()
      c.speed(0)
      c.color("red")
      c.penup()
      c.goto(x + (60 * j), y)
      c.shape("turtle")
      c.setheading(270)
      criminals.append(c)
      screen.update()
  counter = len(criminals)


 

def shoot():
  global level
  global counter
  global criminals
  global deadcounter
  b = turtle.Turtle()
  b.penup()
  b.goto(t)
  b.color("yellow")
  b.speed(1000)
  b.setheading(t.heading())
  for i in range(60):
    b.forward(level + 10)
    screen.update()
    for criminal in criminals:
      if abs(b.xcor() - criminal.xcor()) < 10 and abs(b.ycor() - criminal.ycor()) < 10: 
        b.ht()
        b.goto(10000, 10000)
        criminal.ht()
        criminal.goto(1000, 1000)
        deadcounter += 1
        print deadcounter
        if deadcounter == counter:
          level += 1
          lvlStart()
        
        
      


  b.ht()
  screen.update()
def turnLeft():
  t.left(5)
  screen.update()

def turnRight():
  t.right(5)
  screen.update()

t = turtle.Turtle()

screen = turtle.Screen()
screen.bgcolor("black")
screen.tracer(0)
t.shape('turtle')
t.color("blue")
t.penup()
t.goto(0, -200)
t.setheading(90)
screen.update()
L = turtle.Turtle()

L.goto(-350,-150)
L.color("light green")
L.forward(650)
screen.update()

level = 1

loserwriter = turtle.Turtle()
loserwriter.color("white")
loserwriter.goto(0, 0)
loserwriter.ht()

writer = turtle.Turtle()
counter = 0
deadCounter = 0
criminals = []
wincheck = 0
losecheck = 0
lvlStart()  
screen.onkey(turnLeft, "Left")
screen.onkey(turnRight, "Right")
screen.onkey(shoot, "Space")
screen.listen()
screen.tracer(0)

def win():
  global wincheck
  global criminals
  global writer
  for criminal in criminals:
    criminal.ht()
  screen.update()
  writer.penup()
  writer.goto(0, 0)
  writer.color("white")
  writer.write("nice job! you saved the bank's money from being stolen!")
  wincheck = 1
while True:
  for criminal in criminals:
    criminal.forward(1)
    if criminal.ycor() < -145:
      loserwriter.st()
      loserwriter.clear()
      loserwriter.write("Oh well, it looks like you just got FIRED!")
      losecheck = 1
  screen.update()
  
  if level == 10:
    win()
    for criminal in criminals:
      criminal.ht()
      criminal.goto(1000,1000)
      
  if wincheck == 2:
    writer.clear()
    break
  if losecheck == 1:
    break
  
  
  
'''
Hard things i learned
 
 - list access
 - creating the functions for spawing criminals
 - shoot function
 - rows, coulmns, and placement (x,y)
'''
