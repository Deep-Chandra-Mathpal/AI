from collections import defaultdict

class Q:
  def __init__(self, alpha = 0.5, discount = 0.5):
    self.alpha = alpha
    self.discount = discount
    self.values = defaultdict(lambda: defaultdict(lambda: 0.0))

  def updateqtable(self, state, action, nextstate, reward):
    value = self.values[state][action]
    v = list(self.values[nextstate].values())
    q_next = max(v) if v else 0
    value = value + self.alpha * (reward + self.discount * q_next - value)
    self.values[state][action] = value
  
  def get_best_action(self, state):
    keys = list(self.values[state].keys())
    if not keys: return None
    return max(keys, key=lambda x: self.values[state][x])
