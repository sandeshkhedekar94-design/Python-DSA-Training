class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_map = {}

        for i in range(len(nums)):
            current_num = nums[i]
            complement = target - current_num
            
            if complement in hash_map:
                return [hash_map[complement], i]
                
            hash_map[current_num] = i