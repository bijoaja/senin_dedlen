from OpenGL.GL import *
from OpenGL.GL.glget import GLsize
from OpenGL.GLUT import *
from OpenGL.GLU import *

x = 1000
y = 1000

#antena
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

# BADAN
def badan():
    glBegin(GL_POLYGON)
    glColor3ub(34, 227, 169)
    glVertex2f(10, 18.5)
    glVertex2f(8, 16)
    glVertex2f(8, 8)
    glVertex2f(10,6.5)
    glVertex2f(14,6.5)
    glVertex2f(16, 8)
    glVertex2f(16,16)
    glVertex2f(14,18.5)
    glEnd()

# MATA
def bolamata():
    glPointSize(25)
    glBegin(GL_POINTS)
    glColor3ub(250, 112, 0)
    glVertex2f(12,14.5)
    glEnd()

def retina():
    glPointSize(50)
    glBegin(GL_POINTS)
    glColor3ub(247, 225, 99)
    glVertex2f(12,14.5)
    glEnd()

def TB_kelopak_mata():
    glBegin(GL_QUADS)
    glColor3ub(0, 0, 0)
    glVertex2f(10.5, 12.5) 
    glVertex2f(13.5, 12.5) 
    glVertex2f(13.5, 17) 
    glVertex2f(10.5, 17) 
    glEnd()

def RL_kelopak_mata():
    glBegin(GL_QUADS)
    glColor3ub(0, 0, 0)
    glVertex2f(10, 13) 
    glVertex2f(14, 13) 
    glVertex2f(14, 16) 
    glVertex2f(10, 16)
    glEnd()

#TANGAN kiri
def L_tangan():
    glColor3ub(56, 168, 50)
    glBegin(GL_LINES)
    glVertex2f(8, 12)
    glVertex2f(5.5,14)
    glEnd()
def L_lengan():
    glColor3ub(56, 168, 50)
    glBegin(GL_LINES)
    glVertex2f(5.5,14)
    glVertex2f(5.7,17)
    glEnd()
def tlpk_L_tangan():
    glPointSize(14)
    glBegin(GL_POINTS)
    glColor3ub(56, 168, 50)
    glVertex2f(5.7,17)
    glEnd()

#TANGAN kanan
def R_tangan():
    glColor3ub(56, 168, 50)
    glBegin(GL_LINES)
    glVertex2f(16, 12)
    glVertex2f(18.5,14)
    glEnd()
def R_lengan():
    glColor3ub(56, 168, 50)
    glBegin(GL_LINES)
    glVertex2f(18.5,14)
    glVertex2f(18.7,17)
    glEnd()
def tlpk_R_tangan():
    glPointSize(14)
    glBegin(GL_POINTS)
    glColor3ub(56, 168, 50)
    glVertex2f(18.7,17)
    glEnd()

#MULUT
def bibir():
    glBegin(GL_QUADS)
    glColor3ub(0, 0, 0)
    glVertex2f(9.5, 11.3) 
    glVertex2f(14.5, 11.3) 
    glVertex2f(14.5, 8.5) 
    glVertex2f(9.5, 8.5)
    glEnd()
def bibir2():
    glBegin(GL_QUADS)
    glColor3ub(0, 0, 0)
    glVertex2f(10,10.2)
    glVertex2f(14,10.2)
    glVertex2f(14,9.8)
    glVertex2f(10,9.8)
    glEnd()

def bibir3():
    glBegin(GL_QUADS)
    glColor3ub(0, 0, 0)
    glVertex2f(10.5,9.2)
    glVertex2f(13.5,9.2)
    glVertex2f(13.5,8.8)
    glVertex2f(10.5,8.8)
    glEnd()

def bibir4():
    glBegin(GL_QUADS)
    glColor3ub(0, 0, 0)
    glVertex2f(10.5,8.1)
    glVertex2f(13.5,8.1)
    glVertex2f(13.5,7.8)
    glVertex2f(10.5,7.8)
    glEnd()

def bibir5():
    glColor3ub(0, 0, 0)
    glPointSize(10)
    glBegin(GL_POINTS)
    glVertex2f(10.2, 8.5)
    glEnd()

def bibir6():
    glColor3ub(0, 0, 0)
    glPointSize(10)
    glBegin(GL_POINTS)
    glVertex2f(13.8, 8.5)
    glEnd()

def gigi():
    glBegin(GL_QUADS)
    glColor3ub(255, 255, 255)
    glVertex2f(10, 10)
    glVertex2f(14, 10)
    glVertex2f(14, 11)
    glVertex2f(10, 11)
    glEnd()

def mulut():
    glBegin(GL_POLYGON)
    glColor3ub(255, 18, 18)
    glVertex2f(10, 8.5)
    glVertex2f(10, 10)
    glVertex2f(14, 10)
    glVertex2f(14, 8.5)
    glVertex2f(13.5, 8)
    glVertex2f(10.5, 8)
    glEnd()

def lidah():
    glBegin(GL_POLYGON)
    glColor3ub(209, 84, 84)
    glVertex2f(10, 8.5)
    glVertex2f(10.5, 9)
    glVertex2f(13.5, 9)
    glVertex2f(14, 8.5)
    glVertex2f(13.5, 8)
    glVertex2f(10.5, 8)
    glEnd()

def iterate():
    glViewport(100, 100, 1000, 1000) # untuk mengatur area pandang
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 60, 0.0, 60, 0.0, 1.0) # untuk mengatur berapa blok yang digunakan (skala) nilai x, y, z
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # to clean the screen
    glLoadIdentity()
    iterate()
    #BADAN DAN ANTENA
    pointsleft()
    pointrights()
    badan()
    #MATA
    TB_kelopak_mata()
    RL_kelopak_mata()
    retina()
    bolamata()
    #TANGAN
    L_tangan()
    tlpk_L_tangan()
    L_lengan()
    R_tangan()
    tlpk_R_tangan()
    R_lengan()
    # MULUT
    bibir()
    gigi()
    mulut()
    lidah()
    bibir2()
    bibir3()
    bibir4()
    bibir5()
    bibir6()
    glutSwapBuffers() # untuk membersihkan layar, double buffering

glutInit()
glutInitDisplayMode(GLUT_RGBA) # untuk mengatur display supaya berwarna
glutInitWindowSize(500, 500) # untuk mengatur ukuran window
glutInitWindowPosition(0, 0) # untuk mengatur letak window
wind = glutCreateWindow("PLANKTON") # untuk memberi nama pada window
glutDisplayFunc(showScreen) # untuk fungsi callback
glutIdleFunc(showScreen) # untuk fungsi callback
glutMainLoop() # fungsi yang akan memulai keseluruhan program
