import pygame

class GameBoard:
    def __init__(self):
        self.width = 600
        self.height = 600
        self.tile_size = 30
        pass


    def draw_grid(self, screen):
        game_surface = pygame.Surface((self.width,self.height))
        
        for x in range(0, self.width, self.tile_size):
            for y in range(0, self.height, self.tile_size):
                rect = pygame.Rect(x,y, self.tile_size, self.tile_size)
                pygame.draw.rect(game_surface, "#3c3c3b", rect, 1)

        screen.blit(game_surface, (100,100))
