class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        k=10
        s1=set()
        ans=[]
        for i in range(len(s)-9):
            if s[i:i+10] in s1:
                ans.append(s[i:i+10])
            else:
                s1.add(s[i:i+10])
        return set(ans)
