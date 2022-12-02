def read_file() -> str:
  data_filename = __file__.replace('solutions', 'data').replace('.py', '.txt')
  with open(data_filename, "r") as file:
    return file.read().strip()

if __name__ == "__main__":
  data = read_file()
  pairs = data.split("\n")

  possible_scores = {
    # wins
    "C X": 6 + 1,
    "A Y": 6 + 2,
    "B Z": 6 + 3,
    # ties
    "A X": 3 + 1,
    "B Y": 3 + 2,
    "C Z": 3 + 3,
    # losses
    "B X": 0 + 1,
    "C Y": 0 + 2,
    "A Z": 0 + 3,
  }

  scores = list(map(possible_scores.get, pairs))

  print(f"Part 1: {sum(scores)}")

  possible_scores = {
    # losses
    "A X": 0 + 3,
    "B X": 0 + 1,
    "C X": 0 + 2,
    # ties
    "A Y": 3 + 1,
    "B Y": 3 + 2,
    "C Y": 3 + 3,
    # win
    "A Z": 6 + 2,
    "B Z": 6 + 3,
    "C Z": 6 + 1,
  }

  print(f"Part 2: {sum(list(map(possible_scores.get, pairs)))}")
