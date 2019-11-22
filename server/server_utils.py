from random import randint


def car_door():
    return str(randint(0, 2))


def get_solution(p_door,pc_door,change):
    if change=='s':
        return str(3 - int(p_door) - int(first_choice(p_door,pc_door)))
    else:
        return str(p_door)


def first_choice(p_door,pc_door):
    """
    returns a door with a goat
    """
    if p_door==pc_door:
        return str((int(p_door) +1)%3)
    return str(3 - int(p_door) - int(pc_door))