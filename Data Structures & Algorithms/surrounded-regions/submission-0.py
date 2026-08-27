class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        directions = [
            (-1, 0),
            (1, 0),
            (0, 1),
            (0, -1)
        ]

        q = deque()
        visited = set()

        # Add border O's
        for r in range(rows):
            if board[r][0] == 'O':
                q.append((r, 0))
                visited.add((r, 0))

            if board[r][cols - 1] == 'O':
                q.append((r, cols - 1))
                visited.add((r, cols - 1))

        for c in range(cols):
            if board[0][c] == 'O':
                q.append((0, c))
                visited.add((0, c))

            if board[rows - 1][c] == 'O':
                q.append((rows - 1, c))
                visited.add((rows - 1, c))

        # BFS from border O's
        while q:
            x, y = q.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if (
                    0 <= nx < rows and
                    0 <= ny < cols and
                    board[nx][ny] == 'O' and
                    (nx, ny) not in visited
                ):
                    q.append((nx, ny))
                    visited.add((nx, ny))

        # Any O NOT reachable from border gets captured
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r, c) not in visited:
                    board[r][c] = 'X'