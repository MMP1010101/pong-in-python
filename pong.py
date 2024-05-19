import pygame
import sys

pygame.init()

#iterables
i = 0
j = 0
# colores
BLACK = (0,0,0)
WITHE = (255,255,255)

GREEN = (0, 255, 0)
RED   = (255, 0, 0)
BLUE  = (0, 0, 255)

# pantalla
SIZE = (800,600)
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# cordenadas
player_1x = SIZE[0] - 100
player_1y = SIZE[1] // 2
player_1y = player_1y - 45

player_2x = SIZE[0] - player_1x
player_2y = player_1y


xball = SIZE[0] //2
yball = SIZE[1] //2
print(yball)
efect_x = xball - 10
efect_y = yball

cordenadas_efecty = 20
cordenadas_efectx = 40

hitbox_start_p1 = 251
hitbox_start_p2 = 251
hitbox_final_p1 = 404
hitbox_final_p2 = 404

hitbox_start_p1 = player_1y
hitbox_final_p1 = player_1y + 80  

hitbox_start_p2 = player_2y
hitbox_final_p2 = player_2y + 80  

speed_ballx = 3
speed_bally = 0.5

speed_p1 = 0
speed_p2 = 0
# letras
font = pygame.font.Font("Retrogaming.ttf", 33)

# bucle principal
while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_o:
                speed_p1 = -3
            elif event.key == pygame.K_l:
                speed_p1 = 3
            elif event.key == pygame.K_w:
                speed_p2 = -3
            elif event.key == pygame.K_s:
                speed_p2 = 3

    
    # Lógica del juego

    if xball > 800:
        i = i + 1
        xball = SIZE[0] //2
        yball = SIZE[1] //2
    elif xball < 0:
        j = j + 1
        xball = SIZE[0] //2
        yball = SIZE[1] //2

    if yball > 600:
        yball = 0
    elif yball < 0:
        yball = 600

    if speed_ballx > 0:  
        if player_1x - 5 < xball < player_1x + 15:  
            if player_1y <= yball <= player_1y + 150:
                speed_ballx = -speed_ballx  

    if speed_ballx < 0:  
        if player_2x - 5 < xball < player_2x + 15:  
            if player_2y <= yball <= player_2y + 150:
                speed_ballx = -speed_ballx  
    xball = xball + speed_ballx
    
    if player_1y > 600:
        player_1y = 0
    elif player_1y < 0:
        player_1y = 600
    
    if player_2y > 600:
        player_2y = 0
    elif player_2y < 0:
        player_2y = 600
    hitbox_final_p1 = hitbox_final_p1 - speed_p1
    hitbox_start_p1 = hitbox_start_p1 + speed_p1
    hitbox_final_p2 = hitbox_final_p2 - speed_p2
    hitbox_start_p2 = hitbox_start_p2 + speed_p2
    player_1y = player_1y + speed_p1
    player_2y = player_2y + speed_p2

    if j == 5:
        sys.exit()
    elif i == 5:
        sys.exit()
    # Dibuja todo
    screen.fill(BLACK)
    pygame.draw.circle(screen, WITHE, (xball, yball), 5)
    pygame.draw.line(screen, WITHE, [xball, yball], [xball - cordenadas_efectx, yball - cordenadas_efecty], 3)
    pygame.draw.line(screen, WITHE, [xball, yball], [xball - cordenadas_efectx, yball + cordenadas_efecty], 3)
    pygame.draw.line(screen, WITHE, [xball, yball], [xball - cordenadas_efectx, yball], 3)
    pygame.draw.line(screen, WITHE, [xball, yball], [xball - cordenadas_efectx, yball - (cordenadas_efecty / 2)], 3)
    pygame.draw.line(screen, WITHE, [xball, yball], [xball - cordenadas_efectx, yball + (cordenadas_efecty / 2)], 3)
    pygame.draw.rect(screen, WITHE, (player_1x, player_1y, 15, 80))
    pygame.draw.rect(screen, WITHE, (player_2x, player_2y, 15, 80))
    screen.blit(font.render(f"Jugador {j}", 0, WITHE), (player_1x - 200, player_1y - 100))
    screen.blit(font.render(f"Jugador {i}", 0, WITHE), (player_2x - 50, player_2y - 100))
    pygame.display.flip()
    clock.tick(60)
