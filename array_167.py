class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l_index = 0
        r_index = len(numbers) - 1
        while l_index < r_index:
            if numbers[l_index] + numbers[r_index] == target:
                return [l_index, r_index]
            elif numbers[l_index] + numbers[r_index] < target:
                l_index += 1
            else:
                r_index -= 1

        return []