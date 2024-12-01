class Solution:
    def make_list(self) -> list[str]:
        file = open('input.txt', 'r')
        result = file.readlines()
        file.close()
        return result

    def listify(self, l: list[str]) -> list[list[int]]:
        a = []
        b = []
        for i in l:
            c = i.split()
            a.append(int(c[0]))
            b.append(int(c[1]))
        return [a, b]

    def get_distance(self, a: int, b: int) -> int:
        return abs(a - b)

    def get_distances(self, l: list[list[int]]) -> int:
        result = 0
        for i in range(len(l[0])):
            result += self.get_distance(l[0][i], l[1][i])
        return result

    def create_freq_dict(self, l: list[int]) -> dict:
        result = dict()
        for i in l:
            if i in result:
                result[i] += 1
            else:
                result[i] = 1
        return result

    def make_score_list(self, l: list[int], fd: dict) -> list[int]:
        result = []
        for i in l:
            if i in fd:
                result.append(i * fd[i])
            else:
                result.append(0)
        return result

    def solve(self):
        raw_list = self.make_list()
        data = self.listify(raw_list)
        sorted_data = list()
        sorted_data.append(sorted(data[0]))
        sorted_data.append(sorted(data[1]))
        result1 = self.get_distances(sorted_data)
        freq_dict = self.create_freq_dict(data[1])
        result2 = sum(self.make_score_list(data[0], freq_dict))
        print("part one result: ", result1)
        print("part two result: ", result2)


def main():
    a = Solution()
    a.solve()


if __name__ == '__main__':
    main()
