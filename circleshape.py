import pygame

class CircleShape(pygame.sprite.Sprite):
	def __init__(self, x, y, radius, velocity=None):
		if hasattr(self, "containers"):
			super().__init__(self.containers)
		else:
			super().__init__()

		self.position = pygame.Vector2(x, y)
		if velocity is None:
			self.velocity = pygame.Vector2(0, 0)
		else:
			self.velocity = velocity
		self.radius = radius

	def draw(self, screen):
		# sub-classes must override
		pass

	def update(self, dt):
		# sub-classes must override
		pass

	def is_colliding(self, another_circle):
	    distance = self.position.distance_to(another_circle.position)
	    if distance <= self.radius + another_circle.radius:
	        return True
	    else:
	        return False
