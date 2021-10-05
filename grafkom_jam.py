from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

x = 1000
y = 1000


def main():
    glBegin(GL_POLYGON)
    glColor3ub(252, 123, 3)
    glVertex2f(2, 13.23)
    glVertex2f(2, 15)
    glVertex2f(3, 16)
    glVertex2f(5, 16)
    glVertex2f(6, 15)
    glVertex2f(6, 13.23)
    glVertex2f(6, 8.78)
    glVertex2f(6, 3)
    glVertex2f(5, 2)
    glVertex2f(4.5, 2)
    glVertex2f(4, 1.5)
    glVertex2f(4, 1.5)
    glVertex2f(3.5, 2)
    glVertex2f(3, 2)
    glVertex2f(2, 3)
    glVertex2f(2, 8.78)
    glVertex2f(4.5, 2)
    glEnd()
    
    
def tail():
    glBegin(GL_POLYGON)
    glColor3ub(255, 243, 232)
    glVertex2f(3.9, 8)
    glVertex2f(4.1, 8)
    glVertex2f(4.1, 4.5)
    glVertex2f(3.9, 4.5)
    glEnd()
    
def iterate():
    glViewport(100, 100, 1200, 1200) # untuk mengatur area pandang
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 50, 0.0, 50, 0.0, 1.0) # untuk mengatur berapa blok yang digunakan (skala) nilai x, y, z
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # to clean the screen
    glLoadIdentity()
    iterate()
    main()
    tail()
    glutSwapBuffers() # untuk membersihkan layar, double buffering


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
name = glutCreateWindow("JAM")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()