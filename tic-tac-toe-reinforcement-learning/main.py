from env import ttt
from ql import Q
from agent import agent

class game:
  
  def __init__(self, agent):
    self.agent = agent
  def g(self, t):
    state = t.get_state()
    action = self.agent.get_action(state, t.get_valid_actions())
    winner = t.play(action[0], action[1])
    print()
    t.print_board()
    if winner != None: 
      return winner
    print()
    x = int(input("enter x : "))
    y = int(input("enter y : "))
    winner = t.play(x, y)
    print()
    t.print_board()
    if winner != None: 
      return winner
    return None

  def playgame(self):
    while(True):
      t = ttt()
      while(True):
        winner = self.g(t)
        if(winner != None):
          if winner == 0:
            print("draw")
          else:
            print(t.repr[winner] + " win")
          break

a = agent()
a.train()
a.test()
g = game(a)
g.playgame()