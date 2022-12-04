from math import pi

def get_ball_volume(radius):
    if radius < 0:
        raise ValueError("Radius can't be negative")
    return 4/3*pi*radius**3

def get_ball_square(radius):
    if radius < 0:
        raise ValueError("Radius can't be negative")
    return 4*pi*radius**2

