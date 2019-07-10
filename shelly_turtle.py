import turtle

shelly = turtle.Turtle()
shelly.shape('turtle')

shelly.forward(100) # moves shelly forward 100 steps
shelly.right(90)    # turns shelly right 90 degrees
shelly.left(60)     # turns shelly left 60 degrees
shelly.backward(100) # moves shelly backward 100 steps
shelly.color('red') # makes shelly in the color red
shelly.circle(80)  # makes shelly draw a circle the size of 80
shelly.penup()      # makes shelly lift pen
shelly.pendown()    # makes shelly put the pen down to draw
shelly.goto(50,105)  # move the x coordinate 50, y coordinate 105
shelly.hideturtle() # makes shelly not visible on the screen


turtle.mainloop()
