import pygame
import random
import math

pygame.init()
window = pygame.display.set_mode((800, 600))

# title and icon
pygame.display.set_caption("first_game")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)

# loading images
player_img = pygame.image.load("arcadespace.png")
playery = 480
playerx = 380
playerx_change = 0
playery_change = 0

# creating enemy
enemy_img = pygame.image.load("enemy.png")
enemyx = random.randint(0, 736)
enemyy = random.randint(30, 150)
enemyx_change = 0.3
enemyy_change = 20

# bullet configuration
bullet_img = pygame.image.load("bullet.png")
bulletx = 0
bullety = 480
bulletx_change = 0
bullety_change = 0.5
bullet_state = "ready"

score = 0
font = pygame.font.Font("freesansbold.ttf", 32)

txtx = 10
txty = 10


def show_score(x, y):
    scores = font.render("score :" + str(score), True, (255, 255, 255))
    window.blit(scores, (x, y))


over_font = pygame.font.Font("freesansbold.ttf", 64)


def game_over():
    over = over_font.render("Game over", True, (255, 255, 255))
    window.blit(over, (200, 250))


def player(x, y):
    window.blit(player_img, (x, y))


def enemy(x, y):
    window.blit(enemy_img, (x, y))


def fire(x, y):
    global bullet_state
    bullet_state = "fire"
    window.blit(bullet_img, (x, y))


# collision
def collision(a, b, c, d):
    distance = math.sqrt(math.pow(a - c, 2) + math.pow(b - d, 2))
    if distance <= 28:
        return True


while True:
    window.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerx_change = 0.3
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletx = playerx
                    fire(bulletx, bullety)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change = 0

    # player movement
    playerx += playerx_change
    playery += playery_change
    if playerx <= 0:
        playerx = 0
    elif playerx >= 736:
        playerx = 736

    # enemy movement

    enemyx += enemyx_change
    if enemyx <= 0:
        enemyx_change = 0.4
        enemyy += enemyy_change
    elif enemyx >= 736:
        enemyx_change = -0.4
        enemyy += enemyy_change

    if enemyy >= 420:
        enemyy = 2000
        game_over()

    # bullet movement
    if bullety <= 0:
        bullety = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire(bulletx, bullety)
        bullety -= bullety_change

    collision_bullet = collision(enemyx, enemyy, bulletx, bullety)
    if collision_bullet:
        bullety = 480
        bullet_state = "ready"
        score += 1
        enemyx = random.randint(0, 736)
        enemyy = random.randint(30, 150)

    player(playerx, playery)
    enemy(enemyx, enemyy)
    show_score(txtx, txty)
    pygame.display.update()
