import turtle


def koch_turns(n):
    route = []
    for i in range(n):
        for j in range(4**i):
            route.insert(j*4, 60)
            route.insert(j*4, -120)
            route.insert(j*4, 60)
    return route

def turtle_koch(n, line_lenght=10):
    turtle.setx(-500)
    turtle.setx(-500)
    turtle.clear()
    for move in koch_turns(n):
        turtle.forward(line_lenght)
        turtle.left(move)
    turtle.forward(line_lenght)


n = int(input(n))
#print(koch_turns(n))
turtle_koch(n)
turtle.mainloop()
