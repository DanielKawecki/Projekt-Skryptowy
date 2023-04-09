import pygame

# Textury
red_overall = pygame.image.load("textures/red_overall.png")
green_overall = pygame.image.load("textures/green_overall.png")

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

# class straight_road_castle(pieces):
#     def __init__(self, x, y, grid_x, grid_y):
    
#         # Pozycja
#         self.x = x
#         self.y = y

#         self.grid_x = grid_x
#         self.grid_y = grid_y

#         # 1 - castle
#         # 2 - road
#         # 3 - field
#         # 9 - empty grid
        
#         # Krawędzie
#         self.top = 1
#         self.right = 2
#         self.bottom = 3
#         self.left = 2  

#         # Kto jest właścicelem
#         self.field_owner = "none"
#         self.road_owner = "none"
#         self.castle_owner = "none"
#         self.monastry_owner = "none"

#         # Zakończenie drogi
#         self.intersection = False

#         # Rozdzielność zamków
#         self.separate = False

#         # Właściwości
#         self.width = self.height = 100
#         self.texture = src
#         self.red = False
#         self.placed = False
#         self.correct = False

class piece_template(pieces):
    def __init__(self, top, right, bottom, left, intersect, separate, texture, bonus = False, monastery = False, x = 0, y = 0, grid_x = 0, grid_y = 0):
    
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
        self.field_owner = "none"
        self.road_owner = "none"
        self.castle_owner = "none"
        self.monastry_owner = "none"

        # Zakończenie drogi
        self.intersection = intersect

        # Rozdzielność zamków
        self.separate = separate

        # Właściwości
        self.width = self.height = 100
        self.texture = texture
        self.red = False
        self.placed = False
        self.correct = False

        # Bonusowe punkty
        self.bonus = bonus

        # Czy to klasztor?
        self.monastery = monastery

# class road_turn(pieces):
#     def __init__(self, x, y, grid_x, grid_y):
    
#         # Pozycja
#         self.x = x
#         self.y = y

#         self.grid_x = grid_x
#         self.grid_y = grid_y

#         # 1 - castle
#         # 2 - road
#         # 3 - field
#         # 9 - empty grid
        
#         # Krawędzie
#         self.top = 3
#         self.right = 3
#         self.bottom = 2
#         self.left = 2  

#         # Kto jest właścicelem
#         self.field_owner = "none"
#         self.road_owner = "none"
#         self.castle_owner = "none"
#         self.monastry_owner = "none"

#         # Zakończenie drogi
#         self.intersection = False

#         # Rozdzielność zamków
#         self.separate = False

#         # Właściwości
#         self.width = self.height = 100
#         self.texture = rt
#         self.red = False
#         self.placed = False
#         self.correct = False

# class straight_road(pieces):
#     def __init__(self, x, y, grid_x, grid_y):
    
#         # Pozycja
#         self.x = x
#         self.y = y

#         self.grid_x = grid_x
#         self.grid_y = grid_y

#         # 1 - castle
#         # 2 - road
#         # 3 - field
#         # 9 - empty grid
        
#         # Krawędzie
#         self.top = 2
#         self.right = 3
#         self.bottom = 2
#         self.left = 3  

#         # Kto jest właścicelem
#         self.field_owner = "none"
#         self.road_owner = "none"
#         self.castle_owner = "none"
#         self.monastry_owner = "none"

#         # Zakończenie drogi
#         self.intersection = False

#         # Rozdzielność zamków
#         self.separate = False

#         # Właściwości
#         self.width = self.height = 100
#         self.texture = sr
#         self.red = False
#         self.placed = False
#         self.correct = False

# class three_roads(pieces):
#     def __init__(self, x, y, grid_x, grid_y):
    
#         # Pozycja
#         self.x = x
#         self.y = y

#         self.grid_x = grid_x
#         self.grid_y = grid_y

#         # 1 - castle
#         # 2 - road
#         # 3 - field
#         # 9 - empty grid
        
#         # Krawędzie
#         self.top = 2
#         self.right = 2
#         self.bottom = 2
#         self.left = 3  

#         # Kto jest właścicelem
#         self.field_owner = "none"
#         self.road_owner = "none"
#         self.castle_owner = "none"
#         self.monastry_owner = "none"

#         # Zakończenie drogi
#         self.intersection = True

#         # Rozdzielność zamków
#         self.separate = False

#         # Właściwości
#         self.width = self.height = 100
#         self.texture = tr
#         self.red = False
#         self.placed = False
#         self.correct = False

# class four_roads(pieces):
#     def __init__(self, x, y, grid_x, grid_y):
    
#         # Pozycja
#         self.x = x
#         self.y = y

#         self.grid_x = grid_x
#         self.grid_y = grid_y

#         # 1 - castle
#         # 2 - road
#         # 3 - field
#         # 9 - empty grid
        
#         # Krawędzie
#         self.top = 2
#         self.right = 2
#         self.bottom = 2
#         self.left = 2

#         # Kto jest właścicelem
#         self.field_owner = "none"
#         self.road_owner = "none"
#         self.castle_owner = "none"
#         self.monastry_owner = "none"

#         # Zakończenie drogi
#         self.intersection = True

#         # Rozdzielność zamków
#         self.separate = False

#         # Właściwości
#         self.width = self.height = 100
#         self.texture = fr
#         self.red = False
#         self.placed = False
#         self.correct = False

# class three_roads_castle(pieces):
#     def __init__(self, x, y, grid_x, grid_y):
    
#         # Pozycja
#         self.x = x
#         self.y = y

#         self.grid_x = grid_x
#         self.grid_y = grid_y

#         # 1 - castle
#         # 2 - road
#         # 3 - field
#         # 9 - empty grid
        
#         # Krawędzie
#         self.top = 1
#         self.right = 2
#         self.bottom = 2
#         self.left = 2

#         # Kto jest właścicelem
#         self.field_owner = "none"
#         self.road_owner = "none"
#         self.castle_owner = "none"
#         self.monastry_owner = "none"

#         # Zakończenie drogi
#         self.intersection = True

#         # Rozdzielność zamków
#         self.separate = False

#         # Właściwości
#         self.width = self.height = 100
#         self.texture = trc
#         self.red = False
#         self.placed = False
#         self.correct = False

# class right_turn_castle(pieces):
#     def __init__(self, x, y, grid_x, grid_y):
    
#         # Pozycja
#         self.x = x
#         self.y = y

#         self.grid_x = grid_x
#         self.grid_y = grid_y

#         # 1 - castle
#         # 2 - road
#         # 3 - field
#         # 9 - empty grid
        
#         # Krawędzie
#         self.top = 1
#         self.right = 2
#         self.bottom = 2
#         self.left = 3

#         # Kto jest właścicelem
#         self.field_owner = "none"
#         self.road_owner = "none"
#         self.castle_owner = "none"
#         self.monastry_owner = "none"

#         # Zakończenie drogi
#         self.intersection = False

#         # Rozdzielność zamków
#         self.separate = False

#         # Właściwości
#         self.width = self.height = 100
#         self.texture = rtc
#         self.red = False
#         self.placed = False
#         self.correct = False

# class right_turn_castle(pieces):
#     def __init__(self, x, y, grid_x, grid_y):
    
#         # Pozycja
#         self.x = x
#         self.y = y

#         self.grid_x = grid_x
#         self.grid_y = grid_y

#         # 1 - castle
#         # 2 - road
#         # 3 - field
#         # 9 - empty grid
        
#         # Krawędzie
#         self.top = 1
#         self.right = 3
#         self.bottom = 2
#         self.left = 2

#         # Kto jest właścicelem
#         self.field_owner = "none"
#         self.road_owner = "none"
#         self.castle_owner = "none"
#         self.monastry_owner = "none"

#         # Zakończenie drogi
#         self.intersection = False

#         # Rozdzielność zamków
#         self.separate = False

#         # Właściwości
#         self.width = self.height = 100
#         self.texture = ltc
#         self.red = False
#         self.placed = False
#         self.correct = False

# class single_castle(pieces):
#     def __init__(self, x, y, grid_x, grid_y):
    
#         # Pozycja
#         self.x = x
#         self.y = y

#         self.grid_x = grid_x
#         self.grid_y = grid_y

#         # 1 - castle
#         # 2 - road
#         # 3 - field
#         # 9 - empty grid
        
#         # Krawędzie
#         self.top = 1
#         self.right = 3
#         self.bottom = 3
#         self.left = 3

#         # Kto jest właścicelem
#         self.field_owner = "none"
#         self.road_owner = "none"
#         self.castle_owner = "none"
#         self.monastry_owner = "none"

#         # Zakończenie drogi
#         self.intersection = False

#         # Rozdzielność zamków
#         self.separate = False

#         # Właściwości
#         self.width = self.height = 100
#         self.texture = sg
#         self.red = False
#         self.placed = False
#         self.correct = False

# class double_castle(pieces):
#     def __init__(self, x, y, grid_x, grid_y):
    
#         # Pozycja
#         self.x = x
#         self.y = y

#         self.grid_x = grid_x
#         self.grid_y = grid_y

#         # 1 - castle
#         # 2 - road
#         # 3 - field
#         # 9 - empty grid
        
#         # Krawędzie
#         self.top = 1
#         self.right = 2
#         self.bottom = 2
#         self.left = 3

#         # Kto jest właścicelem
#         self.field_owner = "none"
#         self.road_owner = "none"
#         self.castle_owner = "none"
#         self.monastry_owner = "none"

#         # Zakończenie drogi
#         self.intersection = False

#         # Rozdzielność zamków
#         self.separate = False

#         # Właściwości
#         self.width = self.height = 100
#         self.texture = rtc
#         self.red = False
#         self.placed = False
#         self.correct = False