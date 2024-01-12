import math

def cone_droit_volume(r, h):
    volume = round(((1/3) * math.pi * r**2 * h), 2)
    print(volume)
    return volume

cone_droit_volume(4, 5)