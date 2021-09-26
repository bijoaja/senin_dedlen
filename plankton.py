from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

x = 1000
y = 1000

def pointsleft():
    glPointSize(5)
    glBegin(GL_POINTS)
    glColor3ub(34, 227, 169)
    glVertex2f(10, 18)
    glVertex2f(9.5, 18.5)
    glVertex2f(9, 19)
    glVertex2f(8.5, 19.5)
    glVertex2f(8, 20)
    glVertex2f(7.5, 20.5)
    glEnd()

def pointrights():
    glPointSize(5)
    glBegin(GL_POINTS)
    glColor3ub(34, 227, 169)
    glVertex2f(14, 18)
    glVertex2f(14.5, 18.5)
    glVertex2f(15, 19)
    glVertex2f(15.5, 19.5)
    glVertex2f(16, 20)
    glVertex2f(16.5, 20.5)
    glEnd()

def badan():
    glBegin(GL_POLYGON)
    glColor3ub(34, 227, 169)
    glVertex2f(10, 18)
    glVertex2f(8, 16)
    glVertex2f(8, 8)
    glVertex2f(10,6)
    glVertex2f(14,6)
    glVertex2f(16, 8)
    glVertex2f(16,16)
    glVertex2f(14,18)
    glEnd()
    
# MATA
def bolamata():
    glBegin(GL_QUADS)
    glColor3ub(252, 102, 3)
    glVertex2f(9, 9)
    glVertex2f(11, 9) 
    glVertex2f(11, 11) 
    glVertex2f(9, 11) 
    glEnd()

def retina():
    glBegin(GL_QUADS)
    glColor3ub(34, 227, 169)
    glVertex2f(8, 8) 
    glVertex2f(12, 8) 
    glVertex2f(12, 12)
    glVertex2f(8, 12)
    glEnd()

def RL_kelopak_mata():
    glBegin(GL_QUADS)
    glColor3ub(112, 30, 2)
    glVertex2f(7, 8) 
    glVertex2f(13, 8) 
    glVertex2f(13, 12) 
    glVertex2f(7, 12)
    glEnd()

def TB_kelopak_mata():
    glBegin(GL_QUADS)
    glColor3ub(112, 30, 2)
    glVertex2f(8, 7) 
    glVertex2f(12, 7) 
    glVertex2f(12, 14) 
    glVertex2f(8, 14) 
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
    badan()
    glutSwapBuffers() # untuk membersihkan layar, double buffering

glutInit()
glutInitDisplayMode(GLUT_RGBA) # untuk mengatur display supaya berwarna
glutInitWindowSize(500, 500) # untuk mengatur ukuran window
glutInitWindowPosition(0, 0) # untuk mengatur letak window
wind = glutCreateWindow("Point and Lines") # untuk memberi nama pada window
glutDisplayFunc(showScreen) # untuk fungsi callback
glutIdleFunc(showScreen) # untuk fungsi callback
glutMainLoop() # fungsi yang akan memulai keseluruhan program
