from tkinter import *
from tkinter import messagebox
import random

# Function to be called when the user clicks the 'No' button
def no():
    # Show an information messagebox to the user
    messagebox.showinfo(' ', 'Actually you are a alien too:)')
    quit()
# Function to respond to mouse motion
def motionMouse(event): 
    btnYes.place(x=random.randint(0, 500), y=random.randint(0, 500))

# Create the window
root = Tk()
root.geometry('600x600') 
root.title('survey')

# Prevent the window from being resizable
root.resizable(width=False, height=False)

#background color
root['bg'] = 'white'

# Create a label containing the survey question and place it in the window
Label = Label(root, text='Are you alien?', font='Arial 20 bold', bg='white').pack() 

# Bind the motionMouse function to respond to the Enter event on the 'Yes' button
btnYes = Button(root, text='No', font=('Arial 20 bold'))
btnYes.place(x=170, y=100) 
btnYes.bind('<Enter>', motionMouse) #move

# Create the 'No' button, place it at the initial position, and bind it to the 'no' function
btnNo = Button(root, text='Yes', font='Arial 28 bold', command=no)
btnNo.place(x=350, y=100)

# Display the window
root.mainloop()