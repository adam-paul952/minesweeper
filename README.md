# Minesweeper

A simple minesweeper terminal game written in Python.

Game modes include:

- Beginner: 9x9 board with 10 mines
- Intermediate: 16x16 board with 40 mines
- Expert: 16x30 board with 99 mines

## Getting started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone this repository:
   ```
   git clone https://github.com/adam-paul952/minesweeper
   ```
2. Navigate to the project directory:
   ```
   cd repository
   ```
3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Playing the game

1. Run the game: `python main.py`

2. You will be greeted with a welcome message and a list of game modes. Choose your preferred game mode by typing 'B', 'I', or 'E' and press Enter.

3. The game board will be displayed. Each cell is represented by a square bracket `[]`. Mines are hidden randomly on the board.

4. To reveal a cell, type the row and column numbers separated by a space, then press Enter. For example, to reveal the cell at row 1 and column 1, type `1 1`.

5. If the revealed cell is a mine, the game is over. If not, the number of mines in the adjacent cells will be displayed in the revealed cell.

6. To flag a cell as a mine, type the row and column numbers followed by 'f', then press Enter. For example, to flag the cell at row 1 and column 1, type `1 1 f`.

7. The goal of the game is to reveal all cells that do not contain a mine. If you manage to do this without revealing a mine, you win the game!

8. After the game is over, you will be asked if you want to play again. Type 'yes' to start a new game, or 'no' to quit.
