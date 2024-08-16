class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_map={}
        
        for i in range(len(s)):
            if s[i] in hash_map:
                hash_map[s[i]]+=1
            else:
                hash_map[s[i]]=1
        for key in hash_map.keys():
            if hash_map[key]==1:
                return s.index(key)
        return -1

        