from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def MidpointCircle(radius, x0, y0):
    d = 1 - radius
    x = 0
    y = radius

    Circlepoints(x, y, x0 ,y0)
    while (x < y):
        if (d < 0):
            #choose E
            d = d + 2*x + 3
            x = x + 1
        else:
            # choose SE
            d = d + 2*x - 2*y + 5
            x = x + 1
            y = y - 1

        Circlepoints(x, y, x0, y0)

def Circlepoints(x, y, x0, y0):

    draw_points(x + x0, y + y0)
    draw_points(y + y0, x + x0)
    draw_points(y + y0, -x + x0)
    draw_points(x + x0, -y + y0)
    draw_points(-x + x0, -y + y0)
    draw_points(-y + y0, -x + x0)
    draw_points(-y + y0, x + x0)
    draw_points(-x + x0, y + y0)


def draw_points(x, y):
    glPointSize(3) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 0.0) #konokichur color set (RGB)
    #call the draw methods here
    x = 250
    y = 250
    radius = 150
    MidpointCircle(radius, x, y)
    MidpointCircle(radius / 2, x + 53, y + 53)
    MidpointCircle(radius / 2, x - 53, y - 53)
    MidpointCircle(radius / 2, x + 53, y - 53)
    MidpointCircle(radius / 2, x - 53, y + 53)

    MidpointCircle(radius / 2, x + 75, y )
    MidpointCircle(radius / 2, x - 75, y )
    MidpointCircle(radius / 2, x, y - 75)
    MidpointCircle(radius / 2, x, y + 75)

    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(700, 700) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)

glutMainLoop()