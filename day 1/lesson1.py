from turtle import *

#we want to paint a house

#step.1 draw a square
speed(30)

#speed(30)
width("7")
color("purple")
begin_fill()
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
end_fill()
#end of square

#drawing a door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)    #height of the door
right(90)
forward(70)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing a window

penup()
goto(0, 0)
right(150)
forward(70)
pendown()
width(7)
color("blue")
begin_fill()
right(90)
forward(55)
left(90)
forward(55)
left(90)
forward(55)
left(90)
forward(55)
end_fill()


penup()
goto(0, 0)
left(90)
forward(200)
left(90)
forward(70)
left(90)
pendown()
begin_fill()
forward(50)
right(90)
forward(55)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

exitonclick()