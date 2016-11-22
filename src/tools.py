import pygame
from pygame.locals import *


def new_direction():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return 0
            if event.type == KEYDOWN and event.key == K_LEFT:
                return 2
            if event.type == KEYDOWN and event.key == K_UP:
                return 1
            if event.type == KEYDOWN and event.key == K_RIGHT:
                return -2
            if event.type == KEYDOWN and event.key == K_DOWN:
                return -1


def fusion(carre1):
    return carre1 * 2


def isFusion(carre1, carre2):
    return carre1 == carre2


def win(tab):
    for i in range(len(tab)):
        if tab[i] == 64:
            return True
    return False


def check(grid, x, y, i, j):
    if i < 0 or i > len(grid) - 1 or j < 0 or j > len(grid) - 1:
        return False
    return grid[i][j] == grid[x][y]


def lose(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == 0:
                return False
            else:
                if check(grid, i, j, i - 1, j) or check(grid, i, j, i + 1, j) or check(grid, i, j, i, j - 1) or check(
                        grid, i, j, i, j + 1):
                    return False
    return True
