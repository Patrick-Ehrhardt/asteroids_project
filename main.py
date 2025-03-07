import pygame
from constants import *

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	game_continue = True
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	while(game_continue):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_continue = False
				return
		screen.fill(pygame.Color(255,255,255))
		pygame.display.flip()

if __name__ == "__main__":
	main()
