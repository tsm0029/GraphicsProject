from model import *
import glm


class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.load()
        # cubemap
        self.skybox = SkyBox(app)

    def add_object(self, obj):
        self.objects.append(obj)

    def load(self):
        app = self.app
        add = self.add_object
        self.moving_cube = MovingCube(app, pos=(0, 1, 8), scale=(.75, 2, .75), tex_id=8)
        self.moving_cube1 = MovingCube(app, pos=(0, 4, 8), scale=(.5, .5, .5), tex_id=8)
        # add(House(app))
        # add(Cone(app))
        b,n, s= -10, 80, 2
        exclude_rect_x = range(-100, 100)  # x-coordinate range of the excluded rectangle
        exclude_rect_z = range(18,22)  # z-coordinate range of the excluded rectangle

        for x in range(b, n, s):
            for z in range(b, n, s):
                # Check if the current position is outside the excluded rectangle
                if x not in exclude_rect_x or z not in exclude_rect_z:
                    add(Cube(app, pos=(x, -s, z)))
                else:
                    # Add cubes in the place of the excluded rectangle
                    add(Cube(app, tex_id = 1, pos=(x, -s, z),))
        #house walls
        add(Cube(app, pos=(12.5, 1, 8), scale=(2.4, 2, 1), tex_id=4))
        add(Cube(app, pos=(25, 1, 8), scale=(1, 2, 1), tex_id=4))
        add(Cube(app, pos=(19, 1, 8), scale=(2, 2, 1), tex_id=4))
        add(Cube(app, pos=(22, -.5, 8), scale=(2, 1, 1), tex_id=4))
        add(Cube(app,  pos=(25, 1, 1), scale=(1, 2, 7), tex_id=4))
        add(Cube(app,pos=(17, 1, -5), scale=(7, 2, 1), tex_id=4))
        add(Cube(app,pos=(11.1, .05, 1), scale=(1, 1, 7), tex_id=4))
        #table
        add(Cube(app, pos=(17, 0, 1), rot=(90, 0, 0), scale=(.25, .25, 1), tex_id=4))
        add(Cube(app, pos=(17, 0, 3), rot=(90, 0, 0), scale=(.25, .25, 1), tex_id=4))
        add(Cube(app, pos=(22, 0, 1), rot=(90, 0, 0), scale=(.25, .25, 1), tex_id=4))
        add(Cube(app, pos=(22, 0, 3), rot=(90, 0, 0), scale=(.25, .25, 1), tex_id=4))
        add(Cube(app, pos=(19.5, 1, 2), rot=(180, 0, 0), scale=(3, .25, 2), tex_id=4))

        #house roofs
        add(Cube(app, pos=(18, 4,2), scale=(8, 1, 8),  tex_id=4))
        add(Cube(app,  pos=(18, 6, 2), scale=(6, 1, 8), tex_id=4))
        add(Cube(app, pos=(18, 8, 2), scale=(4, 1, 8),  tex_id=4))
        add(Cube(app, pos=(18, 10, 2), scale=(2, 1, 8), tex_id=4))
        add(Cube(app, pos=(18, 10, 2), scale=(2, 1, 8), tex_id=4))
        add(Cube(app, pos=(14, 8, 2),rot=(0,0,45), scale=(6, 1, 8), tex_id=3))
        add(Cube(app, pos=(22, 8, 2), rot=(0, 0, -45), scale=(6.75, 1, 8), tex_id=3))

        #tower
        add(Cube(app, pos=(50, 1, 8), scale=(4, 16, 1), tex_id=7))
        add(Cube(app, pos=(53, 1, 4), scale=(1, 16, 4), tex_id=7))
        add(Cube(app, pos=(47, 1, 4), scale=(1, 16, 4), tex_id=7))
        add(Cube(app, pos=(50, 1,0), scale=(4, 16, 1), tex_id=7))
        add(Cube(app, pos=(50, 18, 4), scale=(6, 2, 6), tex_id=7))

        #pyramid
        add(Cube(app, pos=(50, 0, 42), scale=(16, 1, 16), tex_id=5))
        add(Cube(app, pos=(50, 2, 42), scale=(14, 1, 14), tex_id=5))
        add(Cube(app, pos=(50, 4, 42), scale=(12, 1, 12), tex_id=5))
        add(Cube(app, pos=(50, 6, 42), scale=(10, 1, 10), tex_id=5))
        add(Cube(app, pos=(50, 8, 42), scale=(8, 1, 8), tex_id=5))
        add(Cube(app, pos=(50, 10, 42), scale=(6, 1, 6), tex_id=5))
        add(Cube(app, pos=(50, 12, 42), scale=(4, 1, 4), tex_id=5))
        add(Cube(app, pos=(50, 14, 42), scale=(2, 1, 2), tex_id=5))

        #stable
        add(Cube(app, pos=(18, 4, 30), rot=(10,0,0), scale=(3, .25, 4), tex_id=4))
        add(Cube(app, pos=(18, 1, 33), rot=(90, 0, 0), scale=(3, .25, 2.5), tex_id=4))
        add(Cube(app, pos=(20.25, 1, 27), rot=(90, 0, 0), scale=(.25, .25, 3.25), tex_id=4))
        add(Cube(app, pos=(15.5, 1, 27), rot=(90, 0, 0), scale=(.25, .25, 3.25), tex_id=4))
        add(Cube(app, pos=(15.5, 1, 30), rot=(180, 0, 0), scale=(.25, .25, 3.25), tex_id=4))
        add(Cube(app, pos=(20.25, 1, 30), rot=(180, 0, 0), scale=(.25, .25, 3.25), tex_id=4))

        #character
        x = 90
        add(Cube(app, pos=(1, 0, 30), rot=(90, 0, 0), scale=(.25, .25, 1), tex_id=8))
        add(Cube(app, pos=(2, 0, 30), rot=(90, 0, 0), scale=(.25, .25, 1), tex_id=8))
        add(Cube(app, pos=(1.5, 2, 30), rot=(90, 0, 0), scale=(.75, .25, 1), tex_id=8))
        #arm
        add(Cube(app, pos=(3, 2, 30), rot=(100, 0, 0), scale=(.25, .25, 1), tex_id=8))
        #neck/head
        add(Cube(app, pos=(1.5, 3, 30), rot=(90, 0, 0), scale=(.25, .25, 1), tex_id=8))

        #arm
        add(Cube(app, pos=(0, 2, 30), rot=(90, 0, 0), scale=(.25, .25, 1), tex_id=8))

        #horse
        #legs
        add(Cube(app, pos=(17, 0, 25), rot=(90, 0, 0), scale=(.25, .25, 1), tex_id=6))
        add(Cube(app, pos=(17, 0, 22), rot=(90, 0, 0), scale=(.25, .25, 1), tex_id=6))
        add(Cube(app, pos=(18.5, 0, 25), rot=(90, 0, 0), scale=(.25, .25, 1), tex_id=6))
        add(Cube(app, pos=(18.5, 0, 22), rot=(90, 0, 0), scale=(.25, .25, 1), tex_id=6))
        #body
        add(Cube(app, pos=(17.7, 2, 23.5), rot=(0, 0, 0), scale=(1.3, 1, 2), tex_id=6))
        #head/neck
        add(Cube(app, pos=(17.7, 3, 21), rot=(-150, 0, 0), scale=(.4, .4, 1), tex_id=6))
        add(Cube(app, pos=(17.7, 3, 20), rot=(-760, 0, 0), scale=(.4, .4, 1), tex_id=6))

        #tree
        add(Cube(app, pos=(7, .1, 27), rot=(90, 0, 0), scale=(.25, .25, 1), tex_id=4))
        add(Cube(app, pos=(7, 1, 27), rot=(0, 0, 0), scale=(1, 1, 1), tex_id=0))
        add(Cube(app, pos=(7, 2.5, 27), rot=(0, 0, 0), scale=(.75, .75, .75), tex_id=0))
        add(Cube(app, pos=(7, 3.5, 27), rot=(0, 0, 0), scale=(.5, 1, .5), tex_id=0))








        add(self.moving_cube)
        add(self.moving_cube1)

    def render(self):
        for obj in self.objects:
            obj.render()
        self.skybox.render()

    def update(self):
        self.moving_cube.rot.y = self.app.time
        self.moving_cube1.rot.y = self.app.time


        #  self.wall1 = Cube(app, pos=(12, 1, 8), scale=(2, self.cube_size, 1), tex_id=2)
        # #         self.wall2 = Cube(app, pos=(25, 1, 8), scale=(1, 2, 1), tex_id=2)
        # #         self.wall3 = Cube(app, pos=(19, 1, 8), scale=(1, 2, 1), tex_id=2)
        # #         self.wall4 = Cube(app, pos=(22, -.5, 8), scale=(2, 2, 1), tex_id=2)
        # #         self.wall5 = Cube(app, pos=(25, 1, 16), scale=(1, 2, 7), tex_id=2)
        # #         self.wall6 = Cube(app, pos=(17, 1, 22), scale=(7, 2, 1), tex_id=2)
        # #         self.wall7 = Cube(app, pos=(11, 1, 16), scale=(1, 2, 7), tex_id=2)

        # Create cube for the roof
        #         self.roof = Cube(app, pos=(18, 4, 15), scale=(8, 1, 8), tex_id=2)
        #         self.roof1 = Cube(app, pos=(18, 6, 15), scale=(6, 1, 8), tex_id=2)
        #         self.roof2 = Cube(app, pos=(18, 8, 15), scale=(4, 1, 8), tex_id=2)
        #         self.roof3 = Cube(app, pos=(18, 10, 15), scale=(2, 1, 8), tex_id=2)
        #         #create cubes for chair
        #         self.chair1 =  Cube(app, pos=(22, .1, 16), scale=(1, 1, 1), tex_id=2)