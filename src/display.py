import pygame
from math import log


def exit_game():
    pygame.display.quit()
    pygame.quit()
    print("Exit Game")


class Display:

    def __init__(self, size):
        self.size = size
        pygame.init()
        self.window = pygame.display.set_mode((540, 540))

        pygame.display.update()

    def print_grid(self, grid):
        pygame.draw.rect(self.window, (50, 50, 50), (20, 20, 500, 500))
        pygame.display.update()
        size_square = 500 // self.size
        font = pygame.font.SysFont(None, 30)
        for j in range(self.size):
            for i in range(self.size):
                if grid[i][j] == 0:
                    pygame.draw.rect(self.window, (50, 50, 50), (
                        20 + size_square * i + 1, 20 + size_square * j + 1, size_square - 2, size_square - 2))
                else:
                    rect = pygame.draw.rect(self.window, (255,
                                                          255 - log(grid[i][j], 2) * 20, 20),
                                            (20 + size_square * i + 1,
                                             20 + size_square * j + 1,
                                             size_square - 2, size_square - 2))
                    number = font.render(str(grid[i][j]), 1, (10, 10, 10))
                    text_pos = number.get_rect()
                    text_pos.centerx = rect.centerx
                    text_pos.centery = rect.centery
                    self.window.blit(number, text_pos)
        pygame.display.update()
