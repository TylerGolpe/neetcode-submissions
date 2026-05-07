class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #We can access specific positions with board[i][j]
        #This works with board[row][column]
        #We can check the row and column validity easily this way.
        #Let's start by creating default sets for each key we stumble upon
        cols = defaultdict(set)
        rows = defaultdict(set)
        grids = defaultdict(set)

        for row in range(9):
            for col in range(9):
                #Empty spaces are "."
                if board[row][col] == ".":
                    continue
                #We're checking 3 things here.
                #Does the current number already exist in our row set?
                #Does the current number already exist in our column set?
                #Does the current number already exist in our grid set?
                if (board[row][col] in rows[row]
                    or board[row][col] in cols[col]
                    #Here, we're setting our "grids" to be equivalent to each 3x3 matrix by saying
                    #"Hey, make sure there's no decimals here, and create a key based on that"
                    #This means if we have 1/3, it'll be 0 and not 0.333, meaning 2/3 matches to 0 too
                    or board[row][col] in grids[(row // 3, col // 3)]):
                    #If it exists already, immediately return False
                    return False

                #Now that we've checked for that number the first time, let's add it to our sets
                #For that column, let's add the value at each row in that column
                cols[col].add(board[row][col])
                #Let's do the same for the rows
                rows[row].add(board[row][col])
                #And of course, for our grids
                grids[(row // 3, col // 3)].add(board[row][col])
                #Notice that this grid area uses the same "technique" as above.

        return True
