import pygame
import random

pygame.init()

# create the screen with 800px width, 600px height
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("icon.png")
background = pygame.image.load("background.png")

pygame.display.set_icon(icon)


playerImg = pygame.image.load("airplane.png")
playerX = 336
playerY = 460
playerX_change = 0

enemyImg = pygame.image.load("alien.png")
enemyX = random.randint(30, 729)
enemyY = random.randint(0, 150)
enemyX_change = 3.5
enemyY_change = 50

bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 460 
bulletX_change = 0
bulletY_change = 15
bullet_state = "ready"

def fire_bullet(x, y):
	global bullet_state, bulletX
	bullet_state = "fire"
	screen.blit(bulletImg, (x+32, y-20))

def player(x, y):
	screen.blit(playerImg, (x, y))

def enemy(x, y):
	screen.blit(enemyImg, (x, y))


running = True
while running:
	screen.fill([255, 255, 255])
	screen.blit(background, (0,0))
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				playerX_change -= 8
			if event.key == pygame.K_RIGHT:
				playerX_change += 8
			if bullet_state != "fire":
				if event.key == pygame.K_SPACE:
					bulletX = playerX	
					fire_bullet(bulletX, playerY)

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or pygame.K_RIGHT:
				playerX_change = 0

	enemyX += enemyX_change
	if enemyX <= 0:
		enemyY += enemyY_change
		enemyX_change = 3.5
	elif enemyX >= 736:
		enemyY += enemyY_change
		enemyX_change = -3.5

	if playerX + playerX_change > 20 and playerX + playerX_change < 660:
		playerX += playerX_change

	if bulletY <= -20:
		bulletY = 460
		bullet_state = "ready"

	if bullet_state is "fire":
		fire_bullet(bulletX, bulletY)
		bulletY -= bulletY_change

	player(playerX, playerY)
	enemy(enemyX, enemyY)
	pygame.display.update()

	


