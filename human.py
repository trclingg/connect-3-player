import game

class HumanPlayer(game.Player):
    def __init__(self, playerCharacter):
        super().__init__(playerCharacter)
        

    def choose_action(self, state):
        actions = state.actions(self.character)
        for ind, action in enumerate(actions):
            print(f"{ind}: {str(action)}")
        while True:
            try:
                chooseIndex = int(input("Please choose an action: "))
                if 0 <= chooseIndex < len(actions):
                    action = actions[chooseIndex]
                    newState = state.clone().execute(action)
                    return newState
                else:
                    print("Invalid input")
            except:
                break
        
