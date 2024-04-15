from random import sample


class Board:
    def __init__(self, width, height, mines):
        self.width = width
        self.height = height
        self.mines = mines
        self.player_board = self.initialize_player_board()
        self.default_board = self.initialize_default_board()

    def initialize_player_board(self):
        return [["*" for _ in range(self.width)] for _ in range(self.height)]

    def initialize_default_board(self):
        default_board = [[" " for _ in range(self.width)] for _ in range(self.height)]
        all_cells = [
            (i, j) for i in range(1, self.height) for j in range(1, self.width)
        ]
        mine_cells = sample(all_cells, self.mines)

        for i, j in mine_cells:
            default_board[i][j] = "M"
            for x in range(max(0, i - 1), min(i + 2, self.height)):
                for y in range(max(0, j - 1), min(j + 2, self.width)):
                    if default_board[x][y] != "M":
                        if default_board[x][y] == " ":
                            default_board[x][y] = "1"
                        else:
                            default_board[x][y] = str(int(default_board[x][y]) + 1)
        return default_board

    def draw_game_board(self, reveal=False):
        """
        Prints the current state of the game board.

        Args:
        reveal (bool, optional): If True, the function prints the default game board (revealing all cells). If False, the function prints the player's game board (with unrevealed cells). Defaults to False.

        The function first prints a row of column numbers. Then, for each row in the game board, it prints the row number, followed by the cell values in that row.

        Each cell value is printed inside a box, and there's a line of dashes under each row to separate it from the next row.

        Example:
        If the player's game board is [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']], and the default game board is [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']], the function will print:

        | 1 | 2 | 3 |
        -----------------
        1 | * | * | * |
        -----------------
        2 | * | * | * |
        -----------------
        3 | * | * | * |
        -----------------

        If reveal is True, the function will print:

        | 1 | 2 | 3 |
        -----------------
        1 | 1 | 2 | 3 |
        -----------------
        2 | 4 | 5 | 6 |
        -----------------
        3 | 7 | 8 | 9 |
        -----------------
        """
        # Choose the board to draw
        board_to_draw = self.default_board if reveal else self.player_board

        separator = " | "
        row_template = separator.join(
            ["{} " if i >= 9 else "{}" for i in range(self.width)]
        )
        row_length = len(row_template) - 2 - max(0, self.width - 9)

        # Print the top row of numbers
        print(
            f"  {separator.rstrip()}",
            separator.join(str(i) for i in range(1, self.width + 1)),
            separator.strip(),
        )

        # Print the line under the top row of numbers
        print("-" * row_length)

        # Print the rows with numbers on the left side and the actual values from the default game board inside
        for i in range(self.height):
            row = board_to_draw[i]
            formatted_row = row_template.format(*row)
            print(f"{ i + 1 : 2} {separator.strip()}", formatted_row, separator.strip())
            print("-" * row_length)

    def is_mine(self, row: int, col: int) -> bool:
        """
        Checks if the cell at the given row and column contains a mine.

        Args:
        row (int): The row of the cell to check.
        col (int): The column of the cell to check.

        Returns:
        bool: True if the cell contains a mine, False otherwise.
        """
        return self.default_board[row][col] == "M"

    def dfs(self, row, col):
        """
        Performs a Depth-First Search (DFS) on the game board starting from a given cell.

        Args:
        row (int): The row number of the cell where the DFS should start.
        col (int): The column number of the cell where the DFS should start.

        The function explores the game board by moving from the starting cell to its unexplored neighbors. If a cell is empty, all its neighbors are added to the stack to be explored. The function continues until all reachable cells have been explored.

        The player's view of the game board is updated as cells are explored: each unexplored cell ("*") is replaced with its corresponding value from the actual game board.

        Note: This function modifies the player_board in-place.
        """
        # List of all 8 possible directions
        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1),
        ]

        # Stack for DFS
        stack = [(row, col)]

        while stack:
            r, c = stack.pop()
            if self.player_board[r][c] == "*":
                self.player_board[r][c] = self.default_board[r][c]
                if self.default_board[r][c] == " ":
                    # If the cell is empty, add all its neighbors to the stack
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if (
                            0 <= nr < self.height
                            and 0 <= nc < self.width
                            and self.player_board[nr][nc] == "*"
                        ):
                            stack.append((nr, nc))
