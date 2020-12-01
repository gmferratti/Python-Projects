#------------------------------------------------------------------------------------------------#
#-----------------------DRAWING COOL SHAPES WITH TURTLE------------------------------------------#
#------------------------------------------------------------------------------------------------#

import turtle,random

def draw_square(size):
    for i in range(4):
        t.forward(size)
        t.right(90)
    return 0

def draw_circles(step, n_circles):
    n = step
    while n <= (n_circles*step):
        t.circle(n)
        n = n+step

def draw_star(side_length):
    star = turtle.Turtle()
    for i in range(5):
        star.forward(side_length)
        star.right(144)

def draw_stars(step,strokes):
    star = turtle.Turtle()
    for i in range(strokes):
        star.forward(i*step)
        star.right(144)

def draw_polygon(num_sides,side_length):
    polygon = turtle.Turtle()
    angle = 360/num_sides
    for i in range(num_sides):
        polygon.forward(side_length)
        polygon.right(angle)

def polygon_spiral(num_sides,length,iterations):
    polygon = turtle.Turtle()
    polygon.speed(0)
    for i in range(iterations):
        polygon.forward(length)
        polygon.right(360/num_sides)
        length = length + length * 0.005
        polygon.right(2)

def draw_matrix(columns, lines):
    dot_distance = 25
    pen = turtle.Turtle()
    pen.penup()
    for x in range(lines):
        for y in range(columns):
            pen.dot()
            pen.forward(dot_distance)
        pen.backward(dot_distance*columns)
        pen.right(90)
        pen.forward(dot_distance)
        pen.left(90)

def ask_and_draw():
    while True:
        shape = input("Which shape would you like me to draw?")
        try:
            if shape == "square":
                draw_square(200)
                break
            elif shape == "circle":
                draw_circles(200, 1)
                break
            elif shape == "star":
                draw_star(200)
                break
            elif shape == "triangle":
                draw_polygon(3,200)
                break
            elif shape == "hexagon":
                draw_polygon(6,200)
                break
            elif shape == "pentagon":
                draw_polygon(5,200)
                break
            else:
                print("Invalid shape.")
        except:
            print("Ops, something went wrong!")
    print("Okey dokey")

def curious_pattern(side_step, rgb_step,iteractions):
    turtle.colormode(255)
    painter = turtle.Turtle()
    painter.speed(0)

    def do_it(n):
        for i in range(120):
            painter.forward(n)
            painter.left(121)

    rgb = rgb_step
    side = side_step

    for i in range(iteractions):
        x = 0 + side/4
        y = -300 + side/4
        painter.up()
        painter.setpos(x,y)
        painter.setheading(90)
        painter.pencolor(rgb,0,rgb)
        painter.down()
        rgb = rgb + rgb_step
        do_it(side)
        side = side + side_step

def draw_warphole():

    def reset_position():
        ninja.penup()
        ninja.goto(0,0)
        ninja.pendown()

    ninja = turtle.Turtle()
    ninja.speed(0)

    #drawing a circular pattern
    for i in range(180):
        #ocuupying all the canvas
        for i in range(3):
            ninja.pencolor("#000000")
            ninja.forward(100)
            ninja.right(30)
            ninja.pencolor("#7E7E7E")
            ninja.forward(20)
            ninja.left(60)
            ninja.pencolor("#000000")
            ninja.forward(50)
            ninja.right(30)

        reset_position()
        ninja.right(2)

def turtle_race():
    #naming the window
    s = turtle.getscreen()
    s.title("CORRIDA DE TARTARUGAS")

    #setting player 1
    player_one = turtle.Turtle()
    player_one.color("red")
    player_one.shape("turtle")
    player_one.penup()
    player_one.goto(-200,100)

    #setting player 2
    player_two = player_one.clone()
    player_two.color("blue")
    player_two.penup()
    player_two.goto(-200, -100)

    #setup speed
    player_one.speed(0)
    player_two.speed(0)

    #making the marks on the ground
    player_one.pencolor("black")
    player_one.goto(-170,150)
    player_one.right(90)
    linhas = range(20)
    colunas = range(12)
    for linha in linhas:
        for coluna in colunas:
            player_one.pendown()
            player_one.forward(20)
            player_one.penup()
            player_one.forward(5)
        player_one.backward(len(colunas)*25)
        player_one.left(90)
        player_one.write(linha+1)
        player_one.forward(20)
        player_one.right(90)

    #restoring default configuration
    player_one.goto(-200,100)
    player_one.setheading(0)
    player_one.pencolor("red")

    #making turtle hole #1
    player_one.goto(250,50)
    player_one.pendown()
    player_one.begin_fill()
    player_one.circle(50)
    player_one.end_fill()
    player_one.penup()

    #writing hole #1
    player_one.pencolor("white")
    player_one.goto(238,100)
    player_one.pendown()
    player_one.write("Hole 1")
    player_one.penup()

    #setting to initial position
    player_one.pencolor("red")
    player_one.goto(-200,100)

    # making turtle hole #2
    player_two.goto(250, -150)
    player_two.pendown()
    player_two.begin_fill()
    player_two.circle(50)
    player_two.end_fill()
    player_two.penup()

    # writing hole #2
    player_two.pencolor("white")
    player_two.goto(238, -100)
    player_two.pendown()
    player_two.write("Hole 2")
    player_two.penup()

    #setting the initial position of P2
    player_two.goto(-200, -100)
    player_two.color("blue")

    #creating the die
    die = [1,2,3,4,5,6]

    #setting the default speed
    player_one.speed(10)
    player_two.speed(10)

    #main loop
    game_over = False

    while not game_over:
        #check if someone won
        if player_one.xcor() >= 175:
            player_one.fillcolor("yellow")
            print("Red wins!")
            game_over =True
            break
        if player_two.xcor() >= 175:
            player_two.fillcolor("yellow")
            print("Blue wins!")
            game_over = True
            break

        input("P1 turn: press enter to roll the die")
        die01_result = random.choice(die)
        print("You got:", die01_result)
        player_one.forward(20*die01_result)

        input("P2 turn: press enter to roll the die")
        die02_result = random.choice(die)
        print("You got:",die02_result)
        player_two.forward(20*die02_result)

    return 0

def cool_shape_01():
    #setup
    pen = turtle.Turtle()
    pen.speed(5)
    pen.pencolor("white")
    s = turtle.getscreen()
    s.bgcolor("black")

    #going to start point
    pen.up()
    pen.rt(45)
    pen.fd(99)
    pen.rt(135)

    x = 0
    pen.down()

    while x<120:
        for i in range(6):
            pen.fd(200)
            pen.rt(61)

        pen.rt(10)
        x += 1

    return 0

def cool_shape_02():

    # setup
    pen = turtle.Turtle()
    pen.speed(5)
    pen.pencolor("white")
    s = turtle.getscreen()
    s.bgcolor("black")

    # setting the turtle to receive rgb inputs
    turtle.colormode(255)

    x = 1
    while x < 400:

        #random rgb
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        pen.pencolor(r,g,b)

        pen.fd(50+x)
        pen.rt(91)

        x += 1
    return 0

def cool_shape_03():

    turtle.setup(width=600, height=500)
    turtle.reset()
    turtle.hideturtle()
    turtle.speed(0)

    turtle.bgcolor('black')

    c = 0
    x = 0

    colors = [
        # reddish colors
        (1.00, 0.00, 0.00), (1.00, 0.03, 0.00), (1.00, 0.05, 0.00), (1.00, 0.07, 0.00), (1.00, 0.10, 0.00),
        (1.00, 0.12, 0.00), (1.00, 0.15, 0.00), (1.00, 0.17, 0.00), (1.00, 0.20, 0.00), (1.00, 0.23, 0.00),
        (1.00, 0.25, 0.00), (1.00, 0.28, 0.00), (1.00, 0.30, 0.00), (1.00, 0.33, 0.00), (1.00, 0.35, 0.00),
        (1.00, 0.38, 0.00), (1.00, 0.40, 0.00), (1.00, 0.42, 0.00), (1.00, 0.45, 0.00), (1.00, 0.47, 0.00),
        # orangey colors
        (1.00, 0.50, 0.00), (1.00, 0.53, 0.00), (1.00, 0.55, 0.00), (1.00, 0.57, 0.00), (1.00, 0.60, 0.00),
        (1.00, 0.62, 0.00), (1.00, 0.65, 0.00), (1.00, 0.68, 0.00), (1.00, 0.70, 0.00), (1.00, 0.72, 0.00),
        (1.00, 0.75, 0.00), (1.00, 0.78, 0.00), (1.00, 0.80, 0.00), (1.00, 0.82, 0.00), (1.00, 0.85, 0.00),
        (1.00, 0.88, 0.00), (1.00, 0.90, 0.00), (1.00, 0.93, 0.00), (1.00, 0.95, 0.00), (1.00, 0.97, 0.00),
        # yellowy colors
        (1.00, 1.00, 0.00), (0.95, 1.00, 0.00), (0.90, 1.00, 0.00), (0.85, 1.00, 0.00), (0.80, 1.00, 0.00),
        (0.75, 1.00, 0.00), (0.70, 1.00, 0.00), (0.65, 1.00, 0.00), (0.60, 1.00, 0.00), (0.55, 1.00, 0.00),
        (0.50, 1.00, 0.00), (0.45, 1.00, 0.00), (0.40, 1.00, 0.00), (0.35, 1.00, 0.00), (0.30, 1.00, 0.00),
        (0.25, 1.00, 0.00), (0.20, 1.00, 0.00), (0.15, 1.00, 0.00), (0.10, 1.00, 0.00), (0.05, 1.00, 0.00),
        # greenish colors
        (0.00, 1.00, 0.00), (0.00, 0.95, 0.05), (0.00, 0.90, 0.10), (0.00, 0.85, 0.15), (0.00, 0.80, 0.20),
        (0.00, 0.75, 0.25), (0.00, 0.70, 0.30), (0.00, 0.65, 0.35), (0.00, 0.60, 0.40), (0.00, 0.55, 0.45),
        (0.00, 0.50, 0.50), (0.00, 0.45, 0.55), (0.00, 0.40, 0.60), (0.00, 0.35, 0.65), (0.00, 0.30, 0.70),
        (0.00, 0.25, 0.75), (0.00, 0.20, 0.80), (0.00, 0.15, 0.85), (0.00, 0.10, 0.90), (0.00, 0.05, 0.95),
        # blueish colors
        (0.00, 0.00, 1.00), (0.05, 0.00, 1.00), (0.10, 0.00, 1.00), (0.15, 0.00, 1.00), (0.20, 0.00, 1.00),
        (0.25, 0.00, 1.00), (0.30, 0.00, 1.00), (0.35, 0.00, 1.00), (0.40, 0.00, 1.00), (0.45, 0.00, 1.00),
        (0.50, 0.00, 1.00), (0.55, 0.00, 1.00), (0.60, 0.00, 1.00), (0.65, 0.00, 1.00), (0.70, 0.00, 1.00),
        (0.75, 0.00, 1.00), (0.80, 0.00, 1.00), (0.85, 0.00, 1.00), (0.90, 0.00, 1.00), (0.95, 0.00, 1.00)
    ]

    while x < 1000:
        idx = int(c)
        color = colors[idx]
        turtle.color(color)
        turtle.forward(x)
        turtle.right(98)
        x = x + 1
        c = c + 0.1

    return 0

#instantiation of screen and turtle
s = turtle.getscreen()
t = turtle.Turtle()

turtle_race()

turtle.Screen().exitonclick()