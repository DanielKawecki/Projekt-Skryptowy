import pygame

def pieceValidation(i, j, grid, new_piece):
    # Pozycja kursora
    mouse = pygame.mouse.get_pos() 

    # Sprawdzanie pozycji nowego elementu
    if grid[i][j].hover(mouse[0], mouse[1]) == True:
        new_piece.grid_x, new_piece.grid_y = grid[i][j].grid_x, grid[i][j].grid_y

    new_piece.x, new_piece.y = mouse[0]-50, mouse[1]-50

    new_piece.checkNeighbors(grid)

# Funkcja rysująca w fazie układania
def redraw(window, grid, grid_width, grid_height, new_piece):
    
    # Tło
    window.fill((200, 200, 200))

    for i in range(grid_width):
        for j in range(grid_height):

            # Rysowanie
            grid[i][j].draw(window)
            
            pieceValidation(i, j, grid, new_piece)
    
    if new_piece:
        new_piece.draw(window)