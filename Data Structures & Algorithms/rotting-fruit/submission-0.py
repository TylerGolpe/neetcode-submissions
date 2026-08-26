from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        fresh = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1

        minutes = 0
        directions = [(-1, 0), (1,0), (0,1), (0,-1)]

        while queue and fresh > 0:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                
                for dirRow, dirCol in directions:
                    neighborRow = row + dirRow
                    neighborCol = col + dirCol
                
                    if 0 <= neighborRow < rows and 0 <= neighborCol < cols:
                        if grid[neighborRow][neighborCol] == 1:
                            grid[neighborRow][neighborCol] = 2
                            fresh -= 1
                            queue.append((neighborRow, neighborCol))
            minutes += 1
       
        if fresh == 0:
            return minutes

        return -1