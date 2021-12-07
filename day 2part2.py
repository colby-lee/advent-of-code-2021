with open('input.txt', 'r') as f:
  lines = [line.split(' ') for line in f.read().splitlines()] 


def get_position(lines:list) -> int:
  depth = 0
  h_pos = 0
  aim = 0

  for line in lines:
    if line[0] == 'forward':
      h_pos += int(line[1])
      depth += (int(line[1]) * aim)
    elif line[0] == 'down':
      aim += int(line[1])
    elif line[0] == 'up':
      aim -= int(line[1])

  return depth * h_pos



print(get_position(lines))
