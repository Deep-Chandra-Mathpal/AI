class ttt:

  def __init__(self):
    self.rc = 3
    self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    self.player = 1
    self.repr = {0: "-", 1: "x", -1: "o"}
  
  def print_board(self):
    for i in range(0, self.rc):
      for j in range(0, self.rc):
        if self.board[i][j] == 0:
          print(self.repr[0], end = "  ")
        elif self.board[i][j] == 1:
          print(self.repr[1], end = "  ")
        else:
          print(self.repr[-1], end = "  ")
      print()
  
  def get_winner(self):
    for i in range(0,self.rc):
      if sum(self.board[i][j] for j in range(0, self.rc)) == 3:
        return 1
      elif sum(self.board[i][j] for j in range(0, self.rc)) == -3:
        return -1
      elif sum(self.board[j][i] for j in range(0, self.rc)) == -3:
        return -1
      elif sum(self.board[j][i] for j in range(0, self.rc)) == 3:
        return 1
    
    if sum(self.board[i][i] for i in range(0, self.rc)) == 3:
      return 1
    if sum(self.board[i][self.rc-1-i] for i in range(0, self.rc)) == 3:
      return 1
    if sum(self.board[i][i] for i in range(0, self.rc)) == -3:
      return -1
    if sum(self.board[i][self.rc-1-i] for i in range(0, self.rc)) == -3:
      return -1
    
    return None
  
  def isended(self):
    for i in range(0, self.rc):
      for j in range(0, self.rc):
        if(self.board[i][j] == 0):
          return False
    return True
    
  def get_state(self):
    return str(self.board)
  
  def get_valid_actions(self):
    actions = []
    for i in range(0, self.rc):
      for j in range(0, self.rc):
        if self.board[i][j] == 0:
          actions.append((i,j))
    return actions
  
  def play(self, x, y):
    if self.board[x][y] != 0:
      return None
    self.board[x][y] = self.player
    winner = self.get_winner()
    if winner:
      return winner
    if(self.isended()):
      return 0
    self.player *= -1
    return None
