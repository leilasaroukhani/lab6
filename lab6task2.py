class point():
    x = 0
    y = 0
point1 = point()
#point2 = point()

point1.x = 1
point1.y = 2
class Rectangle():
    width = 0
    height = 0
    corner = point()

draw = Rectangle()
draw.width = 100
draw.height = 200
draw.corner = point1
draw.corner.x = 1
draw.corner.y = 2
def find_centre (rect):
    p = point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height/2
    return p
print (find_centre(draw))
