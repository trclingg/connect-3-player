import random
import game
import math

class RandomPlayer(game.Player):
    def __init__(self, playerCharacter):
        super().__init__(playerCharacter)
        
    def choose_action(self, state):
        actions = state.actions(self.character)
        if actions:
            action = random.choice(actions)
            newState = state.clone().execute(action)
            return newState

class MinimaxPlayer(game.Player):
    def __init__(self, character):
        super().__init__(character)
        self.depth = 2
        self.recursive_calls = 0
        if self.character == "X":
            self.opponentCharacter = "O"
        else: 
            self.opponentCharacter = "X"
        
    
    def evaluate(self, state):
        winner = state.winner()
        if winner == self.character:
            return 1
        elif winner == self.opponentCharacter:
            return -1
        else:
            return 0
    
    def choose_action(self, state):
        action = self.minimax_decision(state)
        newState = state.clone().execute(action)
        return newState

   
    def minimax_decision(self, state):
        actions = state.actions(self.character)
        max_value = float('-inf')
        decision = actions[0]
        for action in actions:
            new_state = state.clone().execute(action)
            value = self.min_value(new_state)
            if value > max_value:
                max_value = value
                decision = action
        return decision
    
    def min_value(self, state):
        if state.game_over():
            return self.evaluate(state)
        else:
            actions = state.actions(self.opponentCharacter)
            min_value = math.inf
            for action in actions:
                new_state = state.clone().execute(action)
                value = self.max_value(new_state)
                if value < min_value:
                    min_value = value
            return min_value*0.9


    def max_value(self, state):
        if state.game_over():
            return self.evaluate(state)
        else:
            actions = state.actions(self.character)
            max_value = -math.inf
            for action in actions:
                new_state = state.clone().execute(action)
                value = self.min_value(new_state)
                if value > max_value:
                    max_value = value
            return max_value*0.9
        

    