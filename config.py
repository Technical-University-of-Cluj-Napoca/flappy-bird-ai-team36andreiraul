import pygame
import components

pygame.init()

win_width = 550
win_height = 720

window = pygame.display.set_mode((win_width, win_height))
ground = components.Ground(win_width) 
pipes = []

font = pygame.font.SysFont('Arial', 30)
game_state = "menu"

score = 0
high_score = 0


pygame.display.set_caption("Flappy Bird AI")