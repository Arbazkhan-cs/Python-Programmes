# from turtle import *
# # Control
#
# import pyautogui as auto
# import time
#
# for i in range(1):
#     auto.click(x=1250, y=2)
#     time.sleep(1)
#     auto.click(x=900, y=1200)
#     time.sleep(1)
#     auto.write('HELLO WORLD :)')
#     time.sleep(1)
#     auto.click(x=1250, y=2)
#     time.sleep(1)
#     auto.click(x=800, y=1200)
#
#
# #Beautiful Drawing
#
# import turtle
# sc = turtle.Screen()
# sc.bgcolor('black')
# sc.setup(600, 600)
# spiral = turtle.Turtle()
# spiral.speed(10)
# col = ['red', 'green', 'blue', 'yellow', 'indigo', 'violet', 'orange']
# spiral.pensize(4)
# c = 0
#
# for i in range(0, 360, 12):
#     spiral.color(col[c])
#     spiral.seth(i)
#     spiral.circle(100)
#     if c == 6:
#         c = 0
#     else:
#         c += 1
#
#
# spiral.ht()
# turtle.done()
#
# # My Favourite Flower
#
# from turtle import *
# spiral = Turtle()
# bgcolor('black')
# screensize(600, 600)
# speed(10000)
# col = ['red', 'blue', 'green', 'yellow']
# # circle
# c = 0
# for i in range(180):
#     color('white')
#     circle(190-i, 90)
#     left(90)
#     circle(190-i, 90)
#     left(18)
#
#     if c == 3:
#         c = 0
#     else:
#         c += 1
#
# mainloop()
# done()
#
# # Flower
#
# from turtle import *
# # Screen
# sc = Screen()
# sc.bgcolor('black')
# sc.setup(600, 700)
#
#
# # Flower
# pensize(4)
# speed(10)
#
# # First Leaf
# color('yellow')
# fillcolor('yellow')
# begin_fill()
# right(30)
# circle(190, 90)
# left(90)
# circle(190, 90)
# end_fill()
#
# # Second Leaf
# color('indigo')
# fillcolor('indigo')
# begin_fill()
# left(18)
# circle(190, 90)
# left(90)
# circle(190, 90)
# end_fill()
#
# # Third Leaf
# color('violet')
# fillcolor('violet')
# begin_fill()
# left(18)
# circle(190, 90)
# left(90)
# circle(190, 90)
# end_fill()
#
# # Fourth Leaf
# color('blue')
# fillcolor('blue')
# begin_fill()
# left(18)
# circle(190, 90)
# left(90)
# circle(190, 90)
# end_fill()
#
# # Fifth Leaf
# color('orange')
# fillcolor('orange')
# begin_fill()
# left(18)
# circle(190, 90)
# left(90)
# circle(190, 90)
# end_fill()
#
#
# # For making the inner circle.
# fillcolor('red')
# begin_fill()
# left(33)
# forward(15)
# left(90)
# color('red')
# circle(20)
# end_fill()
#
#
# # For making the line.
# pensize(4)
# color('green')
# penup()
# left(100)
# forward(20)
# left(95)
# pendown()
# forward(300)
#
# ht()
# done()
#
#
# # Doremon
# # Screen
# sc = Screen()
# sc.bgcolor('black')
# sc.setup(400, 400)
# speed(12)
#
#
# # Face
# def face():
#     pensize(3)
#     backward(6)
#     right(360)
#     color('black')
#     fillcolor('#0a93f5')
#     begin_fill()
#     circle(90)
#     end_fill()
#
#     # Left Eye
#     pensize(3)
#     penup()
#     goto(-32, 140)
#     left(210)
#     pendown()
#     fillcolor('white')
#     begin_fill()
#     circle(82, 100)
#     left(50)
#     forward(100)
#     left(55)
#     circle(92, 85)
#     left(40)
#     forward(67)
#     end_fill()
#
#     penup()
#     goto(-16, 150)
#     pendown()
#     color('black')
#     fillcolor('white')
#     begin_fill()
#     circle(20, 170)
#     left(20)
#     circle(20, 170)
#     end_fill()
#
#     penup()
#     goto(-16, 135)
#     pendown()
#     fillcolor('black')
#     begin_fill()
#     circle(7)
#     end_fill()
#
#     color('black')
#     fillcolor('white')
#     penup()
#     goto(16, 150)
#     pendown()
#     begin_fill()
#     circle(20, 170)
#     left(20)
#     circle(20, 170)
#     end_fill()
#
#     color('black')
#     penup()
#     goto(18, 125)
#     pendown()
#     right(60)
#     circle(10, 120)
#
#     penup()
#     goto(-12, 110)
#     pendown()
#     fillcolor('red')
#     begin_fill()
#     circle(12)
#     end_fill()
#
#     penup()
#     goto(-3, 88)
#     pendown()
#     left(30)
#     forward(40)
#
#     penup()
#     goto(-54, 55)
#     pendown()
#     left(20)
#     circle(50, 138)
#
#     penup()
#     goto(-13, 78)
#     pendown()
#     left(100)
#     forward(35)
#     penup()
#     goto(-13, 72)
#     pendown()
#     left(12)
#     forward(35)
#     penup()
#     goto(-13, 66)
#     pendown()
#     left(15)
#     forward(35)
#
#     penup()
#     goto(4, 78)
#     pendown()
#     left(180)
#     forward(35)
#
#     penup()
#     goto(4, 74)
#     pendown()
#     right(195)
#     backward(35)
#
#     penup()
#     goto(4, 66)
#     pendown()
#     right(190)
#     forward(35)
#
#     penup()
#     goto(-54, 15)
#     right(100)
#     pendown()
#     fillcolor('red')
#     begin_fill()
#     circle(14, 60)
#     left(50)
#     forward(95)
#     left(60)
#     circle(13, 60)
#     end_fill()
#
#
# # Stomach
# def sto():
#     color('white')
#     fillcolor('#0a93f5')
#     begin_fill()
#     penup()
#     goto(-54, 15)
#     left(115)
#     circle(11, 90)
#     pendown()
#     right(100)
#     forward(80)
#     #fillcolor('white')
#     #begin_fill()
#     circle(20)
#     #end_fill()
#
#     penup()
#     goto(-75, -80)
#     right(180)
#     pendown()
#     forward(25)
#     left(45)
#     forward(25)
#     right(180)
#
#     forward(100)
#     right(90)
#     forward(23)
#     left(8)
#     #fillcolor('white')
#     #begin_fill()
#     circle(9, 172)
#     forward(60)
#
#     circle(9, 172)
#     #end_fill()
#     penup()
#     forward(5)
#     left(7)
#
#     backward(45)
#     right(90)
#
#     pendown()
#     circle(23, 190)
#     left(86)
#     penup()
#     forward(45)
#
#     pendown()
#     #fillcolor('white')
#     #begin_fill()
#     right(180)
#     circle(9, 175)
#     forward(60)
#
#     circle(9, 180)
#     forward(20)
#     #end_fill()
#
#     right(90)
#     forward(120)
#     right(180)
#     forward(10)
#     left(120)
#
#     forward(70)
#     #fillcolor('white')
#     #begin_fill()
#     circle(17)
#     #end_fill()
#     left(110)
#     penup()
#
#     forward(35)
#     pendown()
#     left(70)
#     forward(60)
#     end_fill()
#
#
# ht()
# face()
# sto()
#
# done()
