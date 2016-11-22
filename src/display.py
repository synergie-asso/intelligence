import pygame
from math import log


class Display:
    def __init__(self, size):
        self.size = size
        pygame.init()
        self.window = pygame.display.set_mode((540, 540))
        red = (255, 0, 0)

        pygame.display.update()

    def quit(self):
        pygame.display.quit()
        pygame.quit()
        print("Exit Game")

    def print_grid(self, grid):
        pygame.draw.rect(self.window, (50, 50, 50), (20, 20, 500, 500));
        pygame.display.update()
        print();
        sizeSquare = 500 // self.size
        font = pygame.font.SysFont(None, 30)
        for j in range(self.size):
            for i in range(self.size):
                if grid[i][j] == 0:
                    pygame.draw.rect(self.window, (50, 50, 50), (
                    20 + sizeSquare * i + 1, 20 + sizeSquare * j + 1, sizeSquare - 2, sizeSquare - 2));
                else:
                    rect = pygame.draw.rect(self.window, (255,
                                                          255 - log(grid[i][j], 2) * 20, 20),
                                            (20 + sizeSquare * i + 1,
                                             20 + sizeSquare * j + 1,
                                             sizeSquare - 2, sizeSquare - 2))
                    number = font.render(str(grid[i][j]), 1, (10, 10, 10))
                    textpos = number.get_rect()
                    textpos.centerx = rect.centerx
                    textpos.centery = rect.centery
                    print(textpos)
                    self.window.blit(number, textpos)
        pygame.display.update()
