import random
from env import ttt
from ql import Q

class agent:
  def __init__(self):
    self.eps = 1.0
    self.qlearner = Q()
  
  def get_action(self, state, valid_actions):
    if random.random() < self.eps:
      return random.choice(valid_actions)
    best_action = self.qlearner.get_best_action(state)
    if best_action is None:
      return random.choice(valid_actions)
    return best_action
  
  def trainAgent(self, t):
    state = t.get_state()
    action = self.get_action(state, t.get_valid_actions())
    winner = t.play(action[0], action[1])
    if winner != None: 
      self.qlearner.updateqtable(state, action, t.get_state(), 100)
      return winner
    winner = t.play(*random.choice(t.get_valid_actions()))
    if winner != None: 
      self.qlearner.updateqtable(state, action, t.get_state(), -100)
      return winner
    self.qlearner.updateqtable(state, action, t.get_state(), 0)
    return None
  
  def train(self):
    n = 1
    tn = 50000
    print("\non progress ...")
    while(n<tn):
      t = ttt()
      while(True):
        winner = self.trainAgent(t)
        if(winner != None):
          break
      self.eps -= 0.0001
      n += 1
    print(f"{tn} iteration completed")
  
  # for testing purpose only

  def testgame(self, t):
    state = t.get_state()
    action = self.get_action(state, t.get_valid_actions())
    winner = t.play(action[0], action[1])
    if winner != None: 
      return winner
    winner = t.play(*random.choice(t.get_valid_actions()))
    if winner != None: 
      return winner
    return None
  
  def test(self):
    n = 1
    total_game = 20000
    win = 0
    lose = 0
    draw = 0
    while(n<=total_game):
      t = ttt()
      while(True):
        winner = self.testgame(t)
        if(winner != None):
          if winner == 0:
            draw += 1
          else:
            if winner == 1:
              win += 1
            else:
              lose += 1
          break
      n += 1
    print(f"\ntotal game played- {total_game}\ngame win - {win}\ngame lose - {lose}\ngame draw - {draw}\n")
