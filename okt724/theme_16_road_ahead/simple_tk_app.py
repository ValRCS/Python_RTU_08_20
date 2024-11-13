# tk is a standart library for GUI in python

# let's make a window and show some buttons that when clicked increase or decrease a counter

import tkinter as tk # standart library for GUI in python

# let's make a window
window = tk.Tk() # we now have a window object
# let's change size
window.geometry("640x480") # just like old VGA resolution

counter = 0

cursor_x = 150
cursor_y = 100

# we also want to show the counter
counter_label = tk.Label(window, text=str(counter))

# let's add buttons
# we need to define a function that will be called when the button is clicked
def increase_counter():
    global counter # quick and dirty way to access global variable
    counter += 1    # now let's show debug information
    print(f"Counter: {counter}")
    # let's update the label
    counter_label.config(text=str(counter))

def decrease_counter():
    global counter
    counter -= 1
    # now let's show debug information
    print(f"Counter: {counter}")
    counter_label.config(text=str(counter))

# now let's create buttons
# note we pass function name without brackets
# functions can be passed as arguments in Python!
increase_button = tk.Button(window, text="Increase", command=increase_counter)
decrease_button = tk.Button(window, text="Decrease", command=decrease_counter)

# let's add a canvas with some drawing
# we need to create a canvas object
canvas = tk.Canvas(window, width=300, height=200)
# now we need to draw something
# we can draw lines
# canvas.create_line(0, 0, 300, 200, fill="red")
# let's add a border to the canvas
canvas.create_rectangle(1, 1, 299, 199, outline="black")
# TODO why left and top rectangles are not visible?



# now we need to add the buttons to the window
# increase_button.pack()
# decrease_button.pack()
# counter_label.pack()
# let's have increase and decrease buttons next to each other
# and counter label below them
# increase_button.grid(row=0, column=0)
# decrease_button.grid(row=0, column=1)
# counter_label.grid(row=1, column=0, columnspan=2)

# i want to center increase and decrease buttons next to each other
# and counter label below them
increase_button.pack(side=tk.LEFT)
decrease_button.pack(side=tk.LEFT)
counter_label.pack()

# let's add a canvas
canvas.pack()

# let's add a Quit option on the menu
def quit_app():
    window.quit()
    window.destroy()

# let's make a menu
menu = tk.Menu(window)
window.config(menu=menu)
file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
# file_menu.add_command(label="Quit", command=quit_app)
# i also want Q shortcut for quit
# again note how I pass function name that will actually be called and do the quitting
file_menu.add_command(label="Quit", command=quit_app, accelerator="Q")

# we also need to process keyboard events
# we need to bind keyboard events to functions
def key_pressed(event):
    global cursor_y # ugly but works
    global cursor_x # ugly but works
    print(f"Key pressed: {event.keysym}")
    if event.keysym == "q":
        quit_app()
    # let's add arrow keys for drawing on canvas
    elif event.keysym == "Up":

        cursor_y -= 10
        canvas.create_line(cursor_x, cursor_y, cursor_x, cursor_y + 10, fill="blue")
    elif event.keysym == "Down":
        cursor_y += 10
        canvas.create_line(cursor_x, cursor_y, cursor_x, cursor_y + 10, fill="red")
    elif event.keysym == "Left":
        cursor_x -= 10
        canvas.create_line(cursor_x, cursor_y, cursor_x + 10, cursor_y, fill="green")
    elif event.keysym == "Right":
        cursor_x += 10
        canvas.create_line(cursor_x, cursor_y, cursor_x + 10, cursor_y, fill="black")

# now we need to bind the event to the window
window.bind("<Key>", key_pressed)

# now we need to run the main loop
window.mainloop()
