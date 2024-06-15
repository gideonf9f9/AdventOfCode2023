from library.constants import PATH
import re

input_file = PATH+'day_2//input.txt'
with open(input_file, 'r') as f:
    inp = f.readlines()

COLORS = ['red', 'green', 'blue']

def split_game(game: str):
    combs = re.split(';|:', game)

    id_ = int(combs[0][5:])
    out = []
    for show in combs[1:]:
        stones = show.split(',')
        res = {}
        for stone in stones:
            split_stone = stone.split(' ')
            stone_nr = split_stone[1]
            stone_col = split_stone[2]
            if stone_col[-1] == '\n':
                stone_col = stone_col[:-1]
            res[stone_col] = int(stone_nr)

        for color in COLORS:
            if color not in res:
                res[color] = 0

        out.append(res)

    return id_, out


if __name__ == '__main__':
    out = 0
    for line in inp:
        _, res = split_game(line)
        min_blue = 0
        min_red = 0
        min_green = 0

        for show in res:
            min_red = max(min_red, show['red'])
            min_blue = max(min_blue, show['blue'])
            min_green = max(min_green, show['green'])

        out += min_red * min_blue * min_green
    print(out)
