class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dit = {}
        for i in range(len(nums)):
            more = target - nums[i]
            
            if more in dit:
                return [dit[more], i]
            
            dit[nums[i]] = i
        
        return []
        