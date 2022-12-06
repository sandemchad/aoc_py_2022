import re

def read_file() -> str:
  data_filename = __file__.replace('solutions', 'data').replace('.py', '.txt')
  with open(data_filename, "r") as file:
    return file.read()

def parse_initial_state(line) -> list:
  keys = list(map(lambda x:f"'{x}'", list(line[slice(1, len(line), 4)])))
  return eval("[" + (",".join(keys).replace("' '", "None")) + "]")

def parse_board(initial_state_lines) -> list:
  board = []
  for i in range(0, 9):
    board.append(list(filter(None, list(map(lambda x:x[i] if i < len(x) else None, initial_state_lines))[::-1])))
  return board

if __name__ == "__main__":
  data = read_file()
  lines = data.split("\n")
  stack_count = 8
  initial_state_lines = list(map(parse_initial_state, lines[:8]))

  board = parse_board(initial_state_lines)

  moves = list(map(lambda x:list(map(int, re.findall("\d+", x))), lines[8 + 2:-1]))

  for count, from_index, to_index in moves:
    moved_subset = board[from_index -1][-count:]
    board[from_index - 1] = board[from_index -1][:-count]
    board[to_index - 1].extend(moved_subset[::-1])

  part_1_answer = "".join(list(map(lambda x:x.pop(), board)))
  print(f"Part 1: {part_1_answer}")

  board = parse_board(initial_state_lines)

  for count, from_index, to_index in moves:
    moved_subset = board[from_index -1][-count:]
    board[from_index - 1] = board[from_index -1][:-count]
    board[to_index - 1].extend(moved_subset)
  part_2_answer = "".join(list(map(lambda x:x.pop(), board)))
  print(f"Part 2: {part_2_answer}")
