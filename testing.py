# Importing The Turtle Module!.

from turtle import Turtle, Screen


# Making The Turtle And The Window/Screen!

my_turtle = Turtle()
my_screen = Screen()

# Setting The Color Of The Background To Black!.

my_screen.bgcolor("black")
my_screen.tracer(0)
my_turtle.color("red")
my_screen.update()
# my_screen.tracer(0)
my_turtle.color("green")
my_screen.update()

# Using The turtle.exitonclick() Method To Only Exit When The User Clicks On The Screen!

my_screen.exitonclick()