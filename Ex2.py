def _count_neighbors(grid, r, c):
    rows, cols = len(grid), len(grid[0])
    cnt = 0
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue
            rr, cc = r + dr, c + dc
            if 0 <= rr < rows and 0 <= cc < cols:
                cnt += grid[rr][cc]
    return cnt


def _step(grid):
    rows, cols = len(grid), len(grid[0])
    next_grid = [[0] * cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            n = _count_neighbors(grid, r, c)
            if grid[r][c] == 1:
                # Survie si 2 ou 3 voisins ( selon ma compréhension des règles..)
                next_grid[r][c] = 1 if n in (2, 3) else 0
            else:
                # Naissance si exactement 3 voisins ( également..)
                next_grid[r][c] = 1 if n == 3 else 0
    return next_grid


def _to_html(grid):
    rows_html = []
    for row in grid:
        tds = ''.join(f"<td>{'■' if cell else '·'}</td>" for cell in row)
        rows_html.append(f"<tr>{tds}</tr>")
    table = "<table border='1' cellspacing='0' cellpadding='4'>\n" + "\n".join(rows_html) + "\n</table>"
    return "<!doctype html><html><body>\n" + table + "\n</body></html>"


def game_of_life(board, iterations=5, html_file="game_of_life_result.html"):
    """
    board: (0=mort, 1=vivant)
    iterations: nombre d'itérations
    """
    if not board or not board[0]:
        return board

    grid = [row[:] for row in board]

    for _ in range(iterations):
        grid = _step(grid)

    #save dans un fichier html
    html_code = _to_html(grid)
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html_code)
    print(f"Résultat HTML sauvegardé dans {html_file}")

    return grid

#exemple
if __name__ == "__main__":
    start = [
        [0,0,0,0,0],
        [0,0,1,0,0],
        [0,0,0,1,0],
        [0,1,1,1,0],
        [0,0,0,0,0],
    ]

    final_board = game_of_life(start, iterations=5)
    print("Matrice finale :", final_board)
