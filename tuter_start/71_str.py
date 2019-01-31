class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        if len(path) == 0:
            return path
        l = path.strip('/').split('/')
        st = []
        for item in l:
            if len(item) == 0:
                continue
            if item not in ['.', '..']:
                st.append(item)
            elif item == '..' and len(st) > 0:
                st.pop(-1)
        res = '/' + '/'.join(st)

        return res

solution = Solution()
print(solution.simplifyPath("/a/../../b/../c//.//"))
