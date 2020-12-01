import turtle

#window title
turtle.title("My turtle program")

#instantiation of screen and turtle
s = turtle.getscreen()
t = turtle.Turtle()

#making the turtle a turtle
t.shape("turtle")

#turtle shape (larger)
t.shapesize(2,2,2)

#turtle color
t.fillcolor("blue")

#changing the size of the pen
t.pensize(5)

#changint the color of the pen
t.pencolor("black")

#first draw lines
t.speed(1)
t.right(90) #or t.rt
t.forward(90) #or t.fd
t.left(90) #or t.lt
t.backward(90) #or t.bk

t.goto(100,100)

t.home()

t.pensize(1)
t.speed(10)

#drawing a square and stamping the turtle on the vertices
t.fd(90)
t.stamp()
t.rt(90)
t.fd(90)
t.stamp()
t.rt(90)
t.fd(90)
t.stamp()
t.rt(90)
t.fd(90)
t.stamp()

t.goto(200,200)
t.circle(60)

t.goto(-200,200)
t.dot(60)

turtle.bgcolor("blue")

#creating a shape and filling it

t.begin_fill()
t.fd(100)
t.lt(120)
t.fd(100)
t.lt(120)
t.fd(100)
t.end_fill()

#clearing the screen
t.clear()

#smarter command
t.penup()
t.home()
t.pen(pencolor="purple", fillcolor="pink", pensize=10, speed=9)
t.pendown()
t.begin_fill()
t.circle(90)
t.end_fill()

#Working with clones

t2 = t.clone()
t2.color("magenta")
t2.circle(200)

