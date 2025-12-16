import pygame
from sys import exit
import config
import components
import population
import player
pygame.init()
clock = pygame.time.Clock()



btn_manual = pygame.Rect(config.win_width//2 - 100, config.win_height - 140, 200, 50)
btn_auto = pygame.Rect(config.win_width//2 - 100, config.win_height - 70, 200, 50)
btn_restart = pygame.Rect(config.win_width//2 - 100, config.win_height - 140, 200, 50)

pop = population.Population(100) 
ground = components.Ground(config.win_width)

def draw_game_over_screen():
    if config.game_over_img:
        go_x = config.win_width // 2 - config.game_over_img.get_width() // 2
        config.window.blit(config.game_over_img, (go_x, 100))
    
    if config.scoreboard_img:
        panel_x = config.win_width // 2 - config.scoreboard_img.get_width() // 2
        panel_y = config.win_height // 2 - config.scoreboard_img.get_height() // 2 - 20
        config.window.blit(config.scoreboard_img, (panel_x, panel_y))
        
        medal = None
        if config.score >= 40:
            medal = config.medal_imgs[3] 
        elif config.score >= 30:
            medal = config.medal_imgs[2] 
        elif config.score >= 20:
            medal = config.medal_imgs[1] 
        elif config.score >= 10:
            medal = config.medal_imgs[0] 
            
        if medal:
            config.window.blit(medal, (panel_x + 26, panel_y + 44))
            
        text_color = (255, 255, 255) 
        shadow_color = (0, 0, 0)
        
        score_surface = config.score_font.render(str(config.score), True, text_color)
        config.window.blit(score_surface, (panel_x + 200, panel_y + 35))
        
        hs_surface = config.score_font.render(str(config.high_score), True, text_color)
        config.window.blit(hs_surface, (panel_x + 200, panel_y + 75))
        center_x = config.win_width // 2
        btn_y = panel_y + config.scoreboard_img.get_height() + 20
        
        if config.btn_ok_img:
            ok_x = center_x - config.btn_ok_img.get_width() - 10
            config.window.blit(config.btn_ok_img, (ok_x, btn_y))
            config.btn_ok_rect = pygame.Rect(ok_x, btn_y, config.btn_ok_img.get_width(), config.btn_ok_img.get_height())

        if config.btn_menu_img:
            menu_x = center_x + 10
            config.window.blit(config.btn_menu_img, (menu_x, btn_y))
            config.btn_menu_rect = pygame.Rect(menu_x, btn_y, config.btn_menu_img.get_width(), config.btn_menu_img.get_height())

def generate_pipes():
    config.pipes.append(components.Pipes(config.win_width))

def quit_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.KEYDOWN:
            if config.game_state == "menu":
                if event.key == pygame.K_m:
                    config.game_state = "manual"
                    reset_game()
                elif event.key == pygame.K_a:
                    config.game_state = "auto"
                    reset_game()

            elif config.game_state == "manual":
                if event.key == pygame.K_SPACE:
                    for p in pop.players:
                        p.bird_flap()
            
            elif config.game_state == "game_over":
                 if event.key == pygame.K_SPACE:
                     config.game_state = "manual"
                     reset_game()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            if config.game_state == "menu":
                if btn_manual.collidepoint(mouse_pos):
                    config.game_state = "manual"
                    reset_game()
                elif btn_auto.collidepoint(mouse_pos):
                    config.game_state = "auto"
                    reset_game()


            if config.game_state == "manual":
                for p in pop.players:
                    p.bird_flap()
            
            elif config.game_state == "game_over":
                if config.btn_ok_rect and config.btn_ok_rect.collidepoint(mouse_pos):
                    config.game_state = "manual"
                    reset_game()
                if config.btn_menu_rect and config.btn_menu_rect.collidepoint(mouse_pos):
                    config.game_state = "menu"
                    reset_game()
def reset_game():
    if config.score > config.high_score:
        config.high_score = config.score
    config.score = 0
    config.pipes.clear()
    if config.game_state == "auto":
        pop.players = [player.Player() for _ in range(100)]
    elif config.game_state == "manual":
        pop.players = [player.Player()]
    elif config.game_state == "menu":
        pop.players = []

def draw_menu():
    config.window.blit(config.bg_img, (0,0))
    config.ground.draw(config.window)
    
    title = config.font.render("Flappy Bird AI", True, (0, 0, 0))
    config.window.blit(title, (config.win_width//2 - title.get_width()//2, 100))

    
    text_manual = config.font.render("Press 'M' for Manual Mode", True, (0, 0, 0))
    text_auto = config.font.render("Press 'A' for Auto Mode", True, (0, 0, 0))
    text_tutorial1 = config.font.render("Tutorial:", True, (0,0,0))
    text_tutorial2 = config.font.render("Space to jump, don't hit the pipes!", True, (0,0,0))
    
    config.window.blit(text_manual, (config.win_width//3 - text_manual.get_width()//2 + 20, 250))
    config.window.blit(text_auto, (config.win_width//3 - text_auto.get_width()//2, 300))
    config.window.blit(text_tutorial1, (config.win_width//3 - text_auto.get_width()//2, 350))
    config.window.blit(text_tutorial2, (config.win_width//3 - text_auto.get_width()//2, 400))
    
    

    pygame.draw.rect(config.window, (100, 100, 100), btn_manual)
    text_manual = config.font.render("manual", True, (255, 255, 255))
    config.window.blit(text_manual, (btn_manual.centerx - text_manual.get_width()//2, btn_manual.centery - text_manual.get_height()//2))
    

    pygame.draw.rect(config.window, (100, 100, 100), btn_auto)
    text_auto = config.font.render("auto", True, (255, 255, 255))
    config.window.blit(text_auto, (btn_auto.centerx - text_auto.get_width()//2, btn_auto.centery - text_auto.get_height()//2))
    
    pygame.display.flip()

def draw_score():
    score_surface = config.font.render(f'Score: {config.score}', True, (255, 255, 255))
    config.window.blit(score_surface, (10, 10))
    
    hs_surface = config.font.render(f'High Score: {config.high_score}', True, (255, 255, 255))
    config.window.blit(hs_surface, (10, 40))


def main():
    pipes_spawn_time = 10

    while True:
        quit_game()

        if config.game_state == "menu":
            draw_menu()
        
        else: 
            if config.bg_img:
                config.window.blit(config.bg_img, (0, 0))
            else:
                config.window.fill((0,0,0))
            
            config.ground.draw(config.window)

            if config.game_state != "game_over":
                if pipes_spawn_time <= 0:
                    generate_pipes()
                    pipes_spawn_time = 300 
                pipes_spawn_time -= 1

                for p in config.pipes:
                    p.draw(config.window)
                    was_passed = p.passed
                    p.update()
                    if p.passed and not was_passed:
                        config.score += 1
                    if p.off_screen:
                        config.pipes.remove(p)
                
                draw_score()
            else:
                for p in config.pipes:
                    p.draw(config.window)


            if config.game_state == "manual":
                if not pop.players:
                    pop.players = [player.Player()]
                
                for p in pop.players:
                    if p.alive:
                        p.update(config.ground)
                        p.draw(config.window)
                    else:
                        if config.score > config.high_score:
                            config.high_score = config.score
                        config.game_state = "game_over"
                        p.draw(config.window)
            
            elif config.game_state == "auto":
                if not pop.extinct():
                    pop.update_live_players()
                else:
                    config.pipes.clear()
                    pop.natural_selection()

            if config.game_state == "game_over":
                draw_game_over_screen()

            clock.tick(60)
            pygame.display.flip()

if __name__ == "__main__":
    main()