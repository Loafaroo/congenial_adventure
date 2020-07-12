#Source: Attila Toth
#OpenGL in python e01

import glfw
import OpenGL
import pyrr
import PIL

##create a glfw window

if not glfw.init():
    raise Exception("glfw cannot be initialized.\n")

window = glfw.create_window(1200, 720, "OpenGL in GLFW window", None, None)

#check if window was created:

if not window:
    glfw.terminate()
    raise Exception("glfw window cannot be created.")

# set window position

glfw.set_window_pos(window, 400, 200)

#make the context current

glfw.make_context_current(window)

#the main application loop:
while not glfw.window_should_close(window):
    glfw.poll_events()

    glfw.swap_buffers(window)

#terminate glfw, free up allocated resources

glfw.terminate()
