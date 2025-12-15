import pygame
from sys import exit
import config
import components
import population
import player
pygame.init()
clock = pygame.time.Clock()
pop = population.Population(100) 




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

        if event.type == pygame.MOUSEBUTTONDOWN:
             if config.game_state == "manual":
                for p in pop.players:
                    p.bird_flap()

def reset_game():
    if config.score > config.high_score:
        config.high_score = config.score
    config.score = 0
    config.pipes.clear()
    if config.game_state == "auto":
        pop.players = [player.Player() for _ in range(100)]
    elif config.game_state == "manual":
        pop.players = [player.Player()]

def draw_menu():
    config.window.fill((200, 200, 200)) 
    
    title = config.font.render("Flappy Bird AI", True, (0, 0, 0))
    config.window.blit(title, (config.win_width//2 - title.get_width()//2, 100))
    
    text_manual = config.font.render("Press 'M' for Manual Mode", True, (0, 0, 0))
    text_auto = config.font.render("Press 'A' for Auto Mode", True, (0, 0, 0))
    
    config.window.blit(text_manual, (config.win_width//2 - text_manual.get_width()//2, 250))
    config.window.blit(text_auto, (config.win_width//2 - text_auto.get_width()//2, 300))
    
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
            config.window.fill((0,0,0))
            config.ground.draw(config.window)

            if pipes_spawn_time <= 0:
                generate_pipes()
                pipes_spawn_time = 200
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
            if config.game_state == "manual":
                if pop.players == []:
                    pop.players = [player.Player()]
                for p in pop.players:
                    if p.alive:
                        p.update(config.ground)
                        p.draw(config.window)
                    else:
                        reset_game()
            
            elif config.game_state == "auto":
                if not pop.extinct():
                    pop.update_live_players()
                else:
                    config.pipes.clear()
                    pop.natural_selection()
                # if not pop.players.alive:
                #     reset_game()

            clock.tick(60)
            pygame.display.flip()

if __name__ == "__main__":
    main()