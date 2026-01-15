import pygame
import random

class Person(pygame.sprite.Sprite):
    def __init__(self, x, y, birthday, game_display):
        super().__init__()
        self.birthday = birthday
        self.game_display = game_display
        self.x = x
        self.y = y
        self.radius = 20
        self.color = (random.randint(60, 240), random.randint(60, 240), random.randint(60, 240))

        # Load cake image (small, above the person)
        try:
            self.cake_img = pygame.image.load('images/cake.png')
            self.cake_img = pygame.transform.scale(self.cake_img, (28, 28))
        except:
            self.cake_img = None

    def draw(self, highlight=False):
        # Person circle
        pygame.draw.circle(self.game_display, self.color, (self.x, self.y), self.radius)
        if highlight:
            pygame.draw.circle(self.game_display, (255, 80, 80), (self.x, self.y), self.radius + 5, 4)

        # Birthday number inside circle
        font_num = pygame.font.SysFont("arial", 16, bold=True)
        num_text = font_num.render(str(self.birthday), True, (255,255,255) if sum(self.color) < 400 else (20,20,20))
        self.game_display.blit(num_text, (self.x - 8, self.y - 10))

        # Small cake above the person
        if self.cake_img:
            self.game_display.blit(self.cake_img, (self.x - 14, self.y - 50))
        else:
            # Fallback: tiny yellow circle as cake
            pygame.draw.circle(self.game_display, (255, 220, 80), (self.x, self.y - 35), 10)
            pygame.draw.circle(self.game_display, (255, 100, 100), (self.x, self.y - 35), 6)