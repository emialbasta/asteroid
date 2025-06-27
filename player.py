import pygame
from constants import *

from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
	def __init__(self, x, y):
		super().__init__(x, y, PLAYER_RADIUS)
		self.rotation = 0
		self.timer = 0

	def triangle(self):
    		forward = pygame.Vector2(0, 1).rotate(self.rotation)
    		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
    		a = self.position + forward * self.radius
    		b = self.position - forward * self.radius - right
    		c = self.position - forward * self.radius + right
    		return [a, b, c]

	def draw(self, screen):
		pygame.draw.polygon(screen, "white", self.triangle(), 2)

	def rotate(self, dt):
		self.rotation += PLAYER_TURN_SPEED * dt

	def move(self, dt):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		self.position += forward * PLAYER_SPEED * dt

	def shoot(self):
		if self.timer > 0:
			return
		offset = pygame.Vector2(0, self.radius).rotate(self.rotation)
		shot_x = self.position.x + offset.x
		shot_y = self.position.y + offset.y

		direction = pygame.Vector2(0, 1).rotate(self.rotation)
		velocity = direction * PLAYER_SHOOT_SPEED

		shot = Shot(shot_x, shot_y, velocity)
		self.timer = PLAYER_SHOOT_COOLDOWN

	def update(self, dt):
		keys = pygame.key.get_pressed()
		self.timer = self.timer - dt

		if keys[pygame.K_a] or keys[pygame.K_LEFT]:
			self.rotate(dt * -1)

		if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
			self.rotate(dt)

		if keys[pygame.K_w] or keys[pygame.K_UP]:
			self.move(dt)

		if keys[pygame.K_s] or keys[pygame.K_DOWN]:
			self.move(dt)

		if keys[pygame.K_SPACE]:
            		self.shoot() 
