class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)-1
        sume=0
        while i<j:
            sume = numbers[i]+numbers[j]
            if sume==target:
                return[i+1,j+1]
            elif sume> target:
                j-=1
            else:
                i+=1
        return []
            