# packages imported
import turtle
import random
import time

############################## CREATING THE SCREEN ####################################

# creates a new window for the game using the screen class and assigns it to the variable screen
screen = turtle.Screen()
#sets the title of the game
screen.title("SNAKE GAME")
#specifies the size of the window
screen.setup(width=700, height= 700)
# this turns off the screen updates. This is used to stop the screen from updating in real-time. Useful for animation where you want to control when the screen refreshes to make the game run smoother
screen.tracer(0)
#sets the background color to a dark grey color
screen.bgcolor("#1d1d1d")

############################## CREATING BORDER ####################################

#sets the drawing speed of the turtle to 5
turtle.speed(5)
#sets the thickness of the line that the turtle draws 
turtle.pensize(4)
#lifts the pen up, so moving the turtle wont draw lines. This is used to move the turtle to a starting position for drawing without leaving a trail 
turtle.penup()
#moves the turtle to the specifies coordinates on the screen
turtle.goto(-310, 250)
# puts the pen down so the turtle will draw lines as it moves
turtle.pendown()
# sets the color of the pen to red, which will be the color of the border
turtle.color("red")
#these lines draw the border of the game area
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
#lifts the pen up after drawing the border to move without drawing
turtle.penup()
# hides the turtle icon after drawing the border
turtle.hideturtle()

############################## SCORE ####################################

#initializes the variable that will keep track of the player's score throughout the game
score = 0
#controls how fast the snake moves
delay = 0.1

############################## SNAKE ####################################

# new turtle object for the snake
snake = turtle.Turtle()
# intended to get the current speed
snake.speed()
# sets the shape of the snake to a square
snake.shape("square")
# color of the snake
snake.color("green")
#lifts the pen so that the moving the snake wont draw lines on the screen
snake.penup()
# positions the snake
snake.goto(0, 0)
#adds a custom attribute ' direction' to the snake object and initializes it to 'stop'. this will be used to control the movement direction of the snake
snake.direction = 'stop'

############################## FOOD ####################################

#creates another turtle object for the fruit
fruit = turtle.Turtle()
#sets the drawing speed of the fruit the fastest possible so it appears instantly
fruit.speed(0)
#sets the shape to a square
fruit.shape("square")
#sets the color
fruit.color("white")
#moving the fruit turtle wont draw lines
fruit.penup()
#positions the food
fruit.goto(30,30)
#initializes an empty list to keep track of fruit that has been eaten or needs to be removed from the screen
old_fruit = []

############################## SCORING ####################################

#creates a turtle object for displaiyng the score
scoring = turtle.Turtle()
#sets the drawing speed of the scoring turtle to the fastest possible, so updates appear instantly
scoring.speed(0)
# sets the color
scoring.color("white")
# ensures moving the scoring turtle wont draw lines
scoring.penup()
# hides the turtle icon
scoring.hideturtle()
# positions the scoring display towards the top of the screen
scoring.goto(0, 300)
# displays initial score messages
scoring.write("Score: ", align="center", font=("Courier", 24, "bold"))

############################## MOVEMENT ####################################

# thse functions check the current direction of the snake before chaing it to ensure it cannot immediately reverse
def snake_go_up():
  if snake.direction != "down":
    snake.direction = "up"
def snake_go_down():
  if snake.direction != "up":
    snake.direction = "down"
def snake_go_left():
  if snake.direction != "right":
    snake.direction = "left"
def snake_go_right():
  if snake.direction != "left":
    snake.direction = "right"

# this function moves the snake in the direction its facing by updating its x or y coordinate
def snake_move():
  if snake.direction == "up":
    y = snake.ycor()
    snake.sety(y + 20)
  if snake.direction == "down":
    y = snake.ycor()
    snake.sety(y - 20)
  if snake.direction == "left":
    x = snake.xcor()
    snake.setx(x - 20)
  if snake.direction == "right":
    x = snake.xcor()
    snake.setx(x + 20)

############################## KEYBOARD BINDING ####################################
# these lines set up keyboard bindings to allow the player to control the snake's direction using the arrow keys 
screen.listen()
screen.onkeypress(snake_go_up, "Up")
screen.onkeypress(snake_go_down, "Down")
screen.onkeypress(snake_go_left, "Left")
screen.onkeypress(snake_go_right, "Right")

############################## MAIN LOOP ####################################

#this line refreshes the screen, showing any changes made by the game logio
while True:
  screen.update()

  # snake & fruit colision 
  #this checks if the snake has collided with the fruit, if so the fruit is moved to a new rnadom location, the score is increased and a new piece of fruit is added
  if snake.distance(fruit) < 20:
    x = random.randint(-290, 270)
    y = random.randint(-240, 240)
    fruit.goto(x, y)
    scoring.clear()
    score += 1
    scoring.write("Score: {}".format(score), align="center", font=("Courier", 24, "bold"))
    delay -= 0.001

    # creating new foods
    new_fruit = turtle.Turtle()
    new_fruit.speed(0)
    new_fruit.shape("square")
    new_fruit.color("red")
    new_fruit.penup()
    old_fruit.append(new_fruit)

  #adding ball to snake
  # this logic moves each segment of the snake to follow the one in front of it creating the effect of the snake moving as a whole
  for index in range(len(old_fruit) -1, 0, -1):
    a = old_fruit[index -1].xcor()
    b = old_fruit[index -1].ycor()


    old_fruit[index].goto(a, b)
  
  if len(old_fruit) > 0:
    a = snake.xcor()
    b = snake.ycor()
    old_fruit[0].goto(a, b)
  snake_move()

  #snake & border colision
  #this checks if the snake has collided with the border
  if snake.xcor() >280 or snake.xcor() < -300 or snake.ycor() > 240 or snake.ycor() < -240:
    time.sleep(1)
    screen.clear()
    screen.bgcolor("turquoise")
    scoring.goto(0,0)
    scoring.write("   Game Over \n Your score is  {}".format(score), align="center", font=("Courier", 30, "bold"))

  # snake colisions
  # this checks if the snake has collided with any part of its body 
  for food in old_fruit:
    if food.distance(snake) < 20:
      time.sleep(1)
      screen.clear()
      screen.bgcolor("turquoise")
      scoring.got(0,0)
      scoring.write("   Game Over \n Your score is  {}".format(score), align="center", font=("Courier", 30, "bold"))

  
  time.sleep(delay)

#this ends the program
turtle.Terminator()






