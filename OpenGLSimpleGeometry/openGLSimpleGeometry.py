import OpenGL
import OpenGL.GLUT as GLUT
import OpenGL.GL as OPGLL
import OpenGL.GLU as GLU


def square():

    OPGLL.glBegin(OPGLL.GL_QUADS)
    OPGLL.glVertex2f(100, 100)
    OPGLL.glVertex2f(200, 100)
    OPGLL.glVertex2f(200, 200)
    OPGLL.glVertex2f(100, 200)
    OPGLL.glEnd()

def triangle():
    OPGLL.glBegin(OPGLL.GL_POLYGON)
    OPGLL.glVertex2f(250, 250)
    OPGLL.glVertex2f(150, 250)
    OPGLL.glVertex2f(150, 300)
    OPGLL.glEnd()


def parallelogram():

    OPGLL.glBegin(OPGLL.GL_QUADS)
    OPGLL.glVertex2f(250, 300)
    OPGLL.glVertex2f(0, 400)
    OPGLL.glVertex2f(300, 400)
    OPGLL.glVertex2f(400, 400)
    OPGLL.glVertex2f(0, 300)
    OPGLL.glVertex2f(350, 300)
    OPGLL.glEnd()


def itarate():
    OPGLL.glViewport(0,0,500,500)
    OPGLL.glMatrixMode (OPGLL.GL_PROJECTION)
    OPGLL.glLoadIdentity()
    OPGLL.glOrtho(0.0,500,0.0,500,0.0,1.0)
    OPGLL.glMatrixMode(OPGLL.GL_MODELVIEW)
    OPGLL.glLoadIdentity()



def showScreen():
       OPGLL.glClear(OPGLL.GL_COLOR_BUFFER_BIT | OPGLL.GL_COLOR_BUFFER_BIT)
       OPGLL.glLoadIdentity()
       itarate()
       OPGLL.glColor3f(0,191,255)
       triangle()
       OPGLL.glColor3f(255, 0.0, 0.0)
       square()
       OPGLL.glColor3f(255, 0.0, 0.0)
       parallelogram()
       GLUT.glutSwapBuffers()



GLUT.glutInit()
GLUT.glutInitDisplayMode(GLUT.GLUT_RGBA)
GLUT.glutInitWindowSize(500,500)
GLUT.glutInitWindowPosition(0,0)
mainWindow = GLUT.glutCreateWindow("OpenGL Coding Practice")
GLUT.glutDisplayFunc(showScreen)
GLUT.glutIdleFunc(showScreen)
GLUT.glutMainLoop()
