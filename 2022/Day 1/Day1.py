def make_list() -> list[str]:
    file = open('input.txt', 'r')
    result = file.readlines()
    file.close()
    return result


def become_numeric(cal_list: list[str]) -> list[list[int]]:
    result = list()
    accumulator = list()
    for line in cal_list:
        if line == '\n':
            result.append(accumulator)
            accumulator = list()
        else:
            accumulator.append(int(line))
    return result


def total_cal_list(cal_list: list[list[int]]) -> list[int]:
    result = list()
    for line in cal_list:
        result.append(sum(line))
    return result


def main():
    cal_list = make_list()
    cal_list = become_numeric(cal_list)
    summed_cal_list = total_cal_list(cal_list)
    summed_cal_list = sorted(summed_cal_list)
    print("Solution 1: ", summed_cal_list[-1])
    print("Solution 2: ", sum([summed_cal_list[-1], summed_cal_list[-2], summed_cal_list[-3]]))


if __name__ == '__main__':
    main()
