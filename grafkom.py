from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

x = 1000
y = 1000

def pointsleft():
    glPointSize(10)
    glBegin(GL_POINTS)
    glColor3ub(34, 227, 169)
    glVertex2f(8, 18)
    glVertex2f(9, 17)
    glVertex2f(10, 16)
    glVertex2f(11, 15)
    glVertex2f(12, 14)
    glVertex2f(13, 13)
    glEnd()

def pointrights():
    glPointSize(10)
    glBegin(GL_POINTS)
    glColor3ub(34, 227, 169)
    glVertex2f(18, 13)
    glVertex2f(19, 14)
    glVertex2f(20, 15)
    glVertex2f(21, 16)
    glVertex2f(22, 17)
    glVertex2f(23, 18)
    glEnd()

def iterate():
    glViewport(100, 100, 1000, 1000) # untuk mengatur area pandang
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 100, 0.0, 100, 0.0, 1.0) # untuk mengatur berapa blok yang digunakan (skala) nilai x, y, z
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # to clean the screen
    glLoadIdentity()
    iterate()
    pointsleft()
    pointrights()
    glutSwapBuffers() # untuk membersihkan layar, double buffering

glutInit()
glutInitDisplayMode(GLUT_RGBA) # untuk mengatur display supaya berwarna
glutInitWindowSize(500, 500) # untuk mengatur ukuran window
glutInitWindowPosition(0, 0) # untuk mengatur letak window
wind = glutCreateWindow("Point and Lines") # untuk memberi nama pada window
glutDisplayFunc(showScreen) # untuk fungsi callback
glutIdleFunc(showScreen) # untuk fungsi callback
glutMainLoop() # fungsi yang akan memulai keseluruhan program
