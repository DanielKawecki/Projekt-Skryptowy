import pygame

pygame.font.init()

class text:
    def __init__(self, text, x, y, size=30, color=[0, 0, 0]):
        self.text = text

        self.x = x
        self.y = y

        self.size = size
        self.color = color

    def draw(self, window):
        font = pygame.font.SysFont('Arial', self.size)
        text_surface = font.render(self.text, True, self.color)

        # pygame.draw.rect(window, self.color)
        window.blit(text_surface, (self.x, self.y))

class button:
    def __init__(self, text, x, y, size=30, color=[0, 0, 0]):
        self.text = text

        self.x = x
        self.y = y

        self.size = size
        self.color = color

    def click(self, mouse):
        if self.x-10 < mouse[0] < self.x + 150 and self.y-10 < mouse[1] < self.y + 50:
            # self.color = (255, 0, 0)
            return True 

    def draw(self, window):
        font = pygame.font.SysFont('Arial', self.size)
        text_surface = font.render(self.text, True, self.color)

        # pygame.draw.rect(window, self.color)
        pygame.draw.rect(window, (20, 20, 20), pygame.Rect(self.x-10, self.y-10, 150, 50))
        window.blit(text_surface, (self.x, self.y))

class cancel_button(button):
    def __init__(self, x, y, size=30, color=[0, 0, 0]):
        self.text = "Cancel"

        self.x = x
        self.y = y

        self.size = size
        self.color = color
  
    def click(self, mouse):
        if self.x-10 < mouse[0] < self.x + 150 and self.y-10 < mouse[1] < self.y + 50:
            return True 
        
class pass_button(button):
    def __init__(self, x, y, size=30, color=[0, 0, 0]):
        self.text = "Pass"

        self.x = x
        self.y = y

        self.size = size
        self.color = color
  
    def click(self, mouse):
        if self.x-10 < mouse[0] < self.x + 150 and self.y-10 < mouse[1] < self.y + 50:
            return True 