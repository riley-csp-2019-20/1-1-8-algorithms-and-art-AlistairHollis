import turtle as trtl

drawer = trtl.Turtle()
drawer.speed(10)

# Creating Landscape
    # Creating Ocean
drawer.pencolor("blue")
drawer.fillcolor("blue")
drawer.begin_fill()
drawer.right(180)
drawer.forward(400)
drawer.right(270)
drawer.forward(400)
drawer.right(225)
drawer.forward(566)
drawer.end_fill()
    # Creating Beach
drawer.pencolor("orange")
drawer.fillcolor("orange")
drawer.begin_fill()
drawer.right(45)
drawer.forward(400)
drawer.right(90)
drawer.forward(400)
drawer.right(90)
drawer.forward(800)
drawer.right(135)
drawer.forward(566)
drawer.end_fill()

    ### Object: Small Tree (variable changed for each instance)

drawer.setheading(90)
drawer.pencolor("brown")
drawer.fillcolor("brown")

        ## Variables:

count = 0

if count < 1:
   while count == 0:
        drawer.begin_fill()
        drawer.forward(100)
        drawer.right(90)
        drawer.forward(25)
        drawer.right(90)
        drawer.forward(100)
        drawer.right(90)
        drawer.forward(25)
        drawer.right(90)
        drawer.end_fill()
        drawer.forward(100)
        drawer.right(90)
        drawer.forward(12.5)
        drawer.right(180)
        drawer.pencolor("green")
        drawer.fillcolor("green")
        drawer.begin_fill()
        drawer.forward(30)
        drawer.right(135)
        drawer.forward(42)
        drawer.right(90)
        drawer.forward(42)
        drawer.right(135)
        drawer.forward(30)
        drawer.end_fill()
        drawer.penup()
        drawer.right(270)
        drawer.forward(100)
        drawer.right(90)
        drawer.forward(12.5)
        drawer.setheading(90)
        drawer.pendown()
        count += 1

#Repositioning

drawer.penup()
drawer.right(90)
drawer.forward(200)
drawer.pendown()

    ### Object: Small Tree (variable changed for each instance)

drawer.setheading(90)
drawer.pencolor("brown")
drawer.fillcolor("brown")

        ## Variables:

countv2 = 0

if countv2 < 1:
   while countv2 == 0:
        drawer.begin_fill()
        drawer.forward(100)
        drawer.right(90)
        drawer.forward(25)
        drawer.right(90)
        drawer.forward(100)
        drawer.right(90)
        drawer.forward(25)
        drawer.right(90)
        drawer.end_fill()
        drawer.forward(100)
        drawer.right(90)
        drawer.forward(12.5)
        drawer.right(180)
        drawer.pencolor("green")
        drawer.fillcolor("green")
        drawer.begin_fill()
        drawer.forward(30)
        drawer.right(135)
        drawer.forward(42)
        drawer.right(90)
        drawer.forward(42)
        drawer.right(135)
        drawer.forward(30)
        drawer.end_fill()
        drawer.penup()
        drawer.right(270)
        drawer.forward(100)
        drawer.right(90)
        drawer.forward(12.5)
        drawer.setheading(90)
        drawer.pendown()
        countv2 += 1

# Repositioning

drawer.penup()
drawer.right(90)
drawer.forward(100)
drawer.right(270)

countv3 = 0

drawer.pencolor("brown")
drawer.fillcolor("brown")

if countv3 < 1:
   while countv3 == 0:
        drawer.begin_fill()
        drawer.forward(100)
        drawer.right(90)
        drawer.forward(25)
        drawer.right(90)
        drawer.forward(100)
        drawer.right(90)
        drawer.forward(25)
        drawer.right(90)
        drawer.end_fill()
        drawer.forward(100)
        drawer.right(90)
        drawer.forward(12.5)
        drawer.right(180)
        drawer.pencolor("green")
        drawer.fillcolor("green")
        drawer.begin_fill()
        drawer.forward(30)
        drawer.right(135)
        drawer.forward(42)
        drawer.right(90)
        drawer.forward(42)
        drawer.right(135)
        drawer.forward(30)
        drawer.end_fill()
        drawer.penup()
        drawer.right(270)
        drawer.forward(100)
        drawer.right(90)
        drawer.forward(12.5)
        drawer.setheading(90)
        drawer.pendown()
        countv3 += 1

# End of The World Setup

drawer.penup()
drawer.hideturtle
drawer.forward(300)
drawer.right(270)
drawer.forward(600)
drawer.pendown()
drawer.speed(0)
drawer.hideturtle()

loopphase = 0

drawer.pensize(25)

# End of The World

while loopphase == 0:

    drawer.pencolor("maroon")
    drawer.fillcolor("maroon")
    drawer.begin_fill()
    drawer.circle(100)
    drawer.end_fill()
    loopphase += 1
    
    while loopphase == 1:

        drawer.pencolor("red")
        drawer.fillcolor("red")
        drawer.begin_fill()
        drawer.circle(100)
        drawer.end_fill()
        loopphase += 1

        while loopphase == 2:

            drawer.pencolor("orange")
            drawer.fillcolor("orange")
            drawer.begin_fill()
            drawer.circle(100)
            drawer.end_fill()
            loopphase -= 2

wn = trtl.Screen()
wn.mainloop()