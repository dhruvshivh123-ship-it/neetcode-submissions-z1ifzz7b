class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dit={}
        cnt=0
        l=[]
        bucket=[[] for _ in range(len(nums)+1)]
    
        for i in range(len(nums)):
            dit[nums[i]]=dit.get(nums[i],0)+1
        for n ,freq in dit.items():
            bucket[freq].append(n)
        
        for i in range(len(bucket)-1,0,-1):
            for j in bucket[i]:
                l.append(j)
            if len(l)==k:
                return l


        
