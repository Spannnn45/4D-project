from matrix import *
import pygame
import math

pygame.init()
points = [[[1], [1], [1]]]
distance = 4
clock = pygame.time.Clock()

faces = []

projectedPoint = [i for i in range(0, 16)]

rotation_x = [[1, 0, 0],
              [0, math.cos(0), -math.sin(0)],
              [0, math.sin(0), math.cos(0)]]

rotation_y = [[math.cos(0), 0, -math.sin(0)],
              [0, 1, 0],
              [math.sin(0), 0, math.cos(0)]]

rotation_z = [[math.cos(0), -math.sin(0), 0],
              [math.sin(0), math.cos(0), 0],
              [0, 0, 1]]

black, white, blue = (20, 20, 20), (230, 230, 230), (0, 154, 255)

scale = 600

def set_point(point):
    global points
    points = point


def rotateX(angle):
    global rotation_x
    rotation_x = [[1, 0, 0],
                  [0, math.cos(angle), -math.sin(angle)],
                  [0, math.sin(angle), math.cos(angle)]]


def rotateY(angle):
    global rotation_y
    rotation_y = [[math.cos(angle), 0, -math.sin(angle)],
                  [0, 1, 0],
                  [math.sin(angle), 0, math.cos(angle)]]


def rotateZ(angle):
    global rotation_z
    rotation_z = [[math.cos(angle), -math.sin(angle), 0],
                  [math.sin(angle), math.cos(angle), 0],
                  [0, 0, 1]]

def set_distance(d):
    global distance
    distance = d

def set_scale(scales):
    global scale
    scale = scales

def set_faces(face):
    global faces
    faces = face

def connect(a, b):
    pygame.draw.line(display, black, (a[0][0] * scale + 1920 // 2, a[1][0] * scale + 1080 // 2), (b[0][0] * scale + 1920 // 2, b[1][0] * scale + 1080 // 2), 5)

pygame.display.set_caption("Well hello there")
display = pygame.display.set_mode((1920, 1080))

display.fill(white)

def draw():
    clock.tick(60)
    display.fill(white)
    for i in range(0, len(points)):
        rotated = matMult(rotation_x, points[i])
        rotated = matMult(rotation_y, rotated)
        rotated = matMult(rotation_z, rotated)

        projected = matMult([[1 / (distance - rotated[2][0]), 0, 0], [0, 1 / (distance - rotated[2][0]), 0]], rotated)
        projectedPoint[i] = projected
        pygame.draw.circle(display, blue, ((projected[0][0] * scale)+1920//2, (projected[1][0] * scale)+1080//2), 10)

    connect(projectedPoint[0], projectedPoint[1])
    connect(projectedPoint[1], projectedPoint[2])
    connect(projectedPoint[2], projectedPoint[3])
    connect(projectedPoint[3], projectedPoint[0])

    connect(projectedPoint[4], projectedPoint[5])
    connect(projectedPoint[5], projectedPoint[6])
    connect(projectedPoint[6], projectedPoint[7])
    connect(projectedPoint[7], projectedPoint[4])

    connect(projectedPoint[0], projectedPoint[4])
    connect(projectedPoint[1], projectedPoint[5])
    connect(projectedPoint[2], projectedPoint[6])
    connect(projectedPoint[3], projectedPoint[7])



    connect(projectedPoint[8], projectedPoint[9])
    connect(projectedPoint[9], projectedPoint[10])
    connect(projectedPoint[10], projectedPoint[11])
    connect(projectedPoint[11], projectedPoint[12])

    connect(projectedPoint[12], projectedPoint[13])
    connect(projectedPoint[13], projectedPoint[14])
    connect(projectedPoint[14], projectedPoint[15])
    connect(projectedPoint[15], projectedPoint[8])

    connect(projectedPoint[0], projectedPoint[4])
    connect(projectedPoint[1], projectedPoint[5])
    connect(projectedPoint[2], projectedPoint[6])
    connect(projectedPoint[3], projectedPoint[7])

    pygame.display.update()
