import functools

def read_file() -> str:
  data_filename = __file__.replace('solutions', 'data').replace('.py', '.txt')
  with open(data_filename, "r") as file:
    return file.read()

def group_by_n_uniq(n):
  def group_by_uniq(result, char) -> list:
    result[-1].append(char)
    if len(result[-1]) >= n and len(set(result[-1][-n:])) == n:
      result.append([])
    return result
  return group_by_uniq

if __name__ == "__main__":
  data = read_file().strip()
  markers = functools.reduce(group_by_n_uniq(4), list(data), [[]])

  print(f"Part 1: {len(markers[0])}")

  messages = functools.reduce(group_by_n_uniq(14), list(data), [[]])
  print(f"Part 2: {len(messages[0])}")
