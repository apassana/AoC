class Solution:
    def make_list(self) -> list[str]:
        file = open('input.txt', 'r')
        result = file.readlines()
        file.close()
        return result

    def solve(self):

def main():
    a = Solution()
    a.solve()

if __name__ == '__main__':
    main()