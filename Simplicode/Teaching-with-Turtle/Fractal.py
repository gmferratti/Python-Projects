import turtle,random

def make_a_tree():

    MINIMUM_BRANCH_LENGTH = 5

    def build_tree(t, branch_length, shorten_by, angle):

        turtle.colormode(255)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        tree.pencolor(r, g, b)

        if branch_length > MINIMUM_BRANCH_LENGTH:

            t.speed(0)

            t.forward(branch_length)
            new_length = branch_length - shorten_by

            t.left(angle)
            build_tree(t,new_length, shorten_by, angle)

            t.right(angle*2)
            build_tree(t, new_length, shorten_by, angle)

            t.left(angle)
            t.backward(branch_length)

    tree = turtle.Turtle()
    tree.hideturtle()
    tree.setheading(90)

    build_tree(tree, 50, 5, 30)

    turtle.mainloop()

    return 0

def make_a_snowflake():

    def koch_curve(t, iterations, length, shortening_factor, angle):

        if iterations == 0:
            t.forward(length)
        else:
            iterations = iterations - 1
            length = length / shortening_factor

            koch_curve(t, iterations, length, shortening_factor, angle)
            t.left(angle)
            koch_curve(t, iterations, length, shortening_factor, angle)
            t.right(angle * 2)
            koch_curve(t, iterations, length, shortening_factor, angle)
            t.left(angle)
            koch_curve(t, iterations, length, shortening_factor, angle)

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)

    for i in range(3):
        koch_curve(t, 4, 200, 3, 60)
        t.right(120)

    turtle.mainloop()
    return 0

#instantiation of screen and turtle

s = turtle.getscreen()
t = turtle.Turtle()

# turning the turtle to face upwards
t.rt(-90)

# the acute angle between
# the base and branch of the Y
t.angle = 30

make_a_tree()

turtle.Screen().exitonclick()