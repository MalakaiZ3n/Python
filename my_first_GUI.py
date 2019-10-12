from tkinter import *

window = Tk()
window.title('My First GUI')

# function called when button is clicked


def hello_function():
    print('Hello World')  # prints to Shell
    # change display widget to show this text
    display_area.config(text="Hello, World", fg="yellow", bg='black')


# adding a button widget
button1 = Button(window, text="Click Me", command=hello_function)
button1.pack()  # this places the button on the window

# adding th display area - using label widget
display_area = Label(window, text="")
display_area.pack()  # this places the text area on the window


window.mainloop()  # GUI main event loop
