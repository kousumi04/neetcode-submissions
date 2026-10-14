
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2=len(s1), len(s2)
        if n1>n2:
            return False
        a=[0]*26
        b=[0]*26
        for i in range(n1):
            a[ord(s1[i])-ord('a')]+=1
            b[ord(s2[i])-ord('a')]+=1
        if a==b:
            return True

        for i in range(n1, n2):
            b[ord(s2[i])-ord('a')]+=1
            b[ord(s2[i-n1])-ord('a')]-=1
            if a==b:
                return True
        return False    
