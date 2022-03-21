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
    x = x1
    y = y1

    if abs(dx) > abs(dy):
       steps = abs(dx)
    else:
        steps = abs(dy)
    Xinc = dx / float(steps)
    Yinc = dy / float(steps)

    for i in range(steps):
        drawline(round(x), round(y))
        x += Xinc
        y += Yinc


def DDADashed(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    x = x1
    y = y1

    if abs(dx) > abs(dy):
       steps = abs(dx)
    else:
        steps = abs(dy)
    Xinc = 4 * (dx / float(steps))
    Yinc = dy / float(steps)
    for i in range(int(steps / 4)):
        drawline(round(x), round(y))
        x += Xinc
        y += Yinc


def drawH():
    DDA(100, 200, 101, 400)
    DDA(200, 400, 201, 200)
    DDADashed(100, 301, 201, 301)


def drawT():
    DDA(250, 300, 250, 200)
    DDADashed(200, 300, 300, 300)


def iterate():
    glClearColor(255, 255, 0.0, 0.0)
    glPointSize(1.0)
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)


def display():
    student_id = str(input('Please enter the last 2 digits of your student id: '))
    if int(student_id[-1]) % 2 == 0:
        drawT()
    else:
        drawH()

    glFlush()




glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(700, 700)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("Lab01_Task03_19101077")
iterate()
glutDisplayFunc(display)
glutMainLoop()
