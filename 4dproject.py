import Project3d
from matrix import *
from math import cos, sin

myPoints = []

angleZW = 0
angleXY = 0

scale = 600

def set_scale(scales):
    global scale
    scale = scales

def set_points(points):
    global myPoints
    myPoints = points


def set_angleXY(angle):
    global angleXY
    angleXY = angle


def set_angleZW(angle):
    global angleZW
    angleZW = angle


def use_Demo_tesseract():
    myPoints = [i for i in range(0, 16)]

    myPoints[0] = [[-1], [-1], [1], [1]]
    myPoints[1] = [[1], [-1], [1], [1]]
    myPoints[2] = [[1], [1], [1], [1]]
    myPoints[3] = [[-1], [1], [1], [1]]
    myPoints[4] = [[-1], [-1], [-1], [1]]
    myPoints[5] = [[1], [-1], [-1], [1]]
    myPoints[6] = [[1], [1], [-1], [1]]
    myPoints[7] = [[-1], [1], [-1], [1]]
    myPoints[8] = [[-1], [-1], [1], [-1]]
    myPoints[9] = [[1], [-1], [1], [-1]]
    myPoints[10] = [[1], [1], [1], [-1]]
    myPoints[11] = [[-1], [1], [1], [-1]]
    myPoints[12] = [[-1], [-1], [-1], [-1]]
    myPoints[13] = [[1], [-1], [-1], [-1]]
    myPoints[14] = [[1], [1], [-1], [-1]]
    myPoints[15] = [[-1], [1], [-1], [-1]]


Project3d.set_distance(3)


def draw():
    tempPoints = []
    for point in myPoints:
        rotation_xy = [[cos(angleXY), -sin(angleXY), 0, 0],
                       [sin(angleXY), cos(angleXY), 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 1]]

        rotation_zw = [[1, 0, 0, 0],
                       [0, 1, 0, 0],
                       [0, 0, cos(angleZW), -sin(angleZW)],
                       [0, 0, sin(angleZW), cos(angleZW)]]

        rotated = point
        rotated = matMult(rotation_xy, rotated)
        rotated = matMult(rotation_zw, rotated)

        w = 1
        w = w / (Project3d.distance - rotated[3][0])
        projectionMatrix = [[w, 0, 0, 0],
                            [0, w, 0, 0],
                            [0, 0, w, 0]]

        tempPoints.append(matMult(projectionMatrix, rotated))

    set_point(tempPoints)
    set_scale(scale)
    clock.tick(60)
    rotateY(90)
    draw()
