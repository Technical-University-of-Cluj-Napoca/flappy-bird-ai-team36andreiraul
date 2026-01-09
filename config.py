import pygame
import os
import components

pygame.init()

win_width = 550
win_height = 720

bird_imgs = []
medal_imgs = []
try:
    bg_img = pygame.transform.scale(pygame.image.load(os.path.join("imgs", "bg.png")), (win_width, win_height))
    pipe_img = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "pipe.png")))
    base_img = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "base.png")))
    
    bird_imgs = [
        pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird_up.png"))),
        pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird_mid.png"))),
        pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird_down.png")))
    ]

    game_over_img = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "label_game_over.png")))
    
    scoreboard_img = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "panel_score.png")))
    
    medal_imgs = [
        pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "medal_bronze.png"))),
        pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "medal_silver.png"))),
        pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "medal_gold.png"))),
        pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "medal_platinum.png")))
    ]
    
    btn_menu_img = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "button_menu.png")))
    btn_ok_img = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "button_ok.png")))

except Exception as e:
    print("Error loading images:", e)
    bg_img = None
    pipe_img = None
    base_img = None
    bird_imgs = [None, None, None]
    game_over_img = None
    scoreboard_img = None
    medal_imgs = [None] * 4
    btn_menu_img = None
    btn_ok_img = None


window = pygame.display.set_mode((win_width, win_height))
ground = components.Ground(win_width) 
pipes = []

font = pygame.font.SysFont('Arial', 30)
score_font = pygame.font.SysFont('Arial', 20, bold=True) 

game_state = "menu"
score = 0
high_score = 0


btn_ok_rect = None
btn_menu_rect = None

pygame.display.set_caption("Flappy Bird AI")