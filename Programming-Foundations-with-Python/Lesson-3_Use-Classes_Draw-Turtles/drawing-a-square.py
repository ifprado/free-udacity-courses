import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")
    
    brad = turtle.Turtle()

    sides = 27    
    angle = 360 // sides
    multiple = 4

    brad.speed(100*multiple * sides)

    
    for j in range(multiple*(360//angle)):
        for i in range(360//angle):
            brad.forward((angle*100)//90)
            brad.right(angle)
        brad.right(angle//multiple)

    window.exitonclick()
    
draw_square()
