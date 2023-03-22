import pieces

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
grid_height = 9
grid_width = 13

grid = [[pieces.empty_grid(i*100+70, j*100, i, j) for j in range(grid_height)] for i in range(grid_width)]

# Element początkowy
grid[6][4] = pieces.straight_road_castle(670, 400, 6, 4)
grid[5][3] = pieces.road_turn(570, 300, 5, 3)

# Pierwszy losowy element
new_piece = pieces.road_turn(0, 0, 0, 0)
new_piece.placed = False

def drawNewPiece():
    global new_piece
    new_piece = pieces.straight_road(0, 0, 0, 0)
    global game_phase 
    game_phase = "own"

def place():
    new_piece.placed = True
    new_piece.red = False
    new_piece.x = new_piece.grid_x*100+70
    new_piece.y = new_piece.grid_y*100

    # Umieszczenie elementu na planszy
    grid[new_piece.grid_x][new_piece.grid_y] = new_piece

    # Zmiana fazy gry
    global game_phase 
    game_phase = "draw"

def ownElement():
    pass

def pieceValidation(i, j):
    # Pozycja kursora
    mouse = pygame.mouse.get_pos() 

    # Sprawdzanie pozycji nowego elementu
    if grid[i][j].hover(mouse[0], mouse[1]) == True:
        new_piece.grid_x, new_piece.grid_y = grid[i][j].grid_x, grid[i][j].grid_y

    new_piece.x, new_piece.y = mouse[0]-50, mouse[1]-50

    new_piece.checkNeighbors(grid)
    
# Funkcja rysująca w fazie układania
def redraw():
    
    # Tło
    window.fill((170, 170, 170))

    for i in range(grid_width):
        for j in range(grid_height):

            # Rysowanie
            grid[i][j].draw(window)
            
            pieceValidation(i, j)

    if new_piece:
        new_piece.draw(window)

    # Zmiana klatek
    pygame.display.flip()

# Funkcja rysowania w fazie decydowania o rycerzu
def basicRedraw():
    # Tło
    window.fill((170, 170, 170))

    for i in range(grid_width):
        for j in range(grid_height):

            # Rysowanie
            grid[i][j].draw(window)
        
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

        # Lewy przycisk myszy
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == pygame.BUTTON_LEFT and new_piece.correct == True:
                place()

    if game_phase == "draw":
        basicRedraw()
        drawNewPiece()
    else:
        redraw()

# Koniec programu
pygame.quit()
