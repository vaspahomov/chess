import pickle


class GameSerializer:
    def __init__(self):
        pass

    def save_game(self, state):
        pickle.dump(state, "game.json")

    def load_game(self):
        return pickle.load("game.json")
