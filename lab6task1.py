class point():
    x = 0
    y = 0
point1 = point()
point2 = point()
point1.x = 1
point1.y = 2
point2.x = 3
point2.y = 4
import math
def distance_between_points(point1, point2):
    distance = math.sqrt((point2.x - point1.x) **2 +
                         (point2.y - point1.y)**2)
    return distance
print (distance_between_points(point1, point2))
