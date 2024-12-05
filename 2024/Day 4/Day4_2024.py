import time

class Solution:
    def __init__(self):
        self.matrix = self.make_list()
        self.dirs = []
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if not(i == 0 and j == 0):
                    self.dirs.append((i, j))
        self.word = "XMAS"

    def in_limits(self, coord) -> bool:
        return ((coord[0] >= 0 and coord[0] < len(self.matrix)) and 
                (coord[1] >= 0 and coord[1] < len(self.matrix[0])))

    def in_limits2(self, coord) -> bool:
        return ((coord[0] > 0 and coord[0] < len(self.matrix) - 1) and 
                (coord[1] > 0 and coord[1] < len(self.matrix[0]) - 1))

    def clean_list(self, l: list[str]) -> list[str]:
        result = list()
        for line in l:
            result.append(line.rstrip(" \n"))
        return result

    def make_list(self) -> list[str]:
        file = open('input.txt', 'r')
        result = file.readlines()
        file.close()
        return self.clean_list(result)

    def search(self, coord: list[int]) -> int:
        result = 0
        for d in self.dirs:
            result += self.search_ray([(coord[0] + d[0]), (coord[1] + d[1])], d, 1)
        return result
    
    def search_ray(self, coord: list[int], ray: tuple[int], i: int) -> int:
        if i == 4:
            return 1
        if not self.in_limits(coord):
            return 0
        if self.matrix[coord[0]][coord[1]] == self.word[i]:
            return self.search_ray([(coord[0] + ray[0]), (coord[1] + ray[1])], ray, i + 1)
        return 0

    def mas_check(self, coord: list[int]) -> int:
        if not self.in_limits2(coord):
            return 0
        ul = self.matrix[coord[0] - 1][coord[1] - 1]
        ur = self.matrix[coord[0] + 1][coord[1] - 1]
        dl = self.matrix[coord[0] - 1][coord[1] + 1]
        dr = self.matrix[coord[0] + 1][coord[1] + 1]
        a = ul + dr
        b = ur + dl
        if a == "MS" or a == "SM":
            if b == "MS" or b == "SM":
                return 1
        return 0

    def solve(self):
        result = 0
        result2 = 0
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j] == 'A':
                    b = self.mas_check([i, j])
                    result2 += b
                if self.matrix[i][j] == 'X':
                    a = self.search([i, j])
                    result += a
        print("Part one solution: ", result)
        print("Part two solution: ", result2)
       

def main():
    start = time.time()
    a = Solution()
    a.solve()
    end = time.time()
    print("Took ", (end - start) * 1000, " milliseconds")

if __name__ == '__main__':
    main()
