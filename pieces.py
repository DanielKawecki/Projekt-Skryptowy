import pygame

# Textury
red_overall = pygame.image.load("textures/red_overall.png")
green_overall = pygame.image.load("textures/green_overall.png")

pygame.font.init()
font1 = pygame.font.SysFont('Arial', 15)

class empty_grid:
    def __init__(self, x, y, grid_x, grid_y):
        
        # Pozycja
        self.x = x
        self.y = y

        # Krawędzie
        self.top = 9
        self.right = 9
        self.bottom = 9
        self.left = 9  

        self.grid_x = grid_x
        self.grid_y = grid_y

        self.actual_piece = False

        # Właściwości
        self.width = self.height = 99
        # self.color = [255, 255, 255]     
        self.color = [199, 251, 113]  

        self.string = "x: "+str(self.grid_x)+", y: "+str(self.grid_y)
        self.text_name = font1.render(self.string, True, (0, 0, 0))

    def hover(self, mx, my):
        if self.x <= mx < (self.x + self.width) and self.y <= my < (self.y + self.height):
            self.color = [200, 200, 200]
            return True
        else:
            self.color = [255, 255, 255]  

        return False

    def draw(self, window):
        pygame.draw.rect(window, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
        # window.blit(self.text_name, (self.x+10, self.y+10))
        

class edge_grid:
    def __init__(self, x, y, grid_x, grid_y):
        
        # Pozycja
        self.x = x
        self.y = y

         # Krawędzie
        self.top = 9
        self.right = 9
        self.bottom = 9
        self.left = 9  

        self.grid_x = grid_x
        self.grid_y = grid_y

        # Właściwości
        self.width = self.height = 100
        self.color = [200, 200, 200]    

        self.actual_piece = False

    def hover(self, mx, my):
        pass

    def draw(self, window):
        pygame.draw.rect(window, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

class pieces:
    def rotate(self, direction):
        if direction == "right":
            self.top, self.right, self.bottom, self.left = self.left, self.top, self.right, self.bottom
            self.texture = pygame.transform.rotate(self.texture, 270)

        if direction == "left":
            self.top, self.right, self.bottom, self.left = self.right, self.bottom, self.left, self.top
            self.texture = pygame.transform.rotate(self.texture, 90)

    def hover(self, mx, my):
        pass

    def checkNeighbors(self, grid):
        if (grid[self.grid_x+1][self.grid_y].left == 9 and grid[self.grid_x-1][self.grid_y].right == 9) and (grid[self.grid_x][self.grid_y+1].top == 9 and grid[self.grid_x][self.grid_y-1].bottom == 9):
            self.red = True
            self.correct = False
            return False

        if (grid[self.grid_x+1][self.grid_y].left in (self.right, 9) and grid[self.grid_x-1][self.grid_y].right in (self.left, 9)) and (grid[self.grid_x][self.grid_y+1].top in (self.bottom, 9) and grid[self.grid_x][self.grid_y-1].bottom in (self.top, 9)):
            self.red = False
            self.correct = True
            return True
        
        self.red = True
        self.correct = False
        return False
    
    def own(self, name, color):
        self.monastery_owner = name
        self.owner_color = color

    def draw(self, window):
        window.blit(self.texture, (self.x, self.y))
        if self.red == True:
            window.blit(red_overall, (self.x, self.y))
        elif self.correct == True and self.placed == False:
            window.blit(green_overall, (self.x, self.y))
        elif self.monastery_owner != 9:
            pygame.draw.rect(window, (0, 0, 0), pygame.Rect(self.x + 40, self.y + 40, 20, 20))
            pygame.draw.rect(window, self.owner_color, pygame.Rect(self.x + 42, self.y + 42, 16, 16))
        elif self.road_owner != 9:
            pygame.draw.rect(window, (0, 0, 0), pygame.Rect(self.x + 40, self.y + 40, 20, 20))
            pygame.draw.rect(window, self.owner_color, pygame.Rect(self.x + 42, self.y + 42, 16, 16))

class piece_template(pieces):
    def __init__(self, top, right, bottom, left, intersect, separate, texture, bonus = False, monastery = False, x = 0, y = 0, grid_x = 0, grid_y = 0, roads_available = 0):
    
        # Pozycja
        self.x = x
        self.y = y

        self.grid_x = grid_x
        self.grid_y = grid_y

        # 1 - castle
        # 2 - road
        # 3 - field
        # 9 - empty grid
        
        # Krawędzie
        self.top = top
        self.right = right
        self.bottom = bottom
        self.left = left

        # Kto jest właścicelem
        self.field_owner = 9
        self.road_owner = 9
        self.castle_owner = 9
        self.monastery_owner = 9

        self.owner_color = (0, 0, 0)

        # Zakończenie drogi
        self.intersection = intersect
        self.roads_available = roads_available

        # Rozdzielność zamków
        self.separate = separate

        # Właściwości
        self.width = self.height = 100
        self.texture = texture
        self.red = False
        self.placed = False
        self.correct = False

        self.actual_piece = True

        # Bonusowe punkty
        self.bonus = bonus

        # Czy to klasztor?
        self.monastery = monastery
