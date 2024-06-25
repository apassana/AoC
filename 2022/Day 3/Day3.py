class Group:
    def __init__(self, sacks: list[str]):
        assert len(sacks) == 3
        self.sacks = sacks
        self.badge = ''
        self.find_common_element()

    def find_common_element(self):
        result = set(self.sacks[0]) & set(self.sacks[1]) & set(self.sacks[2])
        self.badge = str(result.pop())


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


def grouper(sack_list: list[str]) -> list[Group]:
    result = list()
    sack_group = list()
    for sack in sack_list:
        sack_group.append(sack)
        if len(sack_group) >= 3:
            result.append(Group(sack_group))
            sack_group = list()
    return result


def compartmentalize(sack_list: list[str]) -> list[list[str]]:
    result = list()
    for sack in sack_list:
        half_sack = len(sack) // 2
        sack_compartments = list()
        sack_compartments.append(sack[0:half_sack].strip())
        sack_compartments.append(sack[half_sack:len(sack)].strip())
        result.append(sack_compartments)
    return result


def setalize(c_sack_list: list[list[str]]) -> list[list[set]]:
    result = list()
    for sack in c_sack_list:
        sack_compartments = list()
        sack_compartments.append(set(sack[0]))
        sack_compartments.append(set(sack[1]))
        result.append(sack_compartments)
    return result


def compile_dupes(s_sack_list: list[list[set]]) -> list[str]:
    result = list()
    for sack in s_sack_list:
        result.append((sack[0] & sack[1]).pop())
    return result


def main():
    priority_dict = {}

    # Lowercase letters (a to z)
    for i in range(26):
        char = chr(ord('a') + i)  # get lowercase letter
        priority_dict[char] = i + 1  # priorities 1 through 26

    # Uppercase letters (A to Z)
    for i in range(26):
        char = chr(ord('A') + i)  # get uppercase letter
        priority_dict[char] = i + 27  # priorities 27 through 52

    sack_list = clean_list(make_list())
    groups = grouper(sack_list)
    c_sack_list = compartmentalize(sack_list)
    s_sack_list = setalize(c_sack_list)
    dupes = compile_dupes(s_sack_list)
    result = 0
    for char in dupes:
        result += priority_dict[char]
    print("Solution 1: ", result)
    result = 0
    for group in groups:
        result += priority_dict[group.badge]
    print("Solution 2: ", result)


if __name__ == '__main__':
    main()
