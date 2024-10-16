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


def create_range(l: str) -> list[list[int]]:
    n = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
    result = []
    r = []
    a = ''
    for i in l:
        if i in n:
            a += i
        if i == '-':
            if a != '':
                r.append(int(a))
            a = ''
        if i == ',':
            if a != '':
                r.append(int(a))
                result.append(r)
            r = []
            a = ''
    r.append(int(a))
    result.append(r)
    return result


def encompassed(l: list[list[int]]) -> bool:
    a = l[0][0]
    b = l[0][1]
    c = l[1][0]
    d = l[1][1]
    if a <= c:
        if d <= b:
            return True
    if c <= a:
        if b <= d:
            return True
    return False


def touching(l: list[list[int]]) -> bool:
    a = l[0][0]
    b = l[0][1]
    c = l[1][0]
    d = l[1][1]
    if b < c:
        return False
    if d < a:
        return False
    return True


def main():
    rans = get_list()
    a = []
    b = 0
    c = 0
    for i in rans:
        a.append(create_range(i))
    for i in a:
        if encompassed(i):
            b += 1
        if touching(i):
            c += 1
    print("Part 1: ", b)
    print("Part 2: ", c)


if __name__ == '__main__':
    main()
