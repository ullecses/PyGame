import pygame

class Alien(pygame.sprite.Sprite):
    """класс одного экрана"""

    def __init__(self, screen):
        """инициализауия и задаём начальную позицию"""
        super(Alien, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/alien.png')
        NEW_ALIEN_SIZE = [80, 44]
        self.image = pygame.transform.scale(self.image, NEW_ALIEN_SIZE)
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """выводим пришельца на экран"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """перемещает пришельцев"""
        self.y += 0.1
        self.rect.y = self.y
