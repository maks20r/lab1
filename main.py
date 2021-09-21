import turtle
def test(radius ,pos_x, pos_y, color, fill_color):
    turtle.up()
    turtle.goto(pos_x, pos_y)
    turtle.down()
    turtle.color(color)
    turtle.fillcolor(fill_color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.done()

def main():
    test(100, 100, 100,"blue", "red")
    test(50, 100, 100, "green", "black")
    input('press')

main()

