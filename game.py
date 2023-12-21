import util
import connect3  

class Player:
    def __init__(self, playerCharacter):
        self.character = playerCharacter
    
    def choose_action(self, state):
        pass
class Game:
    def __init__(self, player1, player2):
        self.state = connect3.State()
        self.player1 = player1
        self.player2 = player2
        self.state_sequence = []
    def play(self):
        current_player = self.player1
        while not self.state.game_over():
            self.state_sequence.append(self.state.clone())
            newState = current_player.choose_action(self.state)
            util.pprint(newState)
            self.state = newState
            if (current_player == self.player1):
                current_player = self.player2
            else:
                current_player = self.player1
        self.state_sequence.append(self.state.clone())
        winner = self.state.winner()
        if winner:
            print(f"{winner} wins")
        else:
            print("Draw")
        return (winner, self.state_sequence)
        



