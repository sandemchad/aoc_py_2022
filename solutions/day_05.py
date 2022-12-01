def read_file() -> str:
  data_filename = __file__.replace('solutions', 'data').replace('.py', '.txt')
  with open(data_filename, "r") as file:
    return file.read().strip()

if __name__ == "__main__":
  data = read_file()
  print(f"Part 1: {data}")
  print(f"Part 2: {data}")
