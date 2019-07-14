import turtle
from other_functions.common_functions import check_update


def car_map():
    turtle.speed(1000)
    turtle.setup(width=650, height=350, startx=400, starty=200)
    turtle.bgpic(r"D:\PycharmProjects\car\ui\map.png")
    turtle.color('red')
    turtle.goto(-200, -25)
    turtle.clear()

    positions = check_update(r'D:\PycharmProjects\car\ui\position.txt')
    for position in positions:
        turtle.forward(int(position.strip('\n')))
        turtle.clear()
    turtle.done()