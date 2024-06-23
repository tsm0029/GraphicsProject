import pygame as pg
import moderngl as mgl
import glm


class Texture:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx
        self.textures = {}
        self.textures[0] = self.getTexture(path='textures/grass.png')
        self.textures[1] = self.getTexture(path='textures/img_1.png')
        self.textures[2] = self.getTexture(path='textures/img_2.png')
        self.textures[3] = self.getTexture(path='textures/roof.png')
        self.textures[4] = self.getTexture(path='textures/wood.png')
        self.textures[5] = self.getTexture(path='textures/sandstone.png')
        self.textures[6] = self.getTexture(path='textures/horse.png')
        self.textures[7] = self.getTexture(path='textures/castle.png')
        self.textures[8] = self.getTexture(path='textures/blue.png')
        self.textures['cubemap'] = self.getTextureCube(dir_path='textures/cubemap/', ext='jpg')
        self.textures['depth_texture'] = self.getDepthTexture()

    def getDepthTexture(self):
        depth_texture = self.ctx.depth_texture(self.app.WIN_SIZE)

        return depth_texture

    def getTextureCube(self, dir_path, ext='jpg'):
        faces = ['posx', 'negx', 'posy', 'negy'] + ['negz', 'posz'][::-1]

        textures = []

        for face in faces:
            texture = pg.image.load(dir_path + f'{face}.{ext}').convert()
            if face in ['right', 'left', 'front', 'back']:
                texture = pg.transform.flip(texture, flip_x=False, flip_y=False)
            else:
                texture = pg.transform.flip(texture, flip_x=False, flip_y=False)
            textures.append(texture)

        size = textures[0].get_size()
        texture_cube = self.ctx.texture_cube(size=size, components=3, data=None)

        for i in range(6):
            texture_data = pg.image.tostring(textures[i], 'RGB')
            texture_cube.write(face=i, data=texture_data)

        return texture_cube

    def getTexture(self, path):
        texture = pg.image.load(path).convert()
        texture = pg.transform.flip(texture, flip_x=False, flip_y=True)
        texture = self.ctx.texture(size=texture.get_size(), components=3,
                                   data=pg.image.tostring(texture, 'RGB'))

        return texture

    def destroy(self):
        [tex.release() for tex in self.textures.values()]