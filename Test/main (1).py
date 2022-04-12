from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def drawline(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def DDA(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
    Xinc = dx / float(steps)
    Yinc = dy / float(steps)
    x = x1
    y = y1
    for i in range(steps):
        drawline(round(x), round(y))
        x += Xinc
        y += Yinc


def DDADashed(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
    Xinc = 4 * (dx / float(steps))
    Yinc = dy / float(steps)
    x = x1
    y = y1
    for i in range(int(steps / 4)):
        drawline(round(x), round(y))
        x += Xinc
        y += Yinc


def drawH():
    DDA(100, 200, 101, 400)
    DDA(200, 400, 300, 500)
    DDADashed(100, 301, 201, 301)




def myInit():
    glClearColor(255, 255, 0.0, 0.0)
    glPointSize(1.0)
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)


def display():
    drawH()
    glFlush()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
glutCreateWindow('Lab Task 03')
myInit()
glutDisplayFunc(display)
glutMainLoop()