import pygame


class Weider():
    def __init__(self, screen):
        """Инициализирует персонажа и задает его начальную позицию."""
        self.screen = screen
        # Загрузка изображения персонажа и получение прямоугольника.
        self.image = pygame.image.load('images/weider.bmp')
        self.image.set_colorkey((255, 255, 255))
        self.image = pygame.transform.scale(self.image, (110, 60))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Каждый новый персонаж появляется у нижнего края экрана.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.centery

    def blitme(self):
        """Рисует персонажа в текущей позиции."""
        self.screen.blit(self.image, self.rect)