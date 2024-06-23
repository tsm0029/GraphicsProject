import glm
import pygame as pg
FOV = 50
NEAR = 0.1
FAR = 100
SPEED = 0.01
SENSITIVITY = 0.05
class Camera:
    def __init__(self,app,position=(0,0,4),yaw = 90, pitch = 0):
        self.app = app
        self.aspect_ratio = app.WIN_SIZE[0] / app.WIN_SIZE[1]
        self.position = glm.vec3(2,3,3)
        self.up = glm.vec3(0,1,0)
        self.right = glm.vec3(1,0,0)
        self.forward = glm.vec3(0,0,-1)
        self.yaw = yaw
        self.pitch = pitch
        self.m_view = self.getViewMatrix()
        self.m_proj = self.getProjectionMatrix()

#calculate yaw apitch with relative values and limit it so its doesnt do some wonky stuff
    def rotate(self):
        rel_x, rel_y = pg.mouse.get_rel()
        self.yaw += rel_x * SENSITIVITY
        self.pitch -= rel_y * SENSITIVITY
        self.pitch = max(-90, min(90, self.pitch))

#recalculates camera angle basedoff  yaw and pitch
    def updateCameraVectors(self):
        yaw, pitch = glm.radians(self.yaw), glm.radians(self.pitch)

        self.forward.x = glm.cos(yaw) * glm.cos(pitch)
        self.forward.y = glm.sin(pitch)
        self.forward.z = glm.sin(yaw) * glm.cos(pitch)

        self.forward = glm.normalize(self.forward)
        self.right = glm.normalize(glm.cross(self.forward, glm.vec3(0, 1, 0)))
        self.up = glm.normalize(glm.cross(self.right, self.forward))


     #recalculates the view matrix
    def update(self):
        self.move()
        self.rotate()
        self.updateCameraVectors()
        self.m_view = self.getViewMatrix()

    def move(self):
        velocity = SPEED * self.app.delta_time
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.position += self.forward * velocity
        if keys[pg.K_s]:
            self.position -= self.forward * velocity
        if keys[pg.K_a]:
            self.position -= self.right * velocity
        if keys[pg.K_d]:
            self.position += self.right * velocity
        if keys[pg.K_q]:
            self.position += self.up * velocity
        if keys[pg.K_e]:
            self.position -= self.up * velocity


    def getViewMatrix(self):
        return glm.lookAt(self.position,self.position+self.forward,self.up)


    def getProjectionMatrix(self):
        return glm.perspective(glm.radians(FOV),self.aspect_ratio, NEAR, FAR)