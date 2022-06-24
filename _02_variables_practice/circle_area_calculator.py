import turtle
from tkinter import messagebox, simpledialog, Tk
import math

# Goal: Write a Python program that asks the user for the radius 
#       of a circle and displays the area of that circle.
#       The formula for the area of a circle is πr^2.
#       See example image in package to check your output.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Ask the user for the radius in pixels and store it in a variable
    # simpledialog.askinteger()
    radius = simpledialog.askinteger(title='Game5', prompt='What radius do you want to put?')
    # Make a new turtle
    background45 = turtle.Turtle()
    # Have your turtle draw a circle with the correct radius
    # my_turtle.circle()
    background45.circle(radius)
    # Call the turtle .penup() method
    background45.penup()
    # Move your turtle to a new x,y position using .goto()
    background45.goto(-20, 30)
    # Calculate the area of your circle and store it in a variable
    # Hint, you can use math.pi
    circle = math.pi * math.pow(radius ,2)
    # Write the area of your circle using the turtle .write() method
    # my_turtle.write(arg="area = " + str(area), move=True, align='left', font=('Arial',8,'normal'))
    background45.write(arg="area = " + str(circle), move=True, align='left', font=('Arial',8,'normal'))
    # Hide your turtle
    background45.hideturtle()
    # Call turtle.done()
    turtle.done()
