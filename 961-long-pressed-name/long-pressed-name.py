class Solution:
    def isLongPressedName(self,name: str, typed: str) -> bool:
        left = 0
        right = 0

        while left < len(name) and right < len(typed):
            if name[left] == typed[right]:
                left += 1
            elif right > 0 and typed[right] == typed[right - 1]:
                
                pass
            else:
                return False
            right += 1

        
        if left < len(name):
            return False

        
        while right < len(typed):
            if typed[right] != typed[right - 1]:
                return False
            right += 1

        return True



#print(Solution.isLongPressedName("save", "sssave"))  