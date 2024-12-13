from turtle import *
speed(100)
def triangle(l):
 if l % 2 == 0:
  color("red") 
 else:
  color("green")
 begin_fill()
 color("blue")
 forward(100)
 left(120)
 forward(100)
 left(120)
 forward(100)
 end_fill()
 penup()
 left(30)
 forward(100)
 left(90)

for i in range(120):

    
 
 
 triangle(i)
exitonclick()