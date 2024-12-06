from turtle import *

def walk():
    forward(200)
    
def fall_back():
    left(180)
    forward(200)
    left(180)

# პარამეტრები / parameter ფუნქციის შიგნით იწერებიან
def walk_and_back(x):
    
    for i in range(x):# 10 ----- 50
        walk()
        fall_back()


walk_and_back(3)
# x = 50
exitonclick()