import turtle
import time as t
import random as rand

delay = 0.1
score = 0
high_score = 0

# SCREEN
window = turtle.Screen()
window.title("Classic snake")
window.bgcolor("black")
window.setup(width=600, height=600)
window.tracer(0)

# SNAKE
snake_front = turtle.Turtle()
snake_front.shape("square")
snake_front.color("red")
snake_front.penup()
snake_front.goto(0, 0)
snake_front.direction = "Stop"

# COLLECTABLES
food = turtle.Turtle()
food.speed(0)
food.shape(rand.choice(['square', 'triangle', 'circle']))
food.color(rand.choice(['green', 'purple', 'yellow']))
food.penup()
food.goto(0, 100)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Punkte: 0 | Highscore: 0", align="center", font=("candara", 24, "bold"))

def up():
	if snake_front.direction != "down":
		snake_front.direction = "up"

def down():
	if snake_front.direction != "up":
		snake_front.direction = "down"

def left():
	if snake_front.direction != "right":
		snake_front.direction = "left"

def right():
	if snake_front.direction != "left":
		snake_front.direction = "right"

def move():
	if snake_front.direction == "up":
		y = snake_front.ycor()
		snake_front.sety(y+20)
	if snake_front.direction == "down":
		y = snake_front.ycor()
		snake_front.sety(y-20)
	if snake_front.direction == "left":
		x = snake_front.xcor()
		snake_front.setx(x-20)
	if snake_front.direction == "right":
		x = snake_front.xcor()
		snake_front.setx(x+20)

window.listen()
window.onkeypress(up, "w")
window.onkeypress(down, "s")
window.onkeypress(left, "a")
window.onkeypress(right, "d")

segments = []

# GAME
while True:
	window.update()

	if snake_front.xcor() > 290 or snake_front.xcor() < -290 or snake_front.ycor() > 290 or snake_front.ycor() < -290:
		t.sleep(1)
		snake_front.goto(0, 0)
		snake_front.direction = "Stop"
		colors = rand.choice(['red', 'blue', 'green'])
		shapes = rand.choice(['square', 'circle'])
		for segment in segments:
			segment.goto(1000, 1000)
		segments.clear()
		score = 0
		delay = 0.1
		pen.clear()
		pen.write("Punkte : {} Highscore : {} ".format(score, high_score), align="center", font=("candara", 24, "bold"))

	if snake_front.distance(food) < 20:
		x = rand.randint(-270, 270)
		y = rand.randint(-270, 270)
		food.goto(x, y)

		# MAKE SNAKE BIGGER
		new_segment = turtle.Turtle()
		new_segment.speed(0)
		new_segment.shape("square")
		new_segment.color("red")
		new_segment.penup()
		segments.append(new_segment)
		delay -= 0.001
		score += 10
		if score > high_score:
			high_score = score
		pen.clear()
		pen.write("Punkte : {} Highscore : {} ".format(score, high_score), align="center", font=("candara", 24, "bold"))

	# COLLISION DETECTION
	for index in range(len(segments)-1, 0, -1):
		x = segments[index-1].xcor()
		y = segments[index-1].ycor()
		segments[index].goto(x, y)

	if len(segments) > 0:
		x = snake_front.xcor()
		y = snake_front.ycor()
		segments[0].goto(x, y)

	move()

	for segment in segments:
		if segment.distance(snake_front) < 20:
			t.sleep(1)
			snake_front.goto(0, 0)
			snake_front.direction = "stop"
			colors = rand.choice(['red', 'blue', 'green'])
			shapes = rand.choice(['square', 'circle'])

			for segment in segments:
				segment.goto(1000, 1000)
			
			segment.clear()
			score = 0
			delay = 0.1
			pen.clear()
			pen.write("Punkte : {} Highscore : {} ".format(score, high_score), align="center", font=("candara", 24, "bold"))
	
	t.sleep(delay)

window.mainloop()