import turtle
turtle.Screen().bgcolor("red")
turtle.Screen().setup(300,400)
polygon = turtle.Turtle()
num_sides = 6
side_legth = 90
angle = 360.0 / num_sides
for i in range(num_sides):
    polygon.forward(side_legth)
    polygon.right(angle)
turtle.done()