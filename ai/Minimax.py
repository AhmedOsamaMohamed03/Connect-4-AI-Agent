from service.Service import *

class Minimax:
  def __init__(self, turn = '1'):
    self.turn = turn
    self.minimax_tree = dict()
  
  def maximize(self, state, K):
    # terminal state
    if K == 0:
      return (None, eval(state, self.turn))
    
    max_child = None
    max_utility = -float('inf')

    for child in get_children(state, self.turn):
      _, utility = self.minimize(child, K - 1)
      if utility > max_utility:
        max_utility = utility
        max_child = child
    
    return (max_child, max_utility)
  
  def minimize(self, state, K):
    # terminal state
    if K == 0:
      return (None, eval(state, self.turn))
    
    min_child = None
    min_utility = float('inf')

    for child in get_children(state, '2' if self.turn == '1' else '1'):
      _, utility = self.maximize(child, K - 1)
      if utility < min_utility:
        min_utility = utility
        min_child = child
    
    return (min_child, min_utility)