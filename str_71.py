class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        if len(path) <= 0:
            return path
        save_record = []
        path_list = path.strip().split('/')
        for p in path_list:
            if p =='' or p =='.':
                continue
            elif p =='..':
                if len(save_record) > 0:
                    save_record = save_record[:-2]
            else:
                save_record.append('/')
                save_record.append(p)


        result = "".join(save_record)

        return result if len(result) > 0 else '/'



if __name__ == '__main__':
    solution = Solution()
    print(solution.simplifyPath("///"))