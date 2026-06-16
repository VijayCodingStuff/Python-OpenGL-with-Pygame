import pygame 
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()
display = (800, 800)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
gluPerspective(45, (display[0] / display[1]), 0.1, 50)

glTranslate(0, 0, -5)
cube_rotation = 0

run = True

glEnable(GL_DEPTH_TEST)

point_place = (
    (1, 1, 1), #0
    (-1, 1, 1), #1
    (-1, -1, 1), #2
    (1, -1, 1), #3
    (1, 1, -1), #4
    (-1, 1, -1), #5
    (-1, -1, -1), #6
    (1, -1, -1) #7
)

place = (
    (0, 1, 2, 3),
    (4, 5, 6, 7),
    (1, 2, 6, 5),
    (0, 3, 7, 4),
    (0, 1, 5, 4),
    (3, 7, 6, 2)
)

def render() :
    glBegin(GL_QUADS)
    for points in place :
        for point in points :
            glColor3fv(point_place[point])
            glVertex3fv(point_place[point])
    glEnd()

while run :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            run = False

    glClear(GL_DEPTH_BUFFER_BIT | GL_COLOR_BUFFER_BIT)

    glPushMatrix()

    cube_rotation += 0.9
    glRotate(cube_rotation, 0.3, 0.2, 0.1)
    render()

    glPopMatrix()

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
quit()