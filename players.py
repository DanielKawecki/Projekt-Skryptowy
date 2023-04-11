import pygame

pygame.font.init()
font1 = pygame.font.SysFont('Arial', 35)
font2 = pygame.font.SysFont('Arial', 20)

class player:
    def __init__(self, name, color, y):
        self.name = name
        self.color = color
        self.y = y

        self.points = 0
        self.text_name = font1.render(self.name, True, (0, 0, 0))
        self.text_points = font2.render('Points: '+str(self.points), True, (0, 0, 0))

    def draw(self, window):
        window.blit(self.text_name, (20, self.y))
        window.blit(self.text_points, (20, self.y+35))
    