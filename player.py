from constants import *
from circleshape import *
from shot import *
import pygame

WHITE = (255, 255, 255)


class Player(CircleShape):

    def __init__(self, x, y,):
        super().__init__(x, y, PLAYER_RADIUS)
        self.position = pygame.Vector2(x, y)
        self.radius = PLAYER_RADIUS
        self.rotation = 0
        self.timer = 0

    def draw(self, screen):
        pygame.draw.polygon(screen, WHITE, self.triangle(), 2)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        self.rotation %= 360

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)  
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

        if self.timer > 0:
            self.timer -= dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.timer > 0:
            return

        else:
            new_shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            velocity = pygame.Vector2(0, 1).rotate(self.rotation)
            velocity *= PLAYER_SHOOT_SPEED
            new_shot.velocity = velocity
            new_shot.add(shots)
            self.timer = PLAYER_SHOOT_COOLDOWN
        
            
