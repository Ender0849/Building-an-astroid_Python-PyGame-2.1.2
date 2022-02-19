import pygame
import sys
from pygame.locals import *
import math
import numpy

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

a = 0

DISPLAYSURF = pygame.display.set_mode((1400, 800))
DISPLAYSURF.fill((0, 0, 0))

while True:
    pygame.display.update()

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    DISPLAYSURF.fill((0, 0, 0))

    #pygame.draw.circle(DISPLAYSURF, (255, 255, 255), (450, 650), 250, 1)
    #pygame.draw.circle(DISPLAYSURF, (255, 255, 255), (450, 150), 250, 1)
    #pygame.draw.circle(DISPLAYSURF, (255, 255, 255), (950, 650), 250, 1)
    #pygame.draw.circle(DISPLAYSURF, (255, 255, 255), (950, 150), 250, 1)

    #pygame.draw.rect(DISPLAYSURF, (0, 0, 0), (200, 650, 1000, 250))
    #pygame.draw.rect(DISPLAYSURF, (0, 0, 0), (200, -100, 1000, 250))
    #pygame.draw.rect(DISPLAYSURF, (0, 0, 0), (950, 150, 250, 500))
    #pygame.draw.rect(DISPLAYSURF, (0, 0, 0), (200, 150, 250, 500))

    for n in range(1, 1000):
        DISPLAYSURF.set_at((int(250 * (math.sin(n) ** 3) + 700), int(250 * (math.cos(n) ** 3) + 400)), (255, 255, 255))

    x1, y1 = 450, 400
    x2, y2 = 950, 400
    dl = 5
    xcoords = [x for x in range(x1, x2, dl if x1 < x2 else -dl)]
    ycoords = [y1] * len(xcoords)
    next_coords = list(zip(xcoords[1::2], ycoords[1::2]))
    last_coords = list(zip(xcoords[0::2], ycoords[0::2]))
    for (x1, y1), (x2, y2) in zip(next_coords, last_coords):
        start = (round(x1), round(y1))
        end = (round(x2), round(y2))
        pygame.draw.line(DISPLAYSURF, (0, 191, 255), start, end, 1)

    x11, y11 = 700, 150
    x12, y12 = 700, 650
    ycoords = [y for y in range(y11, y12, dl if y11 < y12 else -dl)]
    xcoords = [x11] * len(ycoords)
    next_coords = list(zip(xcoords[1::2], ycoords[1::2]))
    last_coords = list(zip(xcoords[0::2], ycoords[0::2]))
    for (x11, y11), (x12, y12) in zip(next_coords, last_coords):
        start = (round(x11), round(y11))
        end = (round(x12), round(y12))
        pygame.draw.line(DISPLAYSURF, (0, 191, 255), start, end, 1)

    x3, y3 = int(700 + 250 * math.cos(math.pi / 4)), int(400 + 250 * math.sin(math.pi / 4))
    x4, y4 = int(700 - 250 * math.cos(math.pi / 4)), int(400 - 250 * math.sin(math.pi / 4))
    c = round(math.sqrt(abs(x4 - x3) ** 2 + abs(y4 - y3) ** 2))
    dx = dl * abs(x4 - x3) / c
    dy = dl * abs(y4 - y3) / c
    xcoords = [x for x in numpy.arange(x3, x4, dx if x3 < x4 else -dx)]
    ycoords = [y for y in numpy.arange(y3, y4, dy if y3 < y4 else -dy)]
    next_coords = list(zip(xcoords[1::2], ycoords[1::2]))
    last_coords = list(zip(xcoords[0::2], ycoords[0::2]))
    for (x3, y3), (x4, y4) in zip(next_coords, last_coords):
        start = (round(x3), round(y3))
        end = (round(x4), round(y4))
        pygame.draw.line(DISPLAYSURF, (0, 191, 255), start, end, 1)

    x5, y5 = int(700 + 250 * math.cos(math.pi / 4 * 3)), int(400 + 250 * math.sin(math.pi / 4 * 3))
    x6, y6 = int(700 - 250 * math.cos(math.pi / 4 * 3)), int(400 - 250 * math.sin(math.pi / 4 * 3))
    c = round(math.sqrt(abs(x6 - x5) ** 2 + abs(y6 - y5) ** 2))
    dx = dl * abs(x6 - x5) / c
    dy = dl * abs(y6 - y5) / c
    xcoords = [x for x in numpy.arange(x5, x6, dx if x5 < x6 else -dx)]
    ycoords = [y for y in numpy.arange(y5, y6, dy if y5 < y6 else -dy)]
    next_coords = list(zip(xcoords[1::2], ycoords[1::2]))
    last_coords = list(zip(xcoords[0::2], ycoords[0::2]))
    for (x5, y5), (x6, y6) in zip(next_coords, last_coords):
        start = (round(x5), round(y5))
        end = (round(x6), round(y6))
        pygame.draw.line(DISPLAYSURF, (0, 191, 255), start, end, 1)

    x7, y7 = int(125 * math.cos(a) - 125 * math.cos(a) + 700), int(125 * math.sin(a) + 125 * math.sin(a) + 400)
    x8, y8 = int(125 * math.cos(a + math.pi) - 125 * math.cos(a) + 700), int(125 * math.sin(a + math.pi) + 125 * math.sin(a) + 400)
    if (x7 == x8):
        ycoords = [y for y in range(y7, y8, dl if y7 < y8 else -dl)]
        xcoords = [x7] * len(ycoords)
    elif (y7 == y8):
        xcoords = [x for x in range(x7, x8, dl if x7 < x8 else -dl)]
        ycoords = [y7] * len(xcoords)
    else:
        c = round(math.sqrt(abs(x8 - x7) ** 2 + abs(y8 - y7) ** 2))
        dx = dl * abs(x8 - x7) / c
        dy = dl * abs(y8 - y7) / c
        xcoords = [x for x in numpy.arange(x7, x8, dx if x7 < x8 else -dx)]
        ycoords = [y for y in numpy.arange(y7, y8, dy if y7 < y8 else -dy)]
    next_coords = list(zip(xcoords[1::2], ycoords[1::2]))
    last_coords = list(zip(xcoords[0::2], ycoords[0::2]))
    for (x7, y7), (x8, y8) in zip(next_coords, last_coords):
        start = (round(x7), round(y7))
        end = (round(x8), round(y8))
        pygame.draw.line(DISPLAYSURF, (152,251,152), start, end, 1)

    pygame.draw.circle(DISPLAYSURF, (135,206,250), (700, 400), 250, 2)

    pygame.draw.circle(DISPLAYSURF, (135,206,250), (-125 * math.cos(a) + 700, 125 * math.sin(a) + 400), 125, 2)

    pygame.draw.circle(DISPLAYSURF, (135, 206, 250), (-187.5 * math.cos(a) + 700, 187.5 * math.sin(a) + 400), 62.5, 2)

    pygame.draw.circle(DISPLAYSURF, (255,255,102), (125 * math.cos(a) - 125 * math.cos(a) + 700, 125 * math.sin(a) + 125 * math.sin(a) + 400), 6)
    pygame.draw.circle(DISPLAYSURF, (255, 255, 102), (125 * math.cos(a + math.pi / 2) - 125 * math.cos(a) + 700, 125 * math.sin(a + math.pi / 2) + 125 * math.sin(a) + 400), 6)
    pygame.draw.circle(DISPLAYSURF, (255, 255, 102), (125 * math.cos(a + math.pi * 1.5) - 125 * math.cos(a) + 700, 125 * math.sin(a + math.pi * 1.5) + 125 * math.sin(a) + 400), 6)
    pygame.draw.circle(DISPLAYSURF, (255, 255, 102), (125 * math.cos(a + math.pi) - 125 * math.cos(a) + 700, 125 * math.sin(a + math.pi) + 125 * math.sin(a) + 400), 6)
    # pygame.draw.circle(DISPLAYSURF, (220, 20, 60), (62.5 * math.cos(3 * a) - 187.5 * math.cos(a) + 700, 62.5 * math.sin(3 * a) + 187.5 * math.sin(a) + 400), 5)
    # pygame.draw.circle(DISPLAYSURF, (220, 20, 60), (62.5 * math.cos(3 * a + math.pi / 2) - 187.5 * math.cos(a) + 700, 62.5 * math.sin(3 * a + math.pi / 2) + 187.5 * math.sin(a) + 400), 5)
    # pygame.draw.circle(DISPLAYSURF, (220, 20, 60), (62.5 * math.cos(3 * a + math.pi * 1.5) - 187.5 * math.cos(a) + 700, 62.5 * math.sin(3 * a + math.pi * 1.5) + 187.5 * math.sin(a) + 400), 5)
    pygame.draw.circle(DISPLAYSURF, (220, 20, 60), (62.5 * math.cos(3 * a + math.pi) - 187.5 * math.cos(a) + 700, 62.5 * math.sin(3 * a + math.pi) + 187.5 * math.sin(a) + 400), 6)


    a += 0.017

    pygame.display.flip()
    FramePerSec.tick(FPS)