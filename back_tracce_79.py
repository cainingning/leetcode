class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(board) <= 0:
            return False
        if len(board[0]) <= 0:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                """将每个元素都当作所求word的起始位置进行求解"""
                if self.exist_core(board, i, j , word, 0):
                    return True

        return False


    def exist_core(self, board, i, j, word, match_index):
        if match_index == len(word):
            return True
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[match_index]:
            return False
        #将ij位置标记为已经访问。
        """英文字母0-127.所以^128出现的字符就不是字母了，可以作为标记，同时再操作一次容易恢复"""
        board[i][j] = '-' + board[i][j]
        is_exist = self.exist_core(board, i-1, j, word, match_index+1) or self.exist_core(board, i, j-1, word, match_index + 1)  or self.exist_core(board, i+1, j, word, match_index+1) or self.exist_core(board, i, j+1, word, match_index+1)

        board[i][j] = board[i][j][1:]

        return is_exist

if __name__ == '__main__':
    solution = Solution()
    print(solution.exist(board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
], word = "ABCB"))