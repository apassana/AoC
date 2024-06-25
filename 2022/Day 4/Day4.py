def make_list() -> list[str]:
    file = open('input.txt', 'r')
    result = file.readlines()
    file.close()
    return result


def clean_list(l: list[str]) -> list[str]:
    result = list()
    for line in l:
        result.append(line.rstrip(" \n"))
    return result


def get_list() -> list[str]:
    a = make_list()
    return clean_list(a)


def create_ranges(l: list[str]) -> list[list[int]]:
    result = list()
    for item in l:



def main():
    rans = get_list()
    print(rans[0])



if __name__ == '__main__':
    main()
