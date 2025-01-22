import pygame


pygame.init()

class deadscreen:
    def __init__(self, screen_width, screen_height):
        self.x = screen_width//2
        self.y = screen_height//2
        self.image = pygame.image.load("./Assets/Other/GameOver.png")
    
