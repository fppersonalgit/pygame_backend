import pygame
import uuid
import random

class Actor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.player_id = str(uuid.uuid4())  # auto-generating
        self.x = random.randint(200, 300)
        self.y = random.randint(400, 500)
        self.width = 50
        self.height = 50
        self.color = self.get_random_color()
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def get_random_color(self):
        return random.choice([(255, 0, 0), (0, 255, 0), (0, 0, 255)])



