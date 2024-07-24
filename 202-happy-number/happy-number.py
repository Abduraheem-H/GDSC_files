class Solution:
    def isHappy(self, n: int) -> bool:
        num = str(n)
        left = 0
        right = len(num) - 1

        seen = set()  

        while left <= right:
            total = 0
            for i in range(len(num)):
                if left == right:
                    total += int(num[left]) ** 2
                else:
                    total += int(num[left]) ** 2 + int(num[right]) ** 2
                left += 1
                right -= 1
                if left>right: break
                print (total)

            num = str(total)

            if num == "1":
                return True
            elif num in seen:
                return False  
            else:
                seen.add(num)  
                left = 0
                right = len(num) - 1

        return False  


sol = Solution().isHappy(1221)
print(sol)
