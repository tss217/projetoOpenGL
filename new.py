import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

triangle_position = [0.0, 0.0, -5.0]
rotating = False

def load_texture(filename):
    texture_surface = pygame.image.load(filename)
    texture_data = pygame.image.tostring(texture_surface, "RGBA", 1)
    width, height = texture_surface.get_width(), texture_surface.get_height()

    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)
    
    glTexImage2D(
        GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, texture_data
    )

    error = glGetError()
    if error != GL_NO_ERROR:
        print(f"Erro OpenGL durante o carregamento da textura: {error}")

    return texture_id

def triangle():
    glColor3f(0, 1, 0)

    glBegin(GL_POLYGON);
    glVertex3d(-1.6,-2.6,0.0);
    glVertex3d(-1.6,-1.0,0.0);
    glVertex3d(-1.6,-1.0,-1.6);
    glVertex3d(-1.6,-2.6,-1.6);
    glEnd();
    glBegin(GL_POLYGON);
    glVertex3d(0.0,-2.6,-1.6);
    glVertex3d(0.0,-1.0,-1.6);
    glVertex3d(1.6,-1.0,-1.6);
    glVertex3d(1.6,-2.6,-1.6);
    glEnd();
    glBegin(GL_POLYGON);
    glVertex3d(1.6,-2.6,0.0);
    glVertex3d(1.6,-1.0,0.0);
    glVertex3d(1.6,-1.0,1.6);
    glVertex3d(1.6,-2.6,1.6);
    glEnd();
    glBegin(GL_POLYGON);
    glVertex3d(0.0,-2.6,1.6);
    glVertex3d(0.0,-1.0,1.6);
    glVertex3d(-1.6,-1.0,1.6);
    glVertex3d(-1.6,-2.6,1.6);
    glEnd();
    glBegin(GL_POLYGON);
    glVertex3d(0.0,-2.6,0.0);
    glVertex3d(1.6,-2.6,0.0);
    glVertex3d(1.6,-2.6,1.6);
    glVertex3d(0.0,-2.6,1.6);
    glEnd();
    glBegin(GL_POLYGON);
    glVertex3d(0.0,-1.0,0.0);
    glVertex3d(-1.6,-1.0,0.0);
    glVertex3d(-1.6,-1.0,1.6);
    glVertex3d(0.0,-1.0,1.6);
    glEnd();
    glBegin(GL_POLYGON);
    glVertex3d(1.6,-1.0,0.0);
    glVertex3d(0.0,-1.0,0.0);
    glVertex3d(0.0,-1.0,1.6);
    glVertex3d(1.6,-1.0,1.6);
    glEnd();
    glBegin(GL_POLYGON);
    glVertex3d(-1.6,-2.6,0.0);
    glVertex3d(0.0,-2.6,0.0);
    glVertex3d(0.0,-2.6,1.6);
    glVertex3d(-1.6,-2.6,1.6);
    glEnd();
    glBegin(GL_POLYGON);
    glVertex3d(1.6,-2.6,1.6);
    glVertex3d(1.6,-1.0,1.6);
    glVertex3d(0.0,-1.0,1.6);
    glVertex3d(0.0,-2.6,1.6);
    glEnd();
    glBegin(GL_POLYGON);
    glVertex3d(-1.6,-2.6,-1.6);
    glVertex3d(-1.6,-1.0,-1.6);
    glVertex3d(0.0,-1.0,-1.6);
    glVertex3d(0.0,-2.6,-1.6);
    glEnd();
    glBegin(GL_POLYGON);
    glVertex3d(-1.6,-2.6,-1.6);
    glVertex3d(0.0,-2.6,-1.6);
    glVertex3d(0.0,-2.6,0.0);
    glVertex3d(-1.6,-2.6,0.0);
    glEnd();
    glBegin(GL_POLYGON);
    glVertex3d(1.6,-1.0,-1.6);
    glVertex3d(0.0,-1.0,-1.6);
    glVertex3d(0.0,-1.0,0.0);
    glVertex3d(1.6,-1.0,0.0);
    glEnd();
    glBegin(GL_POLYGON);
    glVertex3d(0.0,-1.0,-1.6);
    glVertex3d(-1.6,-1.0,-1.6);
    glVertex3d(-1.6,-1.0,0.0);
    glVertex3d(0.0,-1.0,0.0);
    glEnd();
    glBegin(GL_POLYGON);
    glVertex3d(0.0,-2.6,-1.6);
    glVertex3d(1.6,-2.6,-1.6);
    glVertex3d(1.6,-2.6,0.0);
    glVertex3d(0.0,-2.6,0.0);
    glEnd();
    glBegin(GL_POLYGON);
    glVertex3d(1.6,-2.6,-1.6);
    glVertex3d(1.6,-1.0,-1.6);
    glVertex3d(1.6,-1.0,0.0);
    glVertex3d(1.6,-2.6,0.0);
    glEnd();
    glBegin(GL_POLYGON);
    glVertex3d(-1.6,-2.6,1.6);
    glVertex3d(-1.6,-1.0,1.6);
    glVertex3d(-1.6,-1.0,0.0);
    glVertex3d(-1.6,-2.6,0.0);
    glEnd();
    glBegin(GL_POLYGON);
    glVertex3d(-0.000357,-0.992444,0.496222);
    glVertex3d(-0.000357,-0.496222,0.496222);
    glVertex3d(-0.000357,-0.496222,0.165407);
    glVertex3d(-0.000357,-0.992444,0.165407);
    glEnd();
    glBegin(GL_POLYGON);
    glVertex3d(-0.000357,-0.992444,0.165407);
    glVertex3d(-0.000357,-0.496222,0.165407);
    glVertex3d(0.330815,-0.496222,0.165407);
    glVertex3d(0.330815,-0.992444,0.165407);
    glEnd();
    glBegin(GL_POLYGON);
    glVertex3d(0.330815,-0.992444,0.165407);
    glVertex3d(0.330815,-0.496222,0.165407);
    glVertex3d(0.330815,-0.496222,0.496222);
    glVertex3d(0.330815,-0.992444,0.496222);
    glEnd();
    glBegin(GL_POLYGON);
    glVertex3d(0.330815,-0.992444,0.496222);
    glVertex3d(0.330815,-0.496222,0.496222);
    glVertex3d(-0.000357,-0.496222,0.496222);
    glVertex3d(-0.000357,-0.992444,0.496222);
    glEnd();
    glBegin(GL_POLYGON);
    glVertex3d(-0.000357,-0.992444,0.165407);
    glVertex3d(0.330815,-0.992444,0.165407);
    glVertex3d(0.330815,-0.992444,0.496222);
    glVertex3d(-0.000357,-0.992444,0.496222);
    glEnd();
    glBegin(GL_POLYGON);
    glVertex3d(0.330815,-0.496222,0.165407);
    glVertex3d(-0.000357,-0.496222,0.165407);
    glVertex3d(-0.000357,-0.496222,0.496222);
    glVertex3d(0.330815,-0.496222,0.496222);
    glEnd();
    glBegin(GL_POLYGON);
    glVertex3d(0.330815,1.157851,-0.330815);
    glVertex3d(-0.330815,1.157851,-0.330815);
    glVertex3d(-0.330815,1.157851,0.330815);
    glVertex3d(0.330815,1.157851,0.330815);
    glEnd();
    glBegin(GL_POLYGON);
    glVertex3d(0.330815,0.496222,0.330815);
    glVertex3d(0.330815,1.157851,0.330815);
    glVertex3d(-0.330815,1.157851,0.330815);
    glVertex3d(-0.330815,0.496222,0.330815);
    glEnd();
    glBegin(GL_POLYGON);
    glVertex3d(-0.330815,0.496222,0.330815);
    glVertex3d(-0.330815,1.157851,0.330815);
    glVertex3d(-0.330815,1.157851,-0.330815);
    glVertex3d(-0.330815,0.496222,-0.330815);
    glEnd();
    glBegin(GL_POLYGON);
    glVertex3d(-0.330815,0.496222,-0.330815);
    glVertex3d(0.330815,0.496222,-0.330815);
    glVertex3d(0.330815,0.496222,0.330815);
    glVertex3d(-0.330815,0.496222,0.330815);
    glEnd();
    glBegin(GL_POLYGON);
    glVertex3d(0.330815,0.496222,-0.330815);
    glVertex3d(0.330815,1.157851,-0.330815);
    glVertex3d(0.330815,1.157851,0.330815);
    glVertex3d(0.330815,0.496222,0.330815);
    glEnd();
    glBegin(GL_POLYGON);
    glVertex3d(-0.330815,0.496222,-0.330815);
    glVertex3d(-0.330815,1.157851,-0.330815);
    glVertex3d(0.330815,1.157851,-0.330815);
    glVertex3d(0.330815,0.496222,-0.330815);
    glEnd();
    glBegin(GL_POLYGON);
    glVertex3d(-0.330815,-0.496222,0.165407);
    glVertex3d(-0.330815,0.496222,0.165407);
    glVertex3d(-0.330815,0.496222,-0.165407);
    glVertex3d(-0.330815,-0.496222,-0.165407);
    glEnd();
    glBegin(GL_POLYGON);
    glVertex3d(-0.330815,-0.496222,-0.165407);
    glVertex3d(-0.330815,0.496222,-0.165407);
    glVertex3d(0.330815,0.496222,-0.165407);
    glVertex3d(0.330815,-0.496222,-0.165407);
    glEnd();
    glBegin(GL_POLYGON);
    glVertex3d(0.330815,-0.496222,-0.165407);
    glVertex3d(0.330815,0.496222,-0.165407);
    glVertex3d(0.330815,0.496222,0.165407);
    glVertex3d(0.330815,-0.496222,0.165407);
    glEnd();
    glBegin(GL_POLYGON);
    glVertex3d(0.330815,-0.496222,0.165407);
    glVertex3d(0.330815,0.496222,0.165407);
    glVertex3d(-0.330815,0.496222,0.165407);
    glVertex3d(-0.330815,-0.496222,0.165407);
    glEnd();
    glBegin(GL_POLYGON);
    glVertex3d(-0.330815,-0.496222,-0.165407);
    glVertex3d(0.330815,-0.496222,-0.165407);
    glVertex3d(0.330815,-0.496222,0.165407);
    glVertex3d(-0.330815,-0.496222,0.165407);
    glEnd();
    glBegin(GL_POLYGON);
    glVertex3d(0.330815,0.496222,-0.165407);
    glVertex3d(-0.330815,0.496222,-0.165407);
    glVertex3d(-0.330815,0.496222,0.165407);
    glVertex3d(0.330815,0.496222,0.165407);
    glEnd();
    glBegin(GL_POLYGON);
    glVertex3d(-0.330815,-0.992444,-0.165407);
    glVertex3d(-0.330815,-0.496222,-0.165407);
    glVertex3d(-0.330815,-0.496222,-0.496222);
    glVertex3d(-0.330815,-0.992444,-0.496222);
    glEnd();
    glBegin(GL_POLYGON);
    glVertex3d(-0.330815,-0.992444,-0.496222);
    glVertex3d(-0.330815,-0.496222,-0.496222);
    glVertex3d(0.0,-0.496222,-0.496222);
    glVertex3d(0.0,-0.992444,-0.496222);
    glEnd();
    glBegin(GL_POLYGON);
    glVertex3d(0.0,-0.992444,-0.496222);
    glVertex3d(0.0,-0.496222,-0.496222);
    glVertex3d(0.0,-0.496222,-0.165407);
    glVertex3d(0.0,-0.992444,-0.165407);
    glEnd();
    glBegin(GL_POLYGON);
    glVertex3d(0.0,-0.992444,-0.165407);
    glVertex3d(0.0,-0.496222,-0.165407);
    glVertex3d(-0.330815,-0.496222,-0.165407);
    glVertex3d(-0.330815,-0.992444,-0.165407);
    glEnd();
    glBegin(GL_POLYGON);
    glVertex3d(-0.330815,-0.992444,-0.496222);
    glVertex3d(0.0,-0.992444,-0.496222);
    glVertex3d(0.0,-0.992444,-0.165407);
    glVertex3d(-0.330815,-0.992444,-0.165407);
    glEnd();
    glBegin(GL_POLYGON);
    glVertex3d(0.0,-0.496222,-0.496222);
    glVertex3d(-0.330815,-0.496222,-0.496222);
    glVertex3d(-0.330815,-0.496222,-0.165407);
    glVertex3d(0.0,-0.496222,-0.165407);
    glEnd();
    glBegin(GL_POLYGON);
    glVertex3d(0.0,-0.992444,-0.165407);
    glVertex3d(0.0,-0.496222,-0.165407);
    glVertex3d(0.0,-0.496222,-0.496222);
    glVertex3d(0.0,-0.992444,-0.496222);
    glEnd();
    glBegin(GL_POLYGON);
    glVertex3d(0.0,-0.992444,-0.496222);
    glVertex3d(0.0,-0.496222,-0.496222);
    glVertex3d(0.330815,-0.496222,-0.496222);
    glVertex3d(0.330815,-0.992444,-0.496222);
    glEnd();
    glBegin(GL_POLYGON);
    glVertex3d(0.330815,-0.992444,-0.496222);
    glVertex3d(0.330815,-0.496222,-0.496222);
    glVertex3d(0.330815,-0.496222,-0.165407);
    glVertex3d(0.330815,-0.992444,-0.165407);
    glEnd();
    glBegin(GL_POLYGON);
    glVertex3d(0.330815,-0.992444,-0.165407);
    glVertex3d(0.330815,-0.496222,-0.165407);
    glVertex3d(0.0,-0.496222,-0.165407);
    glVertex3d(0.0,-0.992444,-0.165407);
    glEnd();
    glBegin(GL_POLYGON);
    glVertex3d(0.0,-0.992444,-0.496222);
    glVertex3d(0.330815,-0.992444,-0.496222);
    glVertex3d(0.330815,-0.992444,-0.165407);
    glVertex3d(0.0,-0.992444,-0.165407);
    glEnd();
    glBegin(GL_POLYGON);
    glVertex3d(0.330815,-0.496222,-0.496222);
    glVertex3d(0.0,-0.496222,-0.496222);
    glVertex3d(0.0,-0.496222,-0.165407);
    glVertex3d(0.330815,-0.496222,-0.165407);
    glEnd();
    glBegin(GL_POLYGON);
    glVertex3d(-0.330815,-0.992444,0.496222);
    glVertex3d(-0.330815,-0.496222,0.496222);
    glVertex3d(-0.330815,-0.496222,0.165407);
    glVertex3d(-0.330815,-0.992444,0.165407);
    glEnd();
    glBegin(GL_POLYGON);
    glVertex3d(-0.330815,-0.992444,0.165407);
    glVertex3d(-0.330815,-0.496222,0.165407);
    glVertex3d(0.0,-0.496222,0.165407);
    glVertex3d(0.0,-0.992444,0.165407);
    glEnd();
    glBegin(GL_POLYGON);
    glVertex3d(0.0,-0.992444,0.165407);
    glVertex3d(0.0,-0.496222,0.165407);
    glVertex3d(0.0,-0.496222,0.496222);
    glVertex3d(0.0,-0.992444,0.496222);
    glEnd();
    glBegin(GL_POLYGON);
    glVertex3d(0.0,-0.992444,0.496222);
    glVertex3d(0.0,-0.496222,0.496222);
    glVertex3d(-0.330815,-0.496222,0.496222);
    glVertex3d(-0.330815,-0.992444,0.496222);
    glEnd();
    glBegin(GL_POLYGON);
    glVertex3d(-0.330815,-0.992444,0.165407);
    glVertex3d(0.0,-0.992444,0.165407);
    glVertex3d(0.0,-0.992444,0.496222);
    glVertex3d(-0.330815,-0.992444,0.496222);
    glEnd();
    glBegin(GL_POLYGON);
    glVertex3d(0.0,-0.496222,0.165407);
    glVertex3d(-0.330815,-0.496222,0.165407);
    glVertex3d(-0.330815,-0.496222,0.496222);
    glVertex3d(0.0,-0.496222,0.496222);
    glEnd();



    # Repita o processo para os outros polígonos...

def main():
    global rotating
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    # load_texture("/home/ts217/Documents/provaVC/projetoOpenGL/creeper.png")
    


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                triangle_position[0] = (x - display[0] / 2) / 200
                triangle_position[1] = -(y - display[1] / 2) / 200
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    rotating = not rotating
        
        if rotating:
            glRotatef(1, 3, 1, 1)
    
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glEnable(GL_TEXTURE_2D)
        glPushMatrix()
        glTranslatef(*triangle_position)
        triangle()
        glPopMatrix()
        glDisable(GL_TEXTURE_2D)
        pygame.display.flip()
        pygame.time.wait(10)

        error = glGetError()
        if error != GL_NO_ERROR:
            print(f"Erro OpenGL durante o desenho: {error}")

if __name__ == "__main__":
    main()
