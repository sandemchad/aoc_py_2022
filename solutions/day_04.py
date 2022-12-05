def read_file() -> str:
  data_filename = __file__.replace('solutions', 'data').replace('.py', '.txt')
  with open(data_filename, "r") as file:
    return file.read().strip()

def parse_ranges(range_str) -> list:
  start, finish = map(int, range_str.split('-'))
  return set(range(start, finish + 1))

def find_subsets(pair) -> bool:
  range_a, range_b = map(parse_ranges, pair.split(","))
  return range_a.issubset(range_b) or range_b.issubset(range_a)

def find_overlaps(pair) -> bool:
  range_a, range_b = map(parse_ranges, pair.split(","))
  return not(range_a.isdisjoint(range_b))

if __name__ == "__main__":
  data = read_file()
  pairs = data.split("\n")

  print(f"Part 1: {len(list(filter(find_subsets, pairs)))}")
  print(f"Part 2: {len(list(filter(find_overlaps, pairs)))}")
