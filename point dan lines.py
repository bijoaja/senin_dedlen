#import library
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
w,h= 500,500

#fungsi objek titik
def titik():
    glPointSize(10) #utk mengatur ukuran titiknya
    glBegin(GL_POINTS) #utk memulai pembuatan objek titik
    glColor3ub(66, 207, 160) #kode warna pake rgb
    glVertex2f(10,10) #titik koordinat
    glEnd() #utk mengakhiri objek yang dibuat

#fungsi objek garis
def garis():
    glColor3f(0.0,1.0,0.0) #kode warna pake float
    glPointSize(10)
    glBegin(GL_LINES) #utk membuat objek garis
    glVertex2f(200, 200) 
    glVertex2f(300, 300)
    glEnd()

def garisloop():
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_LINE_LOOP) #utk membuat objek garis yang berhubungan
    glVertex2f(150, 150)
    glVertex2f(250, 300)
    glVertex2f(180, 320)
    glEnd()

def kotak():
    glBegin(GL_QUADS) #utk membuat objek kotak/ titik koordinatnya ada 4
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(100, 100)
    glVertex2f(200, 100)
    glVertex2f(200, 200)
    glVertex2f(100, 200)
    glEnd()

def tak_beraturan():
    glBegin(GL_POLYGON) #utk membuat objek yang titik koordinatnya banyak
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(100, 100)
    glVertex2f(200, 100)
    glVertex2f(200, 200)
    glVertex2f(250,250)
    glVertex2f(50,100)
    glVertex2f(100, 200)
    glEnd()

#fungsi iterasi
def iterate():
    glViewport(0, 0, 500, 500) #utk mengatur area pandang
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0) #utk mengatur berapa blok yang digunakan (skala) nilai x, y, z
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #utk membersihkan layar
    glLoadIdentity()
    iterate()
    # titik()
    # garis()
    # garisloop()
    # kotak()
    tak_beraturan()
    glutSwapBuffers() #utk membersihkan layar, double buffering

glutInit() #inisialisasi glut
glutInitDisplayMode(GLUT_RGBA) #utk mengatur display supaya berwarna
glutInitWindowSize(500, 500) #utk mengatur ukuran window
glutInitWindowPosition(0, 0) #utk mengatur letak window
#utk transparansi (tapi belum bisa)
#glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
#glEnable(GL_BLEND)
wind = glutCreateWindow("Point and Lines") #utk memberi nama pada window
glutDisplayFunc(showScreen) #utk fungsi callback
glutIdleFunc(showScreen) #utk fungsi callback
glutMainLoop() #fungsi yang akan memulai keseluruhan program
