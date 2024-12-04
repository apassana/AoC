import re

class Solution:
    def make_list(self) -> list[str]:
        file = open('input.txt', 'r')
        result = file.readlines()
        file.close()
        return result

    def find_matches(self, s: str) -> list[str]:
        x = re.findall("mul[(]([0-9]{3}|[0-9]{2}|[0-9]),([0-9]{3}|[0-9]{2}|[0-9])[)]", s)
        return x

    def find_matches2(self, s: str) -> list[str]:
        x = re.findall("mul[(]([0-9]{3}|[0-9]{2}|[0-9]),([0-9]{3}|[0-9]{2}|[0-9])[)]|(don't[(][)])|(do[(][)])", s)
        return x

    def solve(self):
        l = self.make_list()
        result1 = 0
        result2 = 0
        a = []
        for line in l:
            a += self.find_matches2(line)
            parsed_line = self.find_matches(line)
            for pair in parsed_line:
                result1 += (int(pair[0]) * int(pair[1]))
        on = True
        for expr in a:
            if expr[2] != '':
                on = False
            elif expr[3] != '':
                on = True
            elif on:
                result2 += (int(expr[0]) * int(expr[1]))
        print("Part one solution: ", result1)
        print("Part two solution: ", result2)
       

def main():
    a = Solution()
    a.solve()

if __name__ == '__main__':
    main()
