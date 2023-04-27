import pygame
from text_and_font import text as tx

class player:
    def __init__(self, name, color, y):
        self.name = name
        self.color = color
        self.y = y

        self.points = 0
        self.warriors = 7

        self.text_name = tx(self.name, 20, self.y)
        self.text_points = tx("Points: " + str(self.points), 20, self.y + 35, 20)

    def draw(self, window):
        # pygame.draw.rect(window, (255, 255, 255), pygame.Rect(0, 0, 100, 100))
        self.text_points = tx("Points: " + str(self.points), 20, self.y + 35, 20)
        for i in range(self.warriors):
            pygame.draw.rect(window, self.color, pygame.Rect(20 + i*15, self.y + 60, 10, 10))
        self.text_name.draw(window)
        self.text_points.draw(window)
    