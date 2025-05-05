import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
SIZE = 300
LINE_WIDTH = 15
BOARD_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
XO_COLOR = (0, 0, 0)
BACKGROUND_COLOR = (255, 255, 255)
XO_FONT = pygame.font.Font(None, 74)
GRID_COLOR = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((SIZE, SIZE))
pygame.display.set_caption('Tic-Tac-Toe')

# Draw the board lines
def draw_lines():
    screen.fill(BOARD_COLOR)
    pygame.draw.line(screen, GRID_COLOR, (0, SIZE // 3), (SIZE, SIZE // 3), LINE_WIDTH)
    pygame.draw.line(screen, GRID_COLOR, (0, 2 * SIZE // 3), (SIZE, 2 * SIZE // 3), LINE_WIDTH)
    pygame.draw.line(screen, GRID_COLOR, (SIZE // 3, 0), (SIZE // 3, SIZE), LINE_WIDTH)
    pygame.draw.line(screen, GRID_COLOR, (2 * SIZE // 3, 0), (2 * SIZE // 3, SIZE), LINE_WIDTH)

# Draw X or O
def draw_xo(row, col, player):
    x_pos = col * SIZE // 3 + SIZE // 6
    y_pos = row * SIZE // 3 + SIZE // 6
    if player == 'X':
        pygame.draw.line(screen, XO_COLOR, (x_pos - 50, y_pos - 50), (x_pos + 50, y_pos + 50), LINE_WIDTH)
        pygame.draw.line(screen, XO_COLOR, (x_pos + 50, y_pos - 50), (x_pos - 50, y_pos + 50), LINE_WIDTH)
    else:
        pygame.draw.circle(screen, XO_COLOR, (x_pos, y_pos), 50, LINE_WIDTH)

# Check if the board is full
def is_board_full(board):
    for row in board:
        if '' in row:
            return False
    return True

# Check for a win
def check_win(board, player):
    for row in range(3):
        if all([cell == player for cell in board[row]]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]):
        return True
    if all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

# Main function
def main():
    board = [['' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    game_over = False

    draw_lines()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                x, y = event.pos
                row, col = y // (SIZE // 3), x // (SIZE // 3)

                if board[row][col] == '':
                    board[row][col] = current_player
                    draw_xo(row, col, current_player)

                    if check_win(board, current_player):
                        print(f"Player {current_player} wins!")
                        game_over = True
                    elif is_board_full(board):
                        print("It's a tie!")
                        game_over = True
                    else:
                        current_player = 'O' if current_player == 'X' else 'X'
        
        pygame.display.update()

if __name__ == "__main__":
    main()