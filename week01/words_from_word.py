# This program solve the following problem:
# Given the word X, that is the probability that the word Y can be written if we take N letters

import argparse
from itertools import combinations
from collections import Counter


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="WordsFromWord")
    parser.add_argument("base_word")
    parser.add_argument("Nletters", type=int)
    parser.add_argument("construct")

    args = parser.parse_args()
    construct_counts = Counter(args.construct)

    N_total = 0
    N_favorable = 0
    for characters in combinations(args.base_word, args.Nletters):
        chars_counter = Counter(characters)
        N_total += 1
        if construct_counts <= chars_counter:
            N_favorable += 1

    print(f"Ntotal = {N_total}")
    print(f"Nfav = {N_favorable}")
    print(f"p = {N_favorable / N_total}")
