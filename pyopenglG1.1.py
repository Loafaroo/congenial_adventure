import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from random import choice

vertices = (
    ###create a generator for vertices
    )

edges = (
    ###create a generator for edges 
    )

def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])

    glEnd()

def main():
    pygame.init()
    display = (1080, 720)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(30, display[0]/display[1], 0.1, 50.0)

    glTranslatef(0.0, 0.0, -5)

    glRotatef(0, 0, 0, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()

        pygame.time.wait(choice([10, 100]))

if __name__ == "__main__":
    main()
    
        
