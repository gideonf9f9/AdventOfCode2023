from library.constants import PATH

input_file = PATH + 'day_1//input.txt'

num_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'zero': 0}


def extract_numbers(string: str) -> [int]:
    res = []
    for char in string:
        if 48 <= ord(char) <= 57:
            res.append(char)

    return res


def extrac_numbers_2(string: str) -> [int]:
    res = []
    new_string = string + 'qq'
    for i, char in enumerate(string):
        if 48 <= ord(char) <= 57:
            res.append(char)
        else:
            for key in num_dict:
                if key in string[i: i+5]:
                    res.append(num_dict[key])
    return res


def get_cal_val(string: str) -> int:
    nums = extract_numbers(string)
    return int(nums[0]+nums[-1])


if __name__ == '__main__':
    with open(input_file, 'r') as f:
        res = 0
        for line in f.readlines():
            res += get_cal_val(line)

        print(res)

