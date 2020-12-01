####
#Recipes.py

#Dominick Johnston
####

# Main function for launching recipe app
# theprogram utizizes the Model-View-Control paradigm.


# Imports
from tkinter import *


# Class Declarations
class recipe(object):
    def __init__(self,ingredients,steps):
        self.ingredients = ingredients
        self.steps = steps


# launches the home screen for the app
def launchHome(data):
    pass

# the main loop of the program runs on this. Here we update the model based
# on user actions
def tick(canvas, data):
    pass


def redrawAll(canvas, data):
    canvas.create_text(data.width/2, 20,text="Welcome to Recipe Viewer",)

def keyPressed(canvas, data):
    pass

def mousePressed(canvas, data):
    pass

# Main loop of recipe app. User interacts with UI through this.
def init(width=800, height=800):
    # Define 4 wrapper functions to manage the UI
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        tick(canvas, data)
        redrawAllWrapper(canvas, data)
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)

    # Set up data and call launchHome
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 10 # milliseconds
    root = Tk()
    root.resizable(width=False, height=False) # disallows resizing window
    launchHome(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")



# Main function
def main():
    print("in main")
    init()


# Run main when file is run
if __name__ == '__main__':
    main()