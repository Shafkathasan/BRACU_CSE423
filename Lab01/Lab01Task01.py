import random
from OpenGL.GL import *
from OpenGL.GLUT import *


def draw_point(x, y):
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def helper_func():
    for _ in range(50):
        var = [draw_point(random.randint(1, 500), random.randint(0, 500))]


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def show_screen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0.0, 3.0)

    """This is the beginning of task 1"""
    helper_func()
    '''Task 1 end'''

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGB)
glutInitWindowSize(600, 600)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("Lab01_Task01_19101077")
glutDisplayFunc(show_screen)
glutMainLoop()
