def solve_n_queens_backtracking(n):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or \
               abs(board[i] - col) == abs(i - row):
                return False
        return True
    
    def backtrack(row):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row+1)
                board[row] = -1
    
    solutions = []
    board = [-1] * n
    backtrack(0)
    return solutions

def solve_n_queens_branch_bound(n):
    def backtrack(row):
        nonlocal solutions
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if not cols[col] and not diag1[row+col] and not diag2[row-col]:
                board[row] = col
                cols[col] = diag1[row+col] = diag2[row-col] = True
                backtrack(row+1)
                cols[col] = diag1[row+col] = diag2[row-col] = False
    
    solutions = []
    board = [-1] * n
    cols = [False] * n
    diag1 = [False] * (2*n-1)
    diag2 = [False] * (2*n-1)
    backtrack(0)
    return solutions

# Example usage
n = 4
print("Backtracking solutions:", solve_n_queens_backtracking(n))
print("Branch & Bound solutions:", solve_n_queens_branch_bound(n))