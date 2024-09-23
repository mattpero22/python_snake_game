class Snake:
    def __init__(self, size):
        self.size=1
        self.speed=10
        self.direction='UP'

    def __str__(self):
        return f"Snake size {self.size}"
    
    def eat(self):
        self.size = self.size + 1
        pass

    def draw(self, surface):
        pass

    def move(self, key_input):

        pass
