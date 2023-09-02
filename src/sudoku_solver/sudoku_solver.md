# Sudoku Solver

Your task is to create a function which takes a string representing a sudoku puzzle and returns a string representing the solved puzzle. The input string will be 81 characters long, representing the 9 rows of the puzzle, each row containing 9 characters. The characters will be either a number between 1 and 9, or a period (.) representing an empty cell. The output string should be the same length, with the empty cells filled in with the correct numbers.

**Note:** Depending on how far you want to go with it you can choose whether or not to only consider determinable puzzles (i.e. those which you do not have to guess and test uncertain values for). The example below is a determinable puzzle. If you want to go further, you can find a list of undeterminable puzzles [here](https://sudoku.com/hard/).

Examples
```python
input = '53..7....6..195...98....6..8...6...4..8.3..7...2...6..6....28...419..5....8..79'
solved = '534678912672195348198342567859761423426853791713924856961537284287419635345286179'
# the first 9 characters represent the first row, the next 9 the second row, etc.

```
