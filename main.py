import pieces
import draw_piece
from text_and_font import *
import players
import textures

# Inicjalizacja biblioteki
import pygame
pygame.init()

game_phase = "start"

# Utworzenie okana gry
window_width = 1440
window_height = 900

window = pygame.display.set_mode([window_width, window_height])

# Właściwości belki okna
pygame.display.set_caption("Carcassonne")

# Siatka planszy
grid_height = 22
grid_width = 22

# Przesunięcie planszy
offset = [-330, -600]

grid = [[pieces.empty_grid((i*100)-330, (j*100)-600, i, j) for j in range(grid_height-1)] for i in range(grid_width-1)]

grid.append([pieces.edge_grid((i*100), 2100, i, 21)for i in range(grid_width)])

for i in range(22):
    grid[i].append(pieces.edge_grid(2100, (100*i), 21, i))

# Element początkowy
src = pygame.image.load("textures/straight_road_castle.png")
src = pygame.transform.smoothscale(src, [100, 100])
grid[10][10] = pieces.piece_template(1, 2, 3, 2, False, False, src, False, False, (window_width/2)-50, (window_height/2)-50, 2, 2)

# Pierwszy losowy element
current = 0
new_piece = draw_piece.list_of_elements[current]
new_piece.placed = False
current = 1

# Gracze
all_players = []
all_players.append(players.player("Player 1", (255, 0, 0), 10))
all_players.append(players.player("Player 2", (0, 255, 0), 100))

player_board = textures.player_board

current_player = 0

# Pole wyboru
monastery = button("Monastery", 400, 430, 30, (255, 255, 255))
pass_bt = pass_button(600, 430, 30, (255, 255, 255))
cancel = cancel_button(800, 430, 30, (255, 255, 255))

def drawNewPiece():
    global new_piece
    global current
    new_piece = draw_piece.list_of_elements[current]
    current += 1
    global game_phase 
    game_phase = "own"

def place():
    new_piece.placed = True
    new_piece.red = False
    new_piece.x = new_piece.grid_x*100 + offset[0]
    new_piece.y = new_piece.grid_y*100 + offset[1]

    # Umieszczenie elementu na planszy
    grid[new_piece.grid_x][new_piece.grid_y] = new_piece

def ownElement():
    mouse = pygame.mouse.get_pos() 

    global new_piece
    global all_players

    if monastery.click(mouse) and all_players[current_player].warriors > 0:
        new_piece.own(current_player, all_players[current_player].color)
        all_players[current_player].warriors -= 1
        return True
    
    elif pass_bt.click(mouse):
        return True
    
    elif cancel.click(mouse):
        global game_phase
        game_phase = "draw"
        return False
    
    else:
        return False

def scan_for_points():
    global grid
    global all_players
    for i in range(grid_width):
        for j in range(grid_height):
            if grid[i][j].actual_piece == True and grid[i][j].monastery == True and grid[i][j].monastery_owner != 9:
                counter = 0
                neighbours = [grid[i-1][j-1], grid[i][j-1], grid[i+1][j-1], grid[i-1][j], grid[i+1][j], grid[i-1][j+1], grid[i][j+1], grid[i+1][j+1]]
                for element in neighbours:
                    if isinstance(element, pieces.piece_template):
                        counter += 1
                if counter == 8:
                    all_players[grid[i][j].monastery_owner].warriors += 1
                    all_players[grid[i][j].monastery_owner].points += 9
                    grid[i][j].monastery_owner = 9
    
def pieceValidation(i, j):
    # Pozycja kursora
    mouse = pygame.mouse.get_pos() 

    # Sprawdzanie pozycji nowego elementu
    if grid[i][j].hover(mouse[0], mouse[1]) == True:
        new_piece.grid_x, new_piece.grid_y = grid[i][j].grid_x, grid[i][j].grid_y

    new_piece.x, new_piece.y = mouse[0]-50, mouse[1]-50

    new_piece.checkNeighbors(grid)

# Funkcja rysująca graczy
def draw_players():
    for i in range(len(all_players)):
        all_players[i].draw(window)

# Funkcja rysująca w fazie układania
def redraw():
    
    # Tło
    window.fill((200, 200, 200))

    for i in range(grid_width):
        for j in range(grid_height):

            # Rysowanie
            grid[i][j].draw(window)
            
            pieceValidation(i, j)

    # pygame.draw.rect(window, (76, 227, 253), (0, 0, 150, 200))
    pygame.draw.rect(window, (0, 0, 0), (0, 0, 155, 205))
    pygame.draw.rect(window, (200, 255, 255), (0, 0, 150, 200))
    draw_players()

    # text(str(current_player), 800, 800).draw(window)
    
    if new_piece:
        new_piece.draw(window)

    # Zmiana klatek
    pygame.display.flip()

# Funkcja rysowania w fazie decydowania o rycerzu
def basicRedraw():
    # Tło
    window.fill((200, 200, 200))

    for i in range(grid_width):
        for j in range(grid_height):

            # Rysowanie
            grid[i][j].draw(window)

    pygame.draw.rect(window, (0, 0, 0), (0, 0, 155, 205))
    pygame.draw.rect(window, (200, 255, 255), (0, 0, 150, 200))
    draw_players()

    if new_piece.monastery == True:
        monastery.draw(window)

    pass_bt.draw(window)
    cancel.draw(window)
        
    # Zmiana klatek
    pygame.display.flip()

# Pętla gry
running = True
while running:

    #Obsługa zamknięcia okna
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        # Obracanie elementów
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                new_piece.rotate("left")

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                new_piece.rotate("right")

        # Przesuwanie planszy
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                for i in range(grid_height):
                    for j in range(grid_width):
                        grid[i][j].y += 100
                offset[1] += 100

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                for i in range(grid_height):
                    for j in range(grid_width):
                        grid[i][j].y -= 100
                offset[1] -= 100

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                for i in range(grid_height):
                    for j in range(grid_width):
                        grid[i][j].x += 100
                offset[0] += 100
                    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                for i in range(grid_height):
                    for j in range(grid_width):
                        grid[i][j].x -= 100
                offset[0] -= 100

        # Lewy przycisk myszy
        if event.type == pygame.MOUSEBUTTONUP and game_phase in ("start", "draw"):
            if event.button == pygame.BUTTON_LEFT and new_piece.correct == True:
                game_phase = "own"
                # ownElement()
        elif event.type == pygame.MOUSEBUTTONUP and game_phase == "own":
            if ownElement():
                place()
                drawNewPiece()
                if current_player+1 > len(all_players)-1:
                    current_player = 0
                else:
                    current_player += 1
                game_phase = "draw"
                scan_for_points()

    if game_phase == "draw":
        redraw()
        
    elif game_phase == "own":
        basicRedraw()

    else:
        redraw()

# Koniec programu
pygame.quit()
