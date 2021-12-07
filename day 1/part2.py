with open('input.txt', 'r') as f:
    lines = [int(i) for i in f.readlines()]


# lines = [199,
#          200,
#          208,
#          210,
#          200,
#          207,
#          240,
#          269,
#          260,
#          263]


def get_depth_increase(lines, window):
    increase = 0
    prev = 0

    for i in range(len(lines)):
        t_lst = sum(lines[i: i + window])
        if t_lst > prev:
            increase += 1
        prev = t_lst
    return increase - 1


print(get_depth_increase(lines, 3))
