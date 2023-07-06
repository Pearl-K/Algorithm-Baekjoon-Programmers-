def win(board, x, y):
    LY, RY = (y-1)%3, (y+1)%3
    
    if board[x][y] == board[x][LY] == board[x][RY]:
        return True
    
    UX, DX = (x-1)%3, (x+1)%3
    if board[x][y] == board[UX][y] == board[DX][y]:
        return True
    
    if (board[x][y] == board[UX][LY] == board[DX][RY]) or (board[x][y] == board[UX][RY] == board[DX][LY]):
        return True
    
    return False
    
def solution(board):
    O, X = [], []
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O':
                O.append((i, j))
            elif board[i][j] == 'X':
                X.append((i, j))
                
    if len(O) < len(X) or len(O) - len(X) >= 2:
        return 0
    
    for x, y in O:
        if win(board, x, y) and len(X) != (len(O) -1):
            return 0
        
    for x, y in X:
        if win(board, x, y) and len(X) != len(O):
            return 0
    
    return 1
    