class Solution:
    def make_list(self) -> list[str]:
        file = open('input.txt', 'r')
        result = file.readlines()
        file.close()
        return result

    def listify(self, l: list[str]) -> list[list[int]]:
        result = []
        for i in l:
            result.append(list(map(int, i.split())))
        return result

    def test_line(self, l: list[int]):
        r = range(l[0] + 1, l[0] + 4)
        for i in range(1, len(l)):
            if i not in r:
                return False
            r.start = i + 1
            r.stop = i + 4
        self.num += 1

    def solve(self):
        self.num = 0
        l = self.make_list()
        ll = self.listify(l)
        map(self.test_line, ll)
        print(self.num)


def main():
    a = Solution()
    a.solve()

if __name__ == '__main__':
    main()