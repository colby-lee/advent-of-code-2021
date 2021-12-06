with open('input.txt', 'r') as f:
    lines = f.read().splitlines()


def find_depth_increase(lines):
    increase = 1
    for i in range(0, len(lines) - 1):
        if lines[i + 1] > lines[i]:
            increase += 1
    return increase


find_depth_increase(lines)

