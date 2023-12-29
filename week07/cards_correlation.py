from itertools import product
from random import choice
from scipy.stats import pearsonr


kinds = ["h", "d", "c", "s"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

deck = list(product(kinds, ranks))

reds = kinds[:2]
pictures = ranks[10:]

def play_game(turns=100):
    n_reds, n_pictures = 0, 0
    for i in range(turns):
        card = choice(deck)
        if card[0] in reds:
            n_reds += 1
        if card[1] in pictures:
            n_pictures += 1

    return n_reds, n_pictures


if __name__ == "__main__":
    N = 1000000
    etas, xis = [], []
    for i in range(N):
        eta, xi = play_game(1000)
        etas.append(eta)
        xis.append(xi)

    print(f"Number of games = {N}, corr = {pearsonr(etas, xis)}")
