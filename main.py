import project4d, Project3d

project4d.use_Demo_tesseract()

angle = 0

run = True

while run:
    for event in Project3d.pygame.event.get():
        if event.type == Project3d.pygame.QUIT:
            run = False

    Project3d.clock.tick(60)
    project4d.set_angleXY(angle)
    Project3d.rotateZ(90)
    project4d.set_angleZW(angle)
    project4d.draw()
    angle += .01