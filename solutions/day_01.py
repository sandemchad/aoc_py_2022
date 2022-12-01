def total_calories(entry) -> int:
  return sum(list(map(int, entry.split("\n"))))

def read_file() -> str:
  data_filename = __file__.replace('solutions', 'data').replace('.py', '.txt')
  with open(data_filename, "r") as file:
    return file.read().strip()

if __name__ == "__main__":
  data = read_file()
  elf_calorie_counts = data.split("\n\n")
  calorie_totals = list(map(total_calories, elf_calorie_counts))
  print(f"Part 1: {max(calorie_totals)}")
  print(f"Part 2: {sum(sorted(calorie_totals, reverse=True)[:3])}")
