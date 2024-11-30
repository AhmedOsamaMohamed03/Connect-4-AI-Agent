from service.Service import*

class Expectiminimax:
    def _init_(self, turn = '0', chosen_column = 1):
        self.turn = turn
        self.chosen_column = chosen_column

    def maximize(self, state, k):
        if k == 0:
            return (None, eval(state, self.turn))
        
        max_child = None
        max_utility = -float("inf")

        for child, prob in get_children_probability(state, self.turn, self.chosen_column ):
            _, utility = self.minimize(child, k - 2)
            
            if prob * utility > max_utility:
                max_utility = prob * utility
                max_child = child

        return  (max_child, max_utility)

    def minimize(self, state, k):
        if k == 0:
            return (None, eval(state, self.turn))
        
        min_child = None
        min_utility = float("inf")

        for child, prob in get_children(state, self.turn):
            _, utility = self.maximize(child, k - 1)
            
            if utility < min_utility:
                min_utility = utility
                min_child = child
                
        return  (min_child, min_utility)
    
    def decision(self, state, k):
        child, _ = self.maximize(state, k)
        return child