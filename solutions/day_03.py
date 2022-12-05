def read_file() -> str:
  data_filename = __file__.replace('solutions', 'data').replace('.py', '.txt')
  with open(data_filename, "r") as file:
    return file.read().strip()

def convert_to_score(char) -> int:
  parse_ord = 96 if ord(char) >= 97 else (65 - 27)
  return ord(char) - parse_ord

def find_duplicates(line) -> str:
  all_chars = list(line)
  ransack_len = len(all_chars)
  half = ransack_len // 2
  first_sack, second_sack = all_chars[:half],all_chars[half:]
  common_chars = list(set(first_sack).intersection(second_sack))
  return list(map(convert_to_score, common_chars))

def find_badge(elf_group) -> str:
  a, b, c = elf_group
  return list(map(convert_to_score, set(a).intersection(b).intersection(c)))

def flatten(items) -> list:
  return [item for sublist in items for item in sublist]

if __name__ == "__main__":
  data = read_file()
  lines = list(map(find_duplicates, data.split("\n")))

  print(f"Part 1: {sum(flatten(lines))}")

  elf_groups = list(zip(*[iter(data.split("\n"))]*3))
  badges = list(map(find_badge, elf_groups))

  print(f"Part 2: {sum(flatten(badges))}")
