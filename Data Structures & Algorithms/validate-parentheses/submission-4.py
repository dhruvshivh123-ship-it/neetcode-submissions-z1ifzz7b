class Solution:
    def isValid(self, s: str) -> bool:
        res=[]
        close= { ")" : "(", "]" : "[", "}" : "{" }
        for i in s:
            if i in close:
                if res and res[-1]==close[i]:
                    res.pop()
                else:
                    return False
            else:
                res.append(i)
        return True if not res else False