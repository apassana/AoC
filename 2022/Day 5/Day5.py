class Solution:
    def make_list(self) -> list[str]:
        file = open('input.txt', 'r')
        result = file.readlines()
        file.close()
        return result

    def make_stacks(self, l: list[str]) -> list[list[str]]:
        b = []
        for i in range(9):
            b.append([])
        for i in range(8):
            k = 1
            for j in range(9):
                q = l[i][k + (4*j)]
                if q != ' ':
                    b[j].append(q)
        return b


    def process_instruction(self, s: str) -> list[int]:
        numbers = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
        result = list()
        result.append(int(s[5:7]))
        for i in s[10:]:
            if i in numbers:
                result.append(int(i))
        return result


    def run_instruction(self, i: list[int]) -> bool:
        from_index = i[1] - 1
        to_index = i[2] - 1
        amount = i[0]
        for j in range(amount):
            if len(self.c[from_index]) > 0:
                a = self.c[from_index].pop(0)
                self.c[to_index].insert(0, a)
                return True
            else:
                print("trouble running instruction ", i)
                return False


    def print_stacks(self):
        for i in self.c:
            print(i)

    def solve(self):
        a = self.make_list()
        self.c = self.make_stacks(a)
        instructions = []
        self.print_stacks()
        for i in a[10:]:
            instructions.append(self.process_instruction(i))
        for i in range(72):
            if not self.run_instruction(instructions[i]):
                print("trouble running instruction #", i)
                # break
        print('')
        self.print_stacks()


def main():
    a = Solution()
    a.solve()


if __name__ == '__main__':
    main()