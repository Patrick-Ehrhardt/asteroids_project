import pygame
from constants import *
from player import Player

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	game_continue = True
	clock = pygame.time.Clock()
	dt = 0
	updateable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	Player.containers = (updateable, drawable)
	player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	while(game_continue):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_continue = False
				return
		screen.fill("black")
		updateable.update(dt)
		for object in drawable:
			object.draw(screen)
		pygame.display.flip()
		dt = clock.tick(60) / 1000

if __name__ == "__main__":
	main()
