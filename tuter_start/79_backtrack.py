class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        """如果标记一个位置已经被使用"""
        if len(board) == 0 or word is None:
            return False
        word_l = list(word)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.is_exist(board, i, j, word_l, 0):
                    return True

        return False

    def is_exist(self, board, x, y, word_l, index):
        if index == len(word_l):
            return True
        if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
            return False
        if board[x][y] != word_l[index]:
            return False
        board[x][y] += '-'
        exist = self.is_exist(board, x - 1, y, word_l, index + 1) | \
                self.is_exist(board, x, y - 1, word_l, index + 1) | \
                self.is_exist(board, x + 1, y, word_l, index + 1) | \
                self.is_exist(board, x, y + 1, word_l, index + 1)
        board[x][y] = board[x][y][:1]

        return exist

solution = Solution()
print(solution.exist(board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
], word = "ABCCED"))


