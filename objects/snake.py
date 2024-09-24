import pygame

class Snake:
    def __init__(self):
        self.size=1
        self.speed=5
        self.direction='up'
        self.x = 100
        self.y = 100
    

    def draw(self, surface):
        rect = pygame.Rect(self.x,self.y, 30, 30)
        pygame.draw.rect(surface, 'green', rect, 30)

    def update_position(self):
        if self.direction == 'up': self.y -= self.speed
        elif self.direction == 'down': self.y += self.speed
        elif self.direction == 'right': self.x += self.speed
        elif self.direction == 'left': self.x -= self.speed
