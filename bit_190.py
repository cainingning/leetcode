class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        x = str(bin(n))[2:]
        x = x[::-1]
        if len(x) < 32:
            x = x + '0' * (32 - len(x))
        return int(x, 2)

if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseBits(43261596))

