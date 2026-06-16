# --------------- My Solution ----------------------

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    move()
    turn_right()
   
def recenter():
    turn_right()
    move()
    turn_right()
    move()

while not at_goal():
    if wall_in_front() and wall_on_right():
        turn_left()
    if wall_in_front(): 
        jump()
        if front_is_clear():
            move()
            turn_right()
            move()
        if wall_on_right and wall_in_front():
            turn_left()
    elif wall_on_right() and not wall_in_front():
        move()
        if wall_in_front() and is_facing_north():
           recenter()
        elif wall_in_front():
            turn_left()
    elif not wall_in_front() and not wall_on_right():
        recenter()
    elif is_facing_north():
        recenter()


# ------------------ Dr. Anglea Yu Solution (More efficient) -----------------------

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    while wall_on_right():
        move()
        
    turn_right()
    move()
    turn_right()
    move()
    
    while front_is_clear():
        move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()