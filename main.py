import pygame
import random
import time

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 800, 600
FPS = 60
ENEMY_SIZE = 50
PLAYER_SIZE = 50
TIMER_FONT_SIZE = 30
SCORE_FONT_SIZE = 50

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Настройка экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Survival Game")

# Загрузка шрифтов
timer_font = pygame.font.Font(None, TIMER_FONT_SIZE)
score_font = pygame.font.Font(None, SCORE_FONT_SIZE)

# Игрок
player_pos = [WIDTH // 2, HEIGHT // 2]

# Враги
enemies = []

# Таймер
start_time = time.time()

# Функция для добавления врагов
def add_enemy():
    x_pos = random.randint(0, WIDTH - ENEMY_SIZE)
    y_pos = random.randint(0, HEIGHT - ENEMY_SIZE)
    enemies.append(pygame.Rect(x_pos, y_pos, ENEMY_SIZE, ENEMY_SIZE))

# Функция для проверки столкновений
def check_collision(player_rect):
    for enemy in enemies:
        if player_rect.colliderect(enemy):
            return True
    return False

# Главный игровой цикл
def game_loop():
    global player_pos
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_pos[0] > 0:
            player_pos[0] -= 5
        if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - PLAYER_SIZE:
            player_pos[0] += 5
        if keys[pygame.K_UP] and player_pos[1] > 0:
            player_pos[1] -= 5
        if keys[pygame.K_DOWN] and player_pos[1] < HEIGHT - PLAYER_SIZE:
            player_pos[1] += 5

        # Добавление врагов
        if random.random() < 0.05:  # Вероятность появления врага
            add_enemy()

        # Проверка столкновений
        player_rect = pygame.Rect(player_pos[0], player_pos[1], PLAYER_SIZE, PLAYER_SIZE)
        if check_collision(player_rect):
            running = False  # Игра заканчивается при столкновении

        # Отрисовка
        screen.fill(WHITE)
        pygame.draw.rect(screen, GREEN, player_rect)

        for enemy in enemies:
            pygame.draw.rect(screen, RED, enemy)

        # Обновление таймера
        elapsed_time = int(time.time() - start_time)
        timer_text = timer_font.render(f"Time: {elapsed_time}s", True, BLACK)
        screen.blit(timer_text, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)

    return elapsed_time

# Запуск игры
def main():
    final_score = game_loop()
    print(f"Game Over! You survived for {final_score} seconds.")
    pygame.quit()

if __name__ == "__main__":
    main()
