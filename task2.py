import turtle
def tree(step,len,t):
    if step > 5:
        t.forward(step)
        t.right(45)
        tree(step-len,len, t)
        t.left(90)
        tree(step-len,len, t)
        t.right(45)
        t.backward(step)

def drawtree(level):

    t = turtle.Turtle()
    mytree = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("firebrick")
    t.width(2)
    t.speed(0)

    len  = 10
    step = level*len

    tree(step,len, t)
    mytree.exitonclick()
drawtree(8) 