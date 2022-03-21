from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def init():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

# method for horizontal lines
def midPoint(x1, y1, x2, y2):
    # calculate dx & dy
    dx = x2 - x1
    dy = y2 - y1
    # initial value of decision parameter d
    d = dy - dx
    x,y = x1,y1

    glBegin(GL_POINTS)
    glVertex2f(x,y)
    # iterate through value of X
    while (x < x2):
        x = x + 1
        if (d < 0):
            d = d + dy
        else:
            d = d + (dy - dx)
            y = y + 1

        glVertex2f(x,y)
    glEnd()

# method for vertical lines
def midPoint2(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    d = dy - dx
    x,y= x1,y1

    glBegin(GL_POINTS)
    glVertex2f(x, y)
    # iterate through value of y
    while (y < y2):
        if (d < 0):
            d = d + dy
        else:
            d = d + (dy - dx)
            y = y + 1

        glVertex2f(x,y)
    glEnd()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    #call the draw methods here
    draw()

    glutSwapBuffers()

# put your drawing codes inside this 'draw' function
def draw():
    glColor3d(0,1,0)

    # line calls for printing 7
    midPoint2(250, 25, 100, 150)
    midPoint2(250,150,250,300)
    midPoint(100,300,250,300)

    # line calls for printing 7
    midPoint2(450, 150, 250, 300)
    midPoint2(450, 25, 100, 150)
    midPoint(300,300,450,300)

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
glutCreateWindow(b"Student ID: 19101077, Let's Draw 77")
glutDisplayFunc(showScreen)

init()

glutMainLoop()