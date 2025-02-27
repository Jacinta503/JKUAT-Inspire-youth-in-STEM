# Formula to get the volumeof a cylinder
#V+ PIR2H
import math
def cylinder_volume(radius, height):
    return math.pi * radius ** 2 * height

radius = int(input("Enter the radius of the cylinder: "))
height = int(input("Enter the height of the cylinder: "))
print(cylinder_volume(radius, height ))