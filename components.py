import pygame
import random
import config
class Ground:
    ground_level = 500
    def __init__(self, win_width):
        self.x, self.y = 0, Ground.ground_level
        self.img = config.base_img
        self.rect = self.img.get_rect(topleft=(0, self.y))

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))


class Pipes:
    width = 52
    opening = 200

    def __init__(self, win_width):
        self.x = win_width
        self.bottom_height = random.randint(10, 300)
        self.top_height = Ground.ground_level - self.bottom_height - self.opening
        self.bottom_rect, self.top_rect = pygame.Rect(0, 0, 0, 0), pygame.Rect(0, 0, 0, 0)
        self.passed = False
        self.off_screen = False
        self.pipe_bottom = config.pipe_img
        self.pipe_top = pygame.transform.flip(config.pipe_img, False, True)

    def draw(self, window):
        self.bottom_rect = pygame.Rect(self.x, Ground.ground_level - self.bottom_height, self.width, self.bottom_height)
        self.top_rect = pygame.Rect(self.x, 0, self.width, self.top_height)

        window.blit(self.pipe_top, (self.x, self.top_rect.bottom - self.pipe_top.get_height()))
        window.blit(self.pipe_bottom, (self.x, self.bottom_rect.top))

    def update(self):
        self.x -= 1
        if self.x + Pipes.width <= 52:
            self.passed = True
        if self.x <= -self.width - 100:
            self.off_screen = True