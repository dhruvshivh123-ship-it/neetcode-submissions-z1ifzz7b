class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        for i in range(len(nums)):
            if nums[i]==nums[i-1] and i!=0:
                continue
            j=i+1
            k=len(nums)-1
            sume=0
            while j<k:
                sume=nums[i]+nums[j]+nums[k]
                if sume== 0:
                    ans.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
                elif sume>0:
                    k-=1
                else:
                    j+=1
        return ans