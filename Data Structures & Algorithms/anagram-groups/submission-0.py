class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        has=defaultdict(list)
       
        for i in strs:
            d=[0]*26
            for c in i:
                ind=97-ord(c)
                d[ind]+=1
            has[tuple(d)].append(i)
        return list(has.values())
        
        
            
















        
        
        

            