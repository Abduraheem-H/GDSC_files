class Solution:
    def maxDepth(self,s: str) -> int:
        count=0
        max_length=0
        for i in range(len(s)):
            if s[i]=="(":
                count+=1
                max_length=max(max_length,count)
            elif s[i]==")":
                count-=1
        return max_length
#print(Solution.maxDepth("()(())(((()()())))"))
