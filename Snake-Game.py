import turtle
import time
import random

delay=0.1
segments= []

# set up the screen
win = turtle.Screen()
win.title("My Super Awsome Snake Game")
win.bgcolor("red")
win.setup(width=500,height=500)
win.tracer(0)

# Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("green")
head.penup()
head.goto(0, 100)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("black")
food.penup()
food.shapesize(0.50, 0.50)
food.goto(0, 0)


def go_up():
    if head.direction != "down":
        head.direction = "up"
 
def go_down():
    if head.direction != "up":
        head.direction = "down"
 
def go_right():
    if head.direction != "left":
        head.direction = "right"
 
def go_left():
    if head.direction != "right":
        head.direction = "left"

# Main game loop
while True:
    win.update()
    
    if head.distance(food) < 15:
        # move the food to a random position on screen
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

    # move the end segment in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

        # Move segment 0 to where the head is
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x, y)

# Check for border collision
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
           segment.goto(1000, 1000)
 
        # clear segment list
        segments.clear()

# Check for head collision
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
 
            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
 
            # clear segment list
            segments.clear()
    
    high_score = 0

    # Increase the score
    score = score+10
 
    if score > high_score:
            high_score = score

# reset score
            score = 0
 
            # update score
pen.clear()
pen.write("Score: 0 High Score: {}".format(high_score), align="center", font=("Courier", 24, "bold")
    
    
    move()
    win.listen()
    win.onkey(go_up, "w")
    win.onkey(go_down, "s")
    win.onkey(go_right, "d")
    win.onkey(go_left, "a")
    time.sleep(delay)