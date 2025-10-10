#Activity 1

# Import necessary libraries
from tkinter import *
# Create window
window = Tk()
window.title("Event Handler")
window.geometry("300x300")
# Event Handler for Keypress
def handle_keypress(event):
    #Print the character associated to the key pressed
    print(event.char)
# Bind keypress event to handle_keypress()
window.bind("<Key>", handle_keypress)
# Event handler for button click
def handle_click(event):
    print("\nThe button was clicked!")
button = Button(text="Click me!")
button.pack()
# Bind click event to handle_click()
button.bind("<Button-1>", handle_click)
# Start the GUI event loop
window.mainloop()


print("############################################################################")

#Activity 2

# Import necessary libraries
from tkinter import *
from tkinter import messagebox
# Setup Tkinter Window
root = Tk()
root.geometry("300x300")
"""Function for Displaying Warning Message
 This will be called once the button is clicked
 messagebox.showwarning("Window Name", "Text to be displayed")"""
def msg():
    messagebox.showwarning("Alert", "Stop! VirusFound.")
# Adding Button Widget to Window
button = Button(root, text="Scan for Virus", command=msg)
button.place(x=40, y=80)
# Entering main event loop
root.mainloop()
