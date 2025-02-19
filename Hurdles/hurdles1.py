def turn_right():
    turn_left()
    move()
def turn_square():
    turn_left()
    turn_left()
    turn_left()
    move()
def turn_square1():
    turn_right()
    turn_square()
    turn_square()
move()
for i in range(5):
    turn_right()
    turn_square()
    turn_square()
    turn_right()
turn_square1()