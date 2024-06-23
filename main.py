import pygame as pg
import moderngl as mgl
import sys
from model import *
from camera import Camera
from lighting import Light
from mesh import Mesh
from scene import Scene
from sceneRenderer import SceneRenderer


class GraphicsEngine:
    def __init__(self, win_size=(1600, 1000)):
        pg.init()
        # window size
        self.WIN_SIZE = win_size
        # set opengl attributes
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        # create the opengl context
        pg.display.set_mode(self.WIN_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF)
        # mouse settings
        pg.event.set_grab(True)
        pg.mouse.set_visible(False)
        #detect and get opengl context
        self.ctx = mgl.create_context()
        self.ctx.enable(flags = mgl.DEPTH_TEST| mgl.CULL_FACE)
        self.clock = pg.time.Clock()
        self.time=0
        self.delta_time = 0
        self.light = Light()
        self.camera = Camera(self)
        self.mesh = Mesh(self)
        self.scene = Scene(self)
        self.scene_renderer = SceneRenderer(self)

    def checkEvents(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.mesh.destroy()
                self.scene_renderer.destroy()
                pg.quit()
                sys.exit()

    def render(self):
        # clear framebuffer
        self.ctx.clear(color=(0.08, 0.16, 0.18))
        self.scene_renderer.render()
        # swap buffers
        pg.display.flip()

    def getTime(self):
        self.time = pg.time.get_ticks() * 0.001



    def run(self):
        while True:
            self.getTime()
            self.checkEvents()
            self.camera.update()
            self.render()
            self.delta_time = self.clock.tick(60)


if __name__ == '__main__':
    app = GraphicsEngine()
    app.run()
