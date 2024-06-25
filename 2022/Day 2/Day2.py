def make_list() -> list[str]:
    file = open('input.txt', 'r')
    result = file.readlines()
    file.close()
    return result


def tabulate_matches(input_list: list[str]) -> list[list[str]]:
    result = list()
    for line in input_list:
        result_line = [line[0], line[2]]
        result.append(result_line)
    return result


def score_match(match: list[str]) -> int:
    result = 0
    point_converter = {'X': 1, 'Y': 2, 'Z': 3}
    win_converter = {'A': 'Y', 'B': 'Z', 'C': 'X'}
    draw_converter = {'A': 'X', 'B': 'Y', 'C': 'Z'}
    result += point_converter[match[1]]
    if match[1] == win_converter[match[0]]:
        result += 6
    elif match[1] == draw_converter[match[0]]:
        result += 3
    return result


def convert_match(match: list[str]) -> list[str]:
    result = [match[0], 'J']
    converter_converter = {'X': {'A': 'Z', 'B': 'X', 'C': 'Y'},
                           'Y': {'A': 'X', 'B': 'Y', 'C': 'Z'},
                           'Z': {'A': 'Y', 'B': 'Z', 'C': 'X'}}
    result[1] = converter_converter[match[1]][match[0]]
    return result




def main():
    input_list = make_list()
    match_list = tabulate_matches(input_list)
    match_point_list = list()
    fixed_match_point_list = list()
    for match in match_list:
        match_point_list.append(score_match(match))
        fixed_match_point_list.append(score_match(convert_match(match)))
    print("Solution 1: ", sum(match_point_list))
    print("Solution 2: ", sum(fixed_match_point_list))


if __name__ == '__main__':
    main()
