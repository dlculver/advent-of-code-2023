# Decided to just go with Python, too busy to learn a new language right now.

# link to problem:  https://adventofcode.com/2023/day/2

hash = {"red": 12, "green": 13, "blue": 14} 

with open("input.txt", "r") as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]

indices_of_possible = []

def is_possible(game: str) -> bool:
    trials = game.split(":")[-1].split(";")

    # each trial is something like "3 red, 5 green, 4 blue"
    # so we need to process these kind of lines

    for trial in trials:
        num_color_pairs = trial.split(",")
        for num_color_pair in num_color_pairs:
            num, color = num_color_pair.strip().split()
            if hash[color] < int(num):
                return False

    return True

if __name__ == "__main__":
    for i, line in enumerate(lines):
        if is_possible(line):
            indices_of_possible.append(i + 1) # since we are 0-indexed but the problem is 1-indexed

    print(f"The sum of the indices of the possible games is {sum(indices_of_possible)}")
