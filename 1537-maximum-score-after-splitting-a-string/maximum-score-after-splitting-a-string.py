class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        numZeroes = 0
        rightValue = s.count("1")
        for i in range(len(s)-1):
            if s[i] == "0":
                numZeroes += 1
            
            elif s[i]=="1":
                rightValue -= 1
            max_score = max(max_score, numZeroes + rightValue)
        return max_score
#print(Solution.maxScore("11"))
