import turtle
import random
import time

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

# zaman sayacını gösterecek turtle'ı oluştur
counter_turtle = turtle.Turtle()
counter_turtle.color("black")
counter_turtle.hideturtle()
counter_turtle.penup()
counter_turtle.goto(0, 200)

start_time = 20

# zamanı güncelle ve ekranda göster:
def countdown(time_left):
    if time_left > 0:
        counter_turtle.clear()
        counter_turtle.write(time_left, align="center", font=("Arial", 24, "normal"))
        drawing_board.ontimer(lambda: countdown(time_left - 1), 1000)
    else:
        counter_turtle.clear()
        counter_turtle.write("Game Over!", align="center", font=("Arial", 24, "normal"))
        turtle.hideturtle()
        my_turtle.hideturtle()

countdown(start_time)

turtle.mainloop()