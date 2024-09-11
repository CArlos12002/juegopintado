from turtle import *
from freegames import vector

def line(start, end):
    """Draw line from start to end."""
    width(state['width'])
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """Draw square from start to end."""
    width(state['width'])
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle_shape(start, end):
    """Draw circle from start to end."""
    width(state['width'])
    up()
    goto(start.x, start.y - (end.x - start.x) / 2)  # Adjust position to center
    down()
    begin_fill()
    circle((end.x - start.x) / 2)  # Radius is half the distance from start to end
    end_fill()


def rectangle(start, end):
    """Draw rectangle from start to end."""
    width(state['width'])
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(2):
        forward(end.x - start.x)
        left(90)
        forward(end.y - start.y)
        left(90)

    end_fill()


def triangle(start, end):
    """Draw triangle from start to end."""
    width(state['width'])
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for _ in range(3):
        forward(end.x - start.x)
        left(120)

    end_fill()


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value


state = {'start': None, 'shape': line, 'width': 2}  # Default width set to 2
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle_shape), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
onkey(lambda: store('width', 1), '1')  # Set line width to 1
onkey(lambda: store('width', 2), '2')  # Set line width to 2
onkey(lambda: store('width', 5), '5')  # Set line width to 5
onkey(lambda: store('width', 10), '0')  # Set line width to 10
done()