import pygame
from random import randint
from pygame import gfxdraw
import turtle

# Инициализируем Pygame
pygame.init()

# Устанавливаем размер окна
size = (1000, 750)

# Создаем окно Pygame
screen = pygame.display.set_mode(size)

# Устанавливаем заголовок окна
pygame.display.set_caption("Moveable Rectangle")

# Устанавливаем начальные позиции точек
point1 = [size[0] // 4, size[1] // 4]
point2 = [3 * size[0] // 4, size[1] // 4]
point3 = [3 * size[0] // 4, 3 * size[1] // 4]
point4 = [size[0] // 4, 3 * size[1] // 4]

# Определяем координаты новой точки
point5 = [randint(size[0] // 4, 3 * size[0] // 4),
          randint(size[1] // 4, 3 * size[1] // 4)]

# Определяем координаты текущей точки
point6 = [0, 0]

# Устанавливаем начальный замороженный статус точек
frozen1 = False
frozen2 = False
frozen3 = False
frozen4 = False

# Устанавливаем цвет точек
color = (255, 0, 0)
color_dot = (0, 255, 255)

# Устанавливаем скорость перемещения точек
speed = 5


def draw(point1, point2, point3, point4, point5, color, color_dot):
    # Рисуем прямоугольник
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, color, point1, 5)
    pygame.draw.circle(screen, color_dot, point5, 5)
    pygame.draw.circle(screen, color, point2, 5)
    pygame.draw.circle(screen, color, point3, 5)
    pygame.draw.circle(screen, color, point4, 5)
    pygame.draw.line(screen, color, point1, point2, 2)
    pygame.draw.line(screen, color, point2, point3, 2)
    pygame.draw.line(screen, color, point3, point4, 2)
    pygame.draw.line(screen, color, point4, point1, 2)


# Основной игровой цикл
running = True
new_flag = False
n = 5000

while running:

    if not new_flag:
        # Обрабатываем события
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    new_flag = True

            # Обрабатываем события мыши
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if ((event.pos[0] - point1[0]) ** 2 + (
                            event.pos[1] - point1[1]) ** 2) <= 100:
                        frozen1 = False
                    elif ((event.pos[0] - point2[0]) ** 2 + (
                            event.pos[1] - point2[1]) ** 2) <= 100:
                        frozen2 = False
                    elif ((event.pos[0] - point3[0]) ** 2 + (
                            event.pos[1] - point3[1]) ** 2) <= 100:
                        frozen3 = False
                    elif ((event.pos[0] - point4[0]) ** 2 + (
                            event.pos[1] - point4[1]) ** 2) <= 100:
                        frozen4 = False
            elif event.type == pygame.MOUSEMOTION:
                if not frozen1:
                    if ((event.pos[0] - point1[0]) ** 2 + (
                            event.pos[1] - point1[1]) ** 2) <= 100:
                        point1[0] += event.rel[0]
                        point1[1] += event.rel[1]
                if not frozen2:
                    if ((event.pos[0] - point2[0]) ** 2 + (
                            event.pos[1] - point2[1]) ** 2) <= 100:
                        point2[0] += event.rel[0]
                        point2[1] += event.rel[1]
                if not frozen3:
                    if ((event.pos[0] - point3[0]) ** 2 + (
                            event.pos[1] - point3[1]) ** 2) <= 100:
                        point3[0] += event.rel[0]
                        point3[1] += event.rel[1]
                if not frozen4:
                    if ((event.pos[0] - point4[0]) ** 2 + (
                            event.pos[1] - point4[1]) ** 2) <= 100:
                        point4[0] += event.rel[0]
                        point4[1] += event.rel[1]

    # Рисуем прямоугольник
    draw(point1, point2, point3, point4, point5, color, color_dot)

    # Обновляем экран
    pygame.display.update()

    n = 5000
    if new_flag:
        # Создание поверхности
        surface = pygame.Surface((1000, 750))
        surface.fill((255, 255, 255))
        pygame.draw.circle(surface, color, point1, 5)
        pygame.draw.circle(surface, color_dot, point5, 5)
        pygame.draw.circle(surface, color, point2, 5)
        pygame.draw.circle(surface, color, point3, 5)
        pygame.draw.circle(surface, color, point4, 5)
        pygame.draw.line(surface, color, point1, point2, 2)
        pygame.draw.line(surface, color, point2, point3, 2)
        pygame.draw.line(surface, color, point3, point4, 2)
        pygame.draw.line(surface, color, point4, point1, 2)

        mas = [point1, point2, point3, point4, point5]
        q = int(input("Введите коэффициент: "))
        q = 1 / q
        for i in range(n):
            value = randint(1, 4)
            if value == 1:
                point5[0] = (point5[0] + point1[0]) / (1 + q)
                point5[1] = (point5[1] + point1[1]) / (1 + q)
                pygame.draw.circle(surface, color, point5, 5)
            elif value == 2:
                point5[0] = (point5[0] + point2[0]) / (1 + q)
                point5[1] = (point5[1] + point2[1]) / (1 + q)
                pygame.draw.circle(surface, color, point5, 5)
            elif value == 3:
                point5[0] = (point5[0] + point3[0]) / (1 + q)
                point5[1] = (point5[1] + point3[1]) / (1 + q)
                pygame.draw.circle(surface, color, point5, 5)
            elif value == 4:
                point5[0] = (point5[0] + point4[0]) / (1 + q)
                point5[1] = (point5[1] + point4[1]) / (1 + q)
                pygame.draw.circle(surface, color, point5, 5)
            # отобразить поверхность на экране
            screen.blit(surface, (1000, 750))

            # обновить экран
            pygame.display.flip()
        running = False

# Завершаем Pygame
pygame.quit()

