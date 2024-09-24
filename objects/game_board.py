import pygame

class GameBoard:
    def __init__(self):
        self.width = 600
        self.height = 600
        self.tile_size = 30
        self.color = 'grey'
        self.x_offset = 100
        self.y_offset = 100
        pass


    def draw_grid(self, screen): 
        for x in range(self.x_offset, self.width + self.x_offset + 20, self.tile_size):
            pygame.draw.line(screen, self.color, (x, 100), (x, self.height + 100))
        for y in range(self.y_offset, self.height + self.y_offset + 20, self.tile_size):
            pygame.draw.line(screen, self.color, (100, y), (self.width + 100, y))