import turtle
import random

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Catch The Turtle")
drawing_board.setup(width=600, height=600)

# kursörümüzü yeşil kaplumbağa yapalım:
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.color("green")
my_turtle.penup()

# zaman sayacını gösterecek turtle'ı oluştur
counter_turtle = turtle.Turtle()
counter_turtle.color("black")
counter_turtle.hideturtle()
counter_turtle.penup()
counter_turtle.goto(0, 200)

# skor sayacını gösterecek turtle'ı oluştur:
score_turtle = turtle.Turtle()
score_turtle.color("blue")
score_turtle.hideturtle()
score_turtle.penup()
score_turtle.goto(0, 230)

start_time = 20
score = 0
game_running = True

# skoru güncelle ve ekranda göster:
def update_score():
    score_turtle.clear()
    score_turtle.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))

# zamanı güncelle ve ekranda göster:
def countdown(time_left):
    global game_running
    if time_left > 0:
        counter_turtle.clear()
        counter_turtle.write(time_left, align="center", font=("Arial", 24, "normal"))
        drawing_board.ontimer(lambda: countdown(time_left - 1), 1000)
    else:
        counter_turtle.clear()
        counter_turtle.write("Game Over!", align="center", font=("Arial", 24, "normal"))
        my_turtle.hideturtle()
        game_running = False

# turtle'ı rastgele hareket ettir:
def move_randomly():
    if game_running:
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        my_turtle.goto(x, y)
        drawing_board.ontimer(move_randomly, 500)

# turtle'a tıkla skoru arttır:
def increase_score(x, y):
    global score
    if game_running:
        score += 1
        update_score()

update_score()

countdown(start_time)

move_randomly()

my_turtle.onclick(increase_score)

turtle.mainloop()