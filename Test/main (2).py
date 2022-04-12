from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def myInit():
    glClearColor(255, 255, 0.0, 0.0)
    glPointSize(5.0)
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)


def display():
    glBegin(GL_TRIANGLES)
    glVertex2f(10.0, 300.0)
    glVertex2f(200.0, 300.0)
    glVertex2f(105.0, 400.0)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(10.0, 300.0)
    glVertex2f(10.0, 50.0)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(200.0, 300.0)
    glVertex2f(200.0, 50.0)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(10.0, 50.0)
    glVertex2f(200.0, 50.0)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(190.0, 290.0)
    glVertex2f(190.0, 230.0)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(190.0, 290.0)
    glVertex2f(130.0, 290.0)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(130.0, 290.0)
    glVertex2f(130.0, 230.0)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(130.0, 230.0)
    glVertex2f(190.0, 230.0)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(20.0, 290.0)
    glVertex2f(20.0, 230.0)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(20.0, 230.0)
    glVertex2f(80.0, 230.0)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(80.0, 230.0)
    glVertex2f(80.0, 290.0)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(20.0, 290.0)
    glVertex2f(80.0, 290.0)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(75.0, 50.0)
    glVertex2f(75.0, 150.0)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(140.0, 50.0)
    glVertex2f(140.0, 150.0)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(140.0, 150.0)
    glVertex2f(75.0, 150.0)
    glEnd()
    glBegin(GL_POINTS)
    glVertex2f(10.0, 100.0)
    glEnd()

    glFlush()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
glutCreateWindow('Lab Task 02')
myInit()
glutDisplayFunc(display)
glutMainLoop()