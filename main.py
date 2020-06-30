import pygame
import random
import math
from pygame import mixer

pygame.init()

# create the screen with 800px width, 600px height
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("img/icon.png")

background = pygame.image.load("img/background.png")
mixer.music.load("music/back-music.mp3")
mixer.music.play(-1)

pygame.display.set_icon(icon)


playerImg = pygame.image.load("img/airplane.png")
playerX = 336
playerY = 460
playerX_change = 0

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_enemies = 5

for i in range(num_enemies):
	enemyImg.append(pygame.image.load("img/alien.png"))
	enemyX.append(random.randint(30, 729))
	enemyY.append(random.randint(0, 150))
	enemyX_change.append(1.3)
	enemyY_change.append(50)

bulletImg = pygame.image.load("img/bullet.png")
bulletX = 0
bulletY = 460 
bulletX_change = 0
bulletY_change = 8
bullet_state = "ready"

score = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10 

over_text = pygame.font.Font("freesansbold.ttf", 64)

def fire_bullet(x, y):
	global bullet_state, bulletX
	bullet_state = "fire"
	screen.blit(bulletImg, (x+43, y-30))

def player(x, y):
	screen.blit(playerImg, (x, y))

def enemy(x, y, i): 
	screen.blit(enemyImg[i], (x, y))

def isCollision(enemyX, enemyY, bulletX, bulletY):
	distance = math.sqrt((math.pow((enemyX -10)- bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
	if distance < 35:
		return True
	return False

def showScore(x, y, score):
	score = font.render("Score: "+str(score), True, (255,255,255))
	screen.blit(score, (x, y))

def game_over_text():
	game_over = over_text.render("Game Over", True, (255,255,255))
	screen.blit(game_over, (200, 250))

running = True
while running:
	screen.fill([255, 255, 255])
	screen.blit(background, (0,0))
	showScore(textX, textY, score)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				playerX_change -= 4
			if event.key == pygame.K_RIGHT:
				playerX_change += 4
			if bullet_state != "fire":
				if event.key == pygame.K_SPACE:
					bullet_sound = mixer.Sound("music/laser.wav")
					bullet_sound.play()
					bulletX = playerX	
					fire_bullet(bulletX, playerY)
					

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or pygame.K_RIGHT:
				playerX_change = 0

	for i in range(num_enemies):
		enemyX[i] += enemyX_change[i]
		if enemyX[i] <= 0:
			enemyY[i] += enemyY_change[i]
			enemyX_change[i] = 1.3
		elif enemyX[i] >= 736:
			enemyY[i] += enemyY_change[i]
			enemyX_change[i] = -1.3

		collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
		if collision:
			bulletY = 460
			bullet_state = 'ready'
			score += 1
			enemyX[i] = random.randint(30, 729)
			enemyY[i] = random.randint(0, 80)
			collide_sound = mixer.Sound("music/collide.wav")
			collide_sound.play()

		enemy(enemyX[i], enemyY[i], i)

	for i in range(num_enemies):

		if enemyY[i] > 400:
			for j in range(num_enemies):
				enemyY[j] = 2000
			game_over_text()
			break



	if playerX + playerX_change > 20 and playerX + playerX_change < 660:
		playerX += playerX_change

	if bulletY <= -20:
		bulletY = 460
		bullet_state = "ready"

	if bullet_state is "fire":
		fire_bullet(bulletX, bulletY)
		bulletY -= bulletY_change
	
	player(playerX, playerY)
	pygame.display.update()

	


