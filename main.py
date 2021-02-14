from Project3d import *
from math import cos, sin

angle = 0

myPoints = [i for i in range(0, 16)]

myPoints[0] = [[-1], [-1], [1], [1]]
myPoints[1] = [[1], [-1], [1], [1]]
myPoints[2] = [[1], [1], [1], [1]]
myPoints[3] = [[-1], [1], [1], [1]]
myPoints[4] = [[-1], [-1], [-1], [1]]
myPoints[5] = [[1], [-1], [-1], [1]]
myPoints[6] = [[1], [1], [-1], [1]]
myPoints[7] = [[-1], [1], [-1], [1]]
myPoints[8] = [[-1], [-1], [1], [5]]
myPoints[9] = [[1], [-1], [1], [-1]]
myPoints[10] = [[1], [1], [1], [-1]]
myPoints[11] = [[-1], [1], [1], [-1]]
myPoints[12] = [[-1], [-1], [-1], [-1]]
myPoints[13] = [[1], [-1], [-1], [-1]]
myPoints[14] = [[1], [1], [-1], [-1]]
myPoints[15] = [[-1], [1], [-1], [-1]]

distance = 4

while True:
    tempPoints = []
    for point in myPoints:
        rotation_xy = [[cos(angle), -sin(angle), 0, 0],
                       [sin(angle), cos(angle), 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 1]]

        rotation_zw = [[1, 0, 0, 0],
                       [0, 1, 0, 0],
                       [0, 0, cos(angle), -sin(angle)],
                       [0, 0, sin(angle), cos(angle)]]

        w = (distance - point[3][0])
        projectionMatrix = [[w, 0, 0, 0],
                            [0, w, 0, 0],
                            [0, 0, w, 0]]

        rotated = matMult(rotation_xy, point)
        rotated = matMult(rotation_zw, rotated)
        tempPoints.append(matMult(projectionMatrix, rotated))

    set_point(tempPoints)
    set_distance(10)
    set_scale(300)
    clock.tick(60)
    draw()
    rotateX(90)
    angle += .01
