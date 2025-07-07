import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

win = turtle.Screen()
win.title("Snake Game")
win.bgcolor("black")
win.setup(width=600, height=600)
win.tracer(0)

head = turtle.Turtle()
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

def go_up(): head.direction = "up"
def go_down(): head.direction = "down"
def go_left(): head.direction = "left"
def go_right(): head.direction = "right"

win.listen()
win.onkey(go_up, "w")
win.onkey(go_down, "s")
win.onkey(go_left, "a")
win.onkey(go_right, "d")

while True:
    win.update()

    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        segments.clear()

    if head.direction == "up": head.sety(head.ycor() + 20)
    if head.direction == "down": head.sety(head.ycor() - 20)
    if head.direction == "left": head.setx(head.xcor() - 20)
    if head.direction == "right": head.setx(head.xcor() + 20)

    if head.distance(food) < 20:
        x, y = random.randint(-290, 290), random.randint(-290, 290)
        food.goto(x, y)
        segment = turtle.Turtle()
        segment.shape("square")
        segment.color("grey")
        segment.penup()
        segments.append(segment)

    for i in range(len(segments)-1, 0, -1):
        segments[i].goto(segments[i-1].pos())
    if segments:
        segments[0].goto(head.pos())

    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            segments.clear()

    time.sleep(delay)
