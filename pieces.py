import pygame

# Textury
red_overall = pygame.image.load("textures/red_overall.png")
green_overall = pygame.image.load("textures/green_overall.png")

rt = pygame.image.load("textures/road_turn.png")
sr = pygame.image.load("textures/straight_road.png")
tr = pygame.image.load("textures/three_roads.png")
fr = pygame.image.load("textures/four_roads.png")
src = pygame.image.load("textures/straight_road_castle.png")

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

        # Właściwości
        self.width = self.height = 100
        self.color = [255, 255, 255]      

    def hover(self, mx, my):
        if self.x <= mx < (self.x + self.width) and self.y <= my < (self.y + self.height):
            self.color = [200, 200, 200]
            return True
        else:
            self.color = [255, 255, 255]

        return False

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

    def draw(self, window):
        window.blit(self.texture, (self.x, self.y))
        if self.red == True:
            window.blit(red_overall, (self.x, self.y))
        elif self.correct == True and self.placed == False:
            window.blit(green_overall, (self.x, self.y))

class straight_road_castle(pieces):
    def __init__(self, x, y, grid_x, grid_y):
    
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
        self.top = 1
        self.right = 2
        self.bottom = 3
        self.left = 2  

        # Zakończenie drogi
        self.intersection = False

        # Właściwości
        self.width = self.height = 100
        self.texture = src
        self.red = False
        self.placed = False
        self.correct = False

class road_turn(pieces):
    def __init__(self, x, y, grid_x, grid_y):
    
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
        self.top = 3
        self.right = 3
        self.bottom = 2
        self.left = 2  

        # Zakończenie drogi
        self.intersection = False

        # Właściwości
        self.width = self.height = 100
        self.texture = rt
        self.red = False
        self.placed = False
        self.correct = False

class straight_road(pieces):
    def __init__(self, x, y, grid_x, grid_y):
    
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
        self.top = 2
        self.right = 3
        self.bottom = 2
        self.left = 3  

        # Zakończenie drogi
        self.intersection = False

        # Właściwości
        self.width = self.height = 100
        self.texture = sr
        self.red = False
        self.placed = False
        self.correct = False