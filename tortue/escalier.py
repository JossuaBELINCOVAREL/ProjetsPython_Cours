import turtle

def escalier(taille, nb):
    for i in range(0, taille):
        t.forward(nb)
        t.left(90)
        t.forward(nb)
        t.right(90)
        nb -= 10
    t.forward(nb)

t = turtle.Turtle()

escalier(5, 60)

turtle.done()