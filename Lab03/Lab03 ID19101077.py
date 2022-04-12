from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def MidpointCircle(r, x0, y0):
    d = 1 - r
    x = 0
    y = r

    d = dy - dx
    x,y= x0,y0

    glBegin(GL_POINTS)
    glVertex2f(x, y)
    # iterate through value of y
    while (x < y):
        if (d < 0):
            #choose E
            d = d + 2*x + 3
            x = x + 1
        else:
            # choose SE
            d = d + 2*x - 2*y + 3
            y = y - 1

        glVertex2f(x,y)
    glEnd()

def draw_points(x, y):
    glPointSize(5) #pixel size. by default 1 thake
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
    draw_points(250, 250)
    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(700, 700) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)

glutMainLoop()