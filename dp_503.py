class Solution:
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        result = []
        for i in range(len(nums)):
            ### [0~i-1], [i+1~len()-1]
            index = -1
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    index = j
                    break
            if index == -1:
                for j in range(0, i):
                    if nums[j] > nums[i]:
                        index = j
                        break
            result.append(nums[index] if index != -1 else -1)

        return result

    def nextGreaterElements_simple(self, nums):
        result = [-1] * len(nums)
        st = []
        l = len(nums)
        for i in range(l * 2):
            num = nums[i % l]
            while len(st) and nums[st[-1]] < num:
                result[st.pop(-1)] = num
            if i < l:
                st.append(i)
        return result

if __name__ == '__main__':
    solution = Solution()
    print(solution.nextGreaterElements_simple([1, 2, 1]))
