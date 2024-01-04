import pygame
import sys
import random

pygame.init()

width = 800
length = 600
color_player = (3, 167, 187)
color_window = (0, 0, 0)
color_enemy = (182, 149, 192)
player_size = [50, 50]
principal_window = [139, 0, 139]
game_over = False
in_menu = True

# Player
player_posi = [width // 2, length - player_size[1] * 2]

# Enemy
enemy_size = 50
enemy_posi = [random.randint(0, width - enemy_size), 0]

# Window creation
window = pygame.display.set_mode((width, length))

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def detect_collision(player_posi, enemy_posi):
    px = player_posi[0]
    py = player_posi[1]
    ex = enemy_posi[0]
    ey = enemy_posi[1]

    if (ex >= px and ex < (px + player_size[0])) or (px >= ex and px < (ex + enemy_size)):
        if (ey >= py and ey < (py + player_size[0])) or (py >= ey and py < (ey + enemy_size)):
            return True
    return False

def show_menu():
    window.fill(principal_window)
    text_start = font.render("Press SPACE to Start", True, (255, 255, 255))
    window.blit(text_start, (width // 2 - 200, length // 2 - 10))
    pygame.display.flip()

# Main loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if in_menu:
        show_menu()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            in_menu = False  # Comienza el juego cuando se presiona SPACE

    else:
        keys = pygame.key.get_pressed()
        x = player_posi[0]

        if keys[pygame.K_LEFT]:
            x -= player_size[0]
            # Verificar si el jugador está fuera del borde izquierdo
            if x < 0:
                x = 0
        if keys[pygame.K_RIGHT]:
            x += player_size[0]
            # Verificar si el jugador está fuera del borde derecho
            if x > width - player_size[0]:
                x = width - player_size[0]

        player_posi = [x, player_posi[1]]

        window.fill(color_window)

        if enemy_posi[1] >= 0 and enemy_posi[1] < width:
            enemy_posi[1] += 20
        else:
            enemy_posi[0] = random.randint(0, width - enemy_size)
            enemy_posi[1] = 0

        if detect_collision(player_posi, enemy_posi):
            game_over = True

        pygame.draw.rect(window, color_enemy, (enemy_posi[0], enemy_posi[1], enemy_size, enemy_size))
        pygame.draw.rect(window, color_player, (player_posi[0], player_posi[1], player_size[0], player_size[1]))

        clock.tick(30)
        pygame.display.update()

# Mostrar "Game Over" directamente en la pantalla
text = font.render("GAME OVER", True, (0, 143, 57))
window.blit(text, (width // 2 - 100, length // 2 - 50))
pygame.display.flip()

# Esperar unos segundos antes de salir
pygame.time.wait(2000)
sys.exit()