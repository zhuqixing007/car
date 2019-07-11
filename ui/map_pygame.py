import pygame
import sys
import time

def car_map():
    pygame.init()
    pygame.display.set_caption("地图")
    screen = pygame.display.set_mode((600, 295))
    background = pygame.image.load(r"D:\PycharmProjects\car\ui\map.png")
    i = 90
    while True:
        screen.blit(background, (0, 0))
        pygame.draw.circle(screen, (240, 0, 0), (i, 175), 4, 0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()
        if i == 90:
            time.sleep(1)
        i += 1
        time.sleep(0.008)
        if i > 450:
            i = 90
            time.sleep(1)

#
# car_map()
# print(1)