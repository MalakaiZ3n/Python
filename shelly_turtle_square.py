import turtle

shelly = turtle.Turtle()
shelly.shape('turtle')
shelly.color('red') # makes shelly in the color red

# makes shelly draw a square
for i in range (4):
    shelly.forward(100)
    shelly.left(90)
    print(i)

# shelly turns and draws a circle
shelly.left(180)
shelly.circle(100)


turtle.mainloop()
