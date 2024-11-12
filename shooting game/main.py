import pygame
import os

pygame.font.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooting Game!")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
                    #border placement in center -5 to make it stay aligned and also enlargend, 0= y 10=w
BORDER = pygame.Rect(WIDTH // 2 - 5, 0, 10, HEIGHT)

HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 3
SHOOTER_WIDTH, SHOOTER_HEIGHT = 55, 40

#To customize the event
GREEN_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

GREEN_SHOOTER_IMAGE = pygame.image.load(os.path.join('Assets', 'girl.png'))
GREEN_SHOOTER = pygame.transform.rotate(pygame.transform.scale(GREEN_SHOOTER_IMAGE,(SHOOTER_WIDTH, SHOOTER_HEIGHT)), 90)

RED_SHOOTER_IMAGE = pygame.image.load(os.path.join('Assets', 'guy.png'))
RED_SHOOTER = pygame.transform.rotate(pygame.transform.scale(RED_SHOOTER_IMAGE,(SHOOTER_WIDTH, SHOOTER_HEIGHT)), 270)

BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'bkg.png')), (WIDTH, HEIGHT))

def draw_window(red, green, red_bullets, green_bullets, red_health, green_health):
    WIN.blit(BACKGROUND,(0,0)) #WIN refers to the screen
    pygame.draw.rect(WIN, BLACK, BORDER)

    red_health_text = HEALTH_FONT.render("Health: " +str(red_health), 1, WHITE)
    WIN.blit(red_health_text, (700, 10))
    WIN.blit(RED_SHOOTER, (red.x, red.y))

    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)
    
    green_health_text = HEALTH_FONT.render("Health: " +str(green_health), 1, WHITE)
    WIN.blit(green_health_text, (10, 10))
    WIN.blit(GREEN_SHOOTER, (green.x, green.y))

    for bullet in green_bullets:
        pygame.draw.rect(WIN, GREEN, bullet)

#moves w wasd
def green_handle_movement(keys_pressed, green):
    if keys_pressed[pygame.K_a] and green.x - VEL > 0: #LEFT
        green.x -=VEL
    if keys_pressed[pygame.K_d] and green.x + VEL + green.width < BORDER.x: #RIGHT
        green.x += VEL
    if keys_pressed[pygame.K_w] and green.y - VEL > 0: #UP
        green.y -= VEL
    if keys_pressed[pygame.K_s] and green.y + VEL + green.height < HEIGHT - 15: #DOWN
        green.y += VEL

def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width:
        red.x -=VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH:
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0: 
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 15:
        red.y += VEL

def main():
    red = pygame.Rect(700, 300, SHOOTER_WIDTH, SHOOTER_HEIGHT)
    green = pygame.Rect(100, 300, SHOOTER_WIDTH, SHOOTER_HEIGHT)
    red_bullets = []
    red_health = 10
    green_bullets = []
    green_health = 10
    draw_window(red, green, red_bullets, green_bullets, red_health, green_health)
    main()

if __name__ == "__main__":
    main()



