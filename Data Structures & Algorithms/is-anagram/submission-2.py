class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dr={}
        re={}
        for i in s:
            dr[i]=dr.get(i,0)+1
        for j in t:
            re[j]=re.get(j,0)+1
        if dr==re:
            return True
        return False        
        
            
        