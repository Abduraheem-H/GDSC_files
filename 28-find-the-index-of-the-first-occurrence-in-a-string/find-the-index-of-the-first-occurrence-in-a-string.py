class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # haystack = "sadbutsad", needle = "sad"
        n=len(needle)
        for i in range(len(haystack)):
            if haystack[i:n]==needle:
                return i
            n+=1
        return -1

       
         
            