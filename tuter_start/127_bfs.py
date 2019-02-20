class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        """无向图广度优先遍历。通常办法是建立邻接表，然后访问。
        在这里先对wordlist进行预处理，目的相当于建立邻接表。然后使用queue进行遍历，直到到达终止节点"""
        if beginWord == endWord or len(wordList) == 0:
            return 0
        common_dic = {}
        for item in wordList:
            for i in range(len(item)):
                k = item[:i] + "*" + item[i+1:]
                if common_dic.get(k):
                    common_dic[k].append(item)
                else:
                    common_dic[k] = [item]
        # print(common_dic)
        queue = [(beginWord, 1)] # 1代表处理变换的第几步
        visited = {beginWord: True}
        while queue:
            node, step = queue.pop(0)
            for i in range(len(node)):
                k = node[:i] + "*" + node[i+1:]
                if not common_dic.get(k):
                    continue
                for v in common_dic[k]:
                    if v == endWord:
                        return step + 1
                    if v not in visited.keys():
                        visited[v] = True
                        queue.append((v, step + 1))
                common_dic[k] = []
        return 0

    def __init__(self):
        self.length = 0
        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        from collections import defaultdict
        self.all_combo_dict = defaultdict(list)

    def visitWordNode(self, queue, visited, others_visited):
        current_word, level = queue.pop(0)
        for i in range(self.length):
            # Intermediate words for current word
            intermediate_word = current_word[:i] + "*" + current_word[i + 1:]

            # Next states are all the words which share the same intermediate state.
            for word in self.all_combo_dict[intermediate_word]:
                # If the intermediate state/word has already been visited from the
                # other parallel traversal this means we have found the answer.
                if word in others_visited:
                    return level + others_visited[word]
                if word not in visited:
                    # Save the level as the value of the dictionary, to save number of hops.
                    visited[word] = level + 1
                    queue.append((word, level + 1))
        return None

    def ladderLength_bi(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        # Since all words are of same length.
        self.length = len(beginWord)

        for word in wordList:
            for i in range(self.length):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                self.all_combo_dict[word[:i] + "*" + word[i + 1:]].append(word)

        # Queues for birdirectional BFS
        queue_begin = [(beginWord, 1)]  # BFS starting from beginWord
        queue_end = [(endWord, 1)]  # BFS starting from endWord

        # Visited to make sure we don't repeat processing same word
        visited_begin = {beginWord: 1}
        visited_end = {endWord: 1}
        ans = None

        # We do a birdirectional search starting one pointer from begin
        # word and one pointer from end word. Hopping one by one.
        while queue_begin and queue_end:

            # One hop from begin word
            ans = self.visitWordNode(queue_begin, visited_begin, visited_end)
            if ans:
                return ans
            # One hop from end word
            ans = self.visitWordNode(queue_end, visited_end, visited_begin)
            if ans:
                return ans

        return 0


solution = Solution()
print(solution.ladderLength_bi("hit", "cog", ["hot","dot","dog","lot","log"]))
print(solution.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]))