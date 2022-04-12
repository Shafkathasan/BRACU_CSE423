from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


"""These methods are for task 2"""


def draw_squares(x, y):
    glBegin(GL_LINES)
    glVertex2f(x, y + 100)
    glVertex2f(x + 100, y + 100)
    glVertex2f(x + 100, y + 100)
    glVertex2f(x + 100, y + 200)
    glVertex2f(x, y + 100)
    glVertex2f(x, y + 200)
    glVertex2f(x, y + 200)
    glVertex2f(x + 100, y + 200)
    glEnd()


def draw_big_box():
    glBegin(GL_LINES)
    glVertex2f(50, 50)
    glVertex2f(450, 50)
    glVertex2f(50, 50)
    glVertex2f(50, 450)
    glVertex2f(450, 50)
    glVertex2f(450, 450)
    glEnd()


def draw_door_knobs():
    glPointSize(10)
    glBegin(GL_POINTS)
    glVertex2f(150, 350)
    glVertex2f(350, 350)
    glEnd()


def draw_door():
    glBegin(GL_LINES)
    glVertex2f(150, 50)
    glVertex2f(150, 200)
    glVertex2f(350, 50)
    glVertex2f(350, 200)
    glVertex2f(150, 200)
    glVertex2f(350, 200)
    glEnd()


def draw_triangle():
    glBegin(GL_TRIANGLES)
    glVertex2f(50, 450)  # The left point
    glVertex2f(450, 450)  # The right point
    glVertex2f(250, 650)  # The middle point
    glEnd()


"""Task 2 end"""


def iterate():
    glViewport(0, 0, 1000, 1000)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1000, 0.0, 1000, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def show_screen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0.0, 3.0)

    """This is the begining of task 2"""
    draw_triangle()
    draw_squares(100, 200)
    draw_squares(300, 200)
    draw_big_box()
    draw_door()
    draw_door_knobs()
    '''Task 2 end'''

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(700, 700)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("Lab01_Task02_19101077")
glutDisplayFunc(show_screen)
glutIdleFunc(show_screen)
glutMainLoop()
