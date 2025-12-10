import config
import player

class Population:
    def __init__(self):
        self.players = player.Player()

    def update_live_players(self):
        if self.players.alive:
            self.players.think()
            self.players.update(config.ground)
            self.players.draw(config.window)