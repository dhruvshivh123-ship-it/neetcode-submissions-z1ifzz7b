class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dicte = {}
        for i in range(len(nums)):
            dicte[nums[i]]=dicte.get(nums[i],0)+1
        for val in dicte:
            if dicte[val] >1:
                return True
            
        return False
        

        