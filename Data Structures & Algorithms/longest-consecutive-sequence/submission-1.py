class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        seen= set()
        maxlen=1
        
        for i in nums:
            seen.add(i)
        for val in seen:
            if val-1 not in seen:
                s=val
                leng=1
                while s+leng in seen:
                    leng+=1
                maxlen=max(maxlen,leng)
        return maxlen