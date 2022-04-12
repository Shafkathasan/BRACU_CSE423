from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random



xArr = []*5
yArr = []*5
for i in range(50):
    xArr.append(random.randint(0, 500))
    yArr.append(random.randint(0, 500))



def drawPoints50():
    glPointSize(5)
    glBegin(GL_POINTS)
    for i in range(50):
        glVertex2f(int(xArr[i]), int(yArr[i]))
    glEnd()


def drawLines():

    glBegin(GL_LINES)
    glVertex2f(200,250)
    glVertex2f(250, 250)
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
    glColor3f(1.0, 0.0, 3.0)
    #call the draw methods here
    drawPoints50()

    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()