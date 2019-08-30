# https://www.youtube.com/watch?v=1Lfv5tUGsn8

from math import pi

def circle_area(r):
    if type(r) not in [int, float]:
        raise TypeError("The radius must not be a non-negative real number.")
    if r<0:
        raise ValueError("The radius cannot be negative.")
    return pi*(r**2)