class SceneRenderer:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx
        self.mesh = app.mesh
        self.scene = app.scene
        # depth buffer
        self.depth_texture = self.mesh.texture.textures['depth_texture']
        self.depth_fbo = self.ctx.framebuffer(depth_attachment=self.depth_texture)

    def renderShadow(self):
        self.depth_fbo.clear()
        self.depth_fbo.use()
        for obj in self.scene.objects:
            obj.renderShadow()

    def mainRender(self):
        self.app.ctx.screen.use()
        for obj in self.scene.objects:
            obj.render()
        self.scene.skybox.render()

    def render(self):
        self.scene.update()
        # pass 1
        self.renderShadow()
        # pass 2
        self.mainRender()

    def destroy(self):
        self.depth_fbo.release()
