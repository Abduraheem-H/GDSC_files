class Solution:
    def isPalindrome(self, x: int) -> bool:
        strX=str(x)
        leftptr=0
        rightptr=len(strX)-1
        while(leftptr<rightptr):
            if strX[leftptr]!=strX[rightptr]:
                return False 
            else:
                leftptr+=1
                rightptr-=1
        return True


        