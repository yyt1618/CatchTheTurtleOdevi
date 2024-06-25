import turtle
import random

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Catch The Turtle")
drawing_board.setup(width=600, height=600)
my_turtle = turtle.Turtle()

# kursörümüzü yeşil kaplumbağa yapalım:
my_turtle.shape("turtle")
my_turtle.color("green")

# kalemi kaldıralım:
my_turtle.penup()

turtle.mainloop()