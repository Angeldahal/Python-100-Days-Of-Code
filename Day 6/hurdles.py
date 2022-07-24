def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    n=0
    while True:
        move()
        n+=1
        if right_is_clear():
            move()
    for i in range(1,n+1)
        turn_left()
        move()
        
while not at_goal():
    if front_is_clear():
        move()
    if wall_in_front():
        jump()