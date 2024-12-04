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

    def test_line(self, l: list[int]) -> bool:
        if l[0] < l[1]:
            low = l[0] + 1
            high = l[0] + 3
            for i in range(1, len(l)):
                if l[i] >= low and l[i] <= high:
                    low = l[i] + 1
                    high = l[i] + 3
                else:
                    return False
        else:
            low = l[0] - 3
            high = l[0] - 1
            for i in range(1, len(l)):
                if l[i] >= low and l[i] <= high:
                    low = l[i] - 3
                    high = l[i] - 1
                else:
                    return False
        return True

    def test_line2(self, l: list[int]) -> bool:
        tolerance = True
        l_len = len(l)
        for i in range(l_len):
            if self.test_line(l[0:i] + l[(i + 1):l_len]):
                return True
        return False

    def test_lines(self, f, l: list[list[int]]) -> int:
        result = 0
        for i in l:
            if f(i):
                result += 1
        return result

    def solve(self):
        l = self.make_list()
        ll = self.listify(l)
        num1 = self.test_lines(self.test_line, ll)
        num2 = self.test_lines(self.test_line2, ll)
        print("First solution: ", num1)
        print("Second solution: ", num2)


def main():
    a = Solution()
    a.solve()

if __name__ == '__main__':
    main()
