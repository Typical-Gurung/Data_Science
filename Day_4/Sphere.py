import math
def volume_of_sphere(radius_of_sphere):
    return math.pi*radius_of_sphere**3*(4/3)
def volume_of_hemisphere(radius_of_hemisphere):
    return math.pi*radius_of_hemisphere**3*(2/3)



radius_of_sphere=float(input('Enter the radius of sphere'))
radius_of_hemisphere=float(input('Enter the radius of sphere'))

volumeofsphere=volume_of_sphere(radius_of_sphere)
volumeofhemisphere=volume_of_hemisphere(radius_of_hemisphere)
Total=volumeofsphere+volumeofhemisphere
print(f'The total volume of sphere and hemisphere is {Total:.2f}')