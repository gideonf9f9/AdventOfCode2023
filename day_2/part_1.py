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
        add = True
        id_, res = split_game(line)
        for show in res:
            if show['red'] > 12 or show['green'] > 13 or show['blue'] > 14:
                add = False
                continue
        if add:
            out += id_

    print(out)




