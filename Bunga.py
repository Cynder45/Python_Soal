import turtle
turtle.speed(0)
turtle.hideturtle()
turtle.bgcolor("black")
turtle.pencolor("white")
t = turtle.Turtle()
colors = ["white","blue"]
for i in range(100):
    turtle.circle(50 + i )
    turtle.circle(-50 - i )
    turtle.forward( 1 )
    turtle.right(90)
    turtle.write("Appreciate everything", align='center')
turtle.done() 