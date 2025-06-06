import random

# Velikost hrací plochy
WIDTH, HEIGHT = 10, 10

# Inicializace prázdné hrací plochy
def create_board():
    return [["." for _ in range(WIDTH)] for _ in range(HEIGHT)]

# Vykreslení hrací plochy
def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

# Pohybová logika
def move(position, direction):
    x, y = position
    if direction == "w" and x > 0:
        x -= 1
    elif direction == "s" and x < HEIGHT - 1:
        x += 1
    elif direction == "a" and y > 0:
        y -= 1
    elif direction == "d" and y < WIDTH - 1:
        y += 1
    return [x, y]

# Nepřítel se pohybuje náhodně mezi možnými směry
def enemy_move(position):
    directions = ["w", "a", "s", "d"]
    random.shuffle(directions)
    for direction in directions:
        new_pos = move(position, direction)
        # Můžeš přidat překážky, aby nepřítel nešel přes ně
        # tady není žádná překážka, tak hned vrací první možný krok
        if new_pos != position:
            return new_pos
    return position  # pokud nemůže jít nikam, zůstane

def main():
    player_pos = [HEIGHT // 2, WIDTH // 2]  # start uprostřed
    enemy_pos = [0, 0]  # start v rohu

    while True:
        board = create_board()
        board[player_pos[0]][player_pos[1]] = "P"
        board[enemy_pos[0]][enemy_pos[1]] = "E"
        print_board(board)

        # Tah hráče
        move_input = input("Move (w/a/s/d), q to quit: ").lower()
        if move_input == 'q':
            print("Game over!")
            break
        if move_input not in ["w", "a", "s", "d"]:
            print("Invalid move. Use w/a/s/d.")
            continue

        player_pos = move(player_pos, move_input)

        # Tah nepřítele
        enemy_pos = enemy_move(enemy_pos)

        # Kontrola setkání
        if player_pos == enemy_pos:
            print("Encounter! Boj začíná!")
            break

if __name__ == "__main__":
    main()
