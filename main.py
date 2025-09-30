import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Dimensões da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Goal Goal")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 50, 50)
BLUE = (50, 50, 200)
GREEN = (50, 200, 50)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Jogadores
player_size = 50
player1 = pygame.Rect(100, HEIGHT // 2 - player_size // 2, player_size, player_size)
player2 = pygame.Rect(WIDTH - 150, HEIGHT // 2 - player_size // 2, player_size, player_size)
player_speed = 5

# Bola
ball_size = 30
ball = pygame.Rect(WIDTH // 2 - ball_size // 2, HEIGHT // 2 - ball_size // 2, ball_size, ball_size)
ball_speed_x, ball_speed_y = 4, 4

# Placar
score1, score2 = 0, 0
font = pygame.font.SysFont(None, 50)


# Função para desenhar elementos
def draw():
    screen.fill(GREEN)

    # Desenha jogadores
    pygame.draw.rect(screen, RED, player1)
    pygame.draw.rect(screen, BLUE, player2)

    # Desenha bola
    pygame.draw.ellipse(screen, WHITE, ball)

    # Desenha placar
    score_text = font.render(f"{score1} : {score2}", True, BLACK)
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))

    pygame.display.flip()


# Loop principal
running = True
while running:
    clock.tick(FPS)

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Teclas pressionadas
    keys = pygame.key.get_pressed()
    # Player 1 (WASD)
    if keys[pygame.K_w] and player1.top > 0:
        player1.y -= player_speed
    if keys[pygame.K_s] and player1.bottom < HEIGHT:
        player1.y += player_speed
    if keys[pygame.K_a] and player1.left > 0:
        player1.x -= player_speed
    if keys[pygame.K_d] and player1.right < WIDTH // 2:
        player1.x += player_speed

    # Player 2 (Setas)
    if keys[pygame.K_UP] and player2.top > 0:
        player2.y -= player_speed
    if keys[pygame.K_DOWN] and player2.bottom < HEIGHT:
        player2.y += player_speed
    if keys[pygame.K_LEFT] and player2.left > WIDTH // 2:
        player2.x -= player_speed
    if keys[pygame.K_RIGHT] and player2.right < WIDTH:
        player2.x += player_speed

    # Movimento da bola
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Colisões com paredes
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    # Colisões com jogadores
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x *= -1

    # Gols
    if ball.left <= 0:
        score2 += 1
        ball.center = (WIDTH // 2, HEIGHT // 2)
        ball_speed_x *= -1
    if ball.right >= WIDTH:
        score1 += 1
        ball.center = (WIDTH // 2, HEIGHT // 2)
        ball_speed_x *= -1

    # Desenha tudo
    draw()

pygame.quit()
sys.exit()
