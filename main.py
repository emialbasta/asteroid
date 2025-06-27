import pygame
import sys
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField
from constants import *
def main():
	pygame.init()
	pyclock = pygame.time.Clock()
	asteroid_group = pygame.sprite.Group()
	asteroid_field_group = pygame.sprite.Group()
	shot_group = pygame.sprite.Group()
	update_group = pygame.sprite.Group()
	draw_group = pygame.sprite.Group()
	Shot.containers = (shot_group, update_group, draw_group)
	AsteroidField.containers = (asteroid_field_group, update_group)
	Asteroid.containers = (asteroid_group, update_group, draw_group)
	Player.containers = (update_group, draw_group)
	asteroid_field = AsteroidField()
	dt = 0
	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2
	player = Player(x,y)
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	while True:
		screen.fill("black")
		update_group.update(dt)
		for asteroid in asteroid_group:
		    if asteroid.is_colliding(player):
		        print("Game over!")
		        sys.exit()
		for asteroid in asteroid_group:
			for shot in shot_group:
				if asteroid.is_colliding(shot):
					result = asteroid.split()
					shot.kill()
					if result:
						for new_asteroid in result:
							print("New asteroid velocity:", new_asteroid.velocity)
							asteroid_group.add(new_asteroid)
		for object in draw_group:
			object.draw(screen)
		pygame.display.flip()
		for event in pygame.event.get():
                	if event.type == pygame.QUIT:
                        	return
		dt = pyclock.tick(60) / 1000
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
if __name__ == "__main__":
	main()
