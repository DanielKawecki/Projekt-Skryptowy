import pieces
import draw_piece
import text_and_font
import players

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
grid_height = 21
grid_width = 21

# Przesunięcie planszy
offset = [0, 0]




player1 = players.player('Daniel', 'red', 20)
player2 = players.player('Agata', 'red', 80)




grid = [[pieces.empty_grid((i*100), (j*100), i, j) for j in range(grid_height)] for i in range(grid_width)]

# Element początkowy
src = pygame.image.load("textures/straight_road_castle.png")
src = pygame.transform.smoothscale(src, [100, 100])
grid[2][2] = pieces.piece_template(1, 2, 3, 2, False, False, src, False, False, 200, 200, 2, 2)

# Pierwszy losowy element
current = 0
new_piece = draw_piece.list_of_elements[current]
new_piece.placed = False
current = 1

# sum_of_elements = len(draw_piece.list_of_elements)-current

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

    player1.draw(window)
    player2.draw(window)
    
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

        # Przesuwanie planszy
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                for i in range(20):
                    for j in range(20):
                        grid[i][j].y -= 100
                offset[1] -= 100

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                for i in range(20):
                    for j in range(20):
                        grid[i][j].y += 100
                offset[1] += 100

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                for i in range(20):
                    for j in range(20):
                        grid[i][j].x -= 100
                offset[0] -= 100
                    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                for i in range(20):
                    for j in range(20):
                        grid[i][j].x += 100
                offset[0] += 100

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
