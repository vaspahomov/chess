import pickle


class GameSerializer:
    def __init__(self):
        pass

    def save_game(self, figures):
        with open("figures.json") as figures_file:
            pickle.dump(figures, figures_file)

    def load_game(self):
        figures =  pickle.load("game.json")

        return figures
