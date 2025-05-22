import math

def volume_cylinder(radius,height_cylinder):
    return math.pi*radius**2*height_cylinder

def volume_cone(radius,height_cone):
    return (math.pi*radius**2*height_cone)/3


radius=float(input('enter the radius of the diagram'))

height_cylinder=float(input('enter the height of the cylinder'))

height_cone=float(input('enter the height of the cone'))


volumeofcylinder=volume_cylinder(radius,height_cylinder)
volumeofcone=volume_cone(radius,height_cone)
totalvolume=volumeofcylinder+volumeofcone

print(f'The total volume of the combined solids are: {totalvolume}')