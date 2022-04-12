from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

def midpointLine(x1, y1, x2, y2):
    glBegin(GL_POINTS)
    dy = y2-y1
    dx = x2-x1

    d_init = (2*dy) - dx
    d = d_init

    if x1 == x2:
        while(y1 != y2):
            glVertex2f(x1, y1)
            y1 += 1
        glVertex2f(x1, y1)
    elif y1 == y2:
        while(x1 != x2):
            glVertex2f(x1, y1)
            x1 += 1
        glVertex2f(x1, y1)
    else:
        while(x1 != x2 and y1 != y2):
            glVertex2f(x1, y1)
            if d > 0:
                x1 += 1
                y1 += 1
                d += 2(dy - dx)
            else:
                x1 += 1
                d += 2*dy
        glVertex2f(x1, y1)
    glEnd()

def digit():
    midpointLine(400, 450, 500, 450)
    midpointLine(400, 350, 500, 350)
    midpointLine(400, 250, 500, 250)
    midpointLine(500, 350, 500, 450)
    midpointLine(500, 250, 500, 350)





def iterate():
    glViewport(0, 0, 700, 700)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 700, 0.0, 700, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(0, 10, 10)
    glPointSize(8)
    digit()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(800, 750)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("Task-1 ; ID- 19101333")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()