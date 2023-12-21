import human
import agent 
import game
import util

if __name__ == "__main__":
    P1 = util.get_arg(1)
    P2 = util.get_arg(2)
    if P1 == "human":
        player1 = human.HumanPlayer("X")
    elif P1 == "random":
        player1 = agent.RandomPlayer("X")
    elif P1 == "minimax":
        player1 = agent.MinimaxPlayer("X")
    if P2 == "human":
        player2 = human.HumanPlayer("O")
    elif P2 == "random":
        player2 = agent.RandomPlayer("O")
    elif P2 == "minimax":
        player2 = agent.MinimaxPlayer("O")
    connect3_game = game.Game(player1, player2)
    returnTuple = connect3_game.play()
    util.pprint(returnTuple[1])