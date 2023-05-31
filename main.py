import turtle

drawingBoard = turtle.Screen()
drawingBoard.bgcolor("light blue")
drawingBoard.title("board")

jack = turtle.Turtle()


def jackWalk():
    jack.forward(5)


def jackLeft():
    jack.setheading((jack.heading()+2))
    # jack.left(10)


def jackRight():
    jack.setheading((jack.heading()-2))
    # jack.right(10)


def clearScreen():
    jack.clear()

def javkHome():
    penUp()
    jack.home()
    penDown()


def penUp():
    jack.penup()

def penDown():
    jack.pendown()

drawingBoard.listen()
drawingBoard.onkeypress(fun=jackWalk, key="space")
drawingBoard.onkeypress(fun=jackLeft, key="Left")
drawingBoard.onkeypress(fun=jackRight, key="Right")
drawingBoard.onkey(fun=clearScreen, key="c")
drawingBoard.onkey(fun=javkHome, key="h")
drawingBoard.onkey(fun=penUp, key="Up")
drawingBoard.onkey(fun=penDown, key="Down")



turtle.mainloop()