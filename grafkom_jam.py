from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *

x = 1000
y = 1000


def main():
    r,b,g = 42, 173, 167
    glBegin(GL_POLYGON)
    for i in range(100):
        glColor3ub(r+i,g*i,b**i)
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
    x1,x2,x3 = 3.9,4.1,4
    r,b,g = 255, 162, 0
    glBegin(GL_POLYGON)
    glColor3ub(r,b,g)
    glVertex2f(x1, 8)
    glVertex2f(x2, 8)
    glVertex2f(x2, 4.5)
    glVertex2f(x1, 4.5)
    glEnd()
    Circle_polygon(x3, 4, 0.5, 100, r,b,g)

def Circle_polygon(x_pos, y_pos, radius, sides,r,g,b): # membuat fungsi lingkaran         
    glBegin(GL_POLYGON)
    glColor3ub(r,g,b)
    for i in range(100):#perhitungan sin dan cos dari sudut lingkaran
        cosine= radius * cos(i*2*pi/sides) + x_pos  
        sine  = radius * sin(i*2*pi/sides) + y_pos   
        glVertex2f(cosine,sine)
    glEnd()

def titik():
    glPointSize(10)
    glBegin(GL_POINTS)
    glColor3ub(255, 17, 0) 
    glVertex2f(4,14)
    glVertex2f(5.57, 13.56)
    glVertex2f(6.68, 12.35)
    glVertex2f(7,11)
    glVertex2f(6.65, 9.59)
    glVertex2f(5.58, 8.45)
    glVertex2f(4, 8)
    glVertex2f(2.44, 8.44)
    glVertex2f(1.35, 9.6)
    glVertex2f(1, 11)
    glVertex2f(1.34, 12.39)
    glVertex2f(2.43, 13.56)
    glVertex2f(4, 14)
    glVertex2f(4, 11)
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
    Circle_polygon(4, 11, 3, 100, 242, 179, 70  )
    tail()
    glutSwapBuffers() # untuk membersihkan layar, double buffering

glutInit()
glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
name = glutCreateWindow("JAM")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()
