import math
def volume(radius,height):
    return math.pi*radius**2*height

radius=int(input('Enter the radius of the cylinder'))
height=int(input('Enter the height of the cylinder'))
print(f'volume of cylinder is: {volume(radius,height):.2f}')