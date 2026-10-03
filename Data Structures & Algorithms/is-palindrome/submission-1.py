class Solution:
    def isPalindrome(self, s: str) -> bool:
        concat=s.lower()
        i=0
        j=len(concat)-1
        while i<j:
            if not concat[i].isalnum():
                i+=1
            elif not concat[j].isalnum():
                j-=1
            elif concat[i]==concat[j]:
                i+=1
                j-=1    
            else:
                return False
        return True