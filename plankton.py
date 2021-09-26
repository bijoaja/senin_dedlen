from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

x = 200
y = 200

def points():
    glPointSize(10)
    glBegin(GL_POINTS)
    glColor3ub(34, 227, 169)
    glVertex2f(8, 18)
    glVertex2f(18, 9)
    glEnd()

def iterate():
    glViewport(200, 200, 200, 200) # untuk mengatur area pandang
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 200, 0.0, 200, 0.0, 1.0) # untuk mengatur berapa blok yang digunakan (skala) nilai x, y, z
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # to clean the screen
    glLoadIdentity()
    iterate()
    points()
    glutSwapBuffers() # untuk membersihkan layar, double buffering

glutInit()
glutInitDisplayMode(GLUT_RGBA) # untuk mengatur display supaya berwarna
glutInitWindowSize(500, 500) # untuk mengatur ukuran window
glutInitWindowPosition(0, 0) # untuk mengatur letak window
wind = glutCreateWindow("Point and Lines") # untuk memberi nama pada window
glutDisplayFunc(showScreen) # untuk fungsi callback
glutIdleFunc(showScreen) # untuk fungsi callback
glutMainLoop() # fungsi yang akan memulai keseluruhan program