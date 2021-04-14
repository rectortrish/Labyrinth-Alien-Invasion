

class GameStats:
    #Tracking statistics for Alien Invasion

    def __init__ (self, ai_game):
        #Initilize stats

        self.settings = ai_game.settings
        self.reset_stats()

        self.game_active = False
        self.high_score = 0
        self.level = 1



        

    def reset_stats(self):

        #Initilize stats that can change during game play

        self.ship_left = self.settings.ship_limit
        self.score = 0
