from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        answer = 0
        list_length = len(nums)

        for number_position in range(list_length):
            if nums[number_position] != val:
                nums[answer] = nums[number_position]
                answer += 1
        return answer


solutions_instance = Solution()
nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2

print(solutions_instance.removeElement(nums, val))
