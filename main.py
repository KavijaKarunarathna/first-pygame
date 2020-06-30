import pygame

pygame.init()

# create the screen with 800px width, 600px height
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)


playerImg = pygame.image.load("airplane.png")

playerX = 336
playerY = 460
playerX_change = 0


def player(x, y):
	screen.blit(playerImg, (x, y))

running = True
while running:
	screen.fill([255, 255, 255])
	screen.blit(BackGround.image, BackGround.rect)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				playerX_change -= 0.6
			if event.key == pygame.K_RIGHT:
				playerX_change += 0.6

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or pygame.K_RIGHT:
				playerX_change = 0

	if playerX + playerX_change > 20 and playerX + playerX_change < 660:
		playerX += playerX_change

	player(playerX, playerY)
	pygame.display.update()

	


