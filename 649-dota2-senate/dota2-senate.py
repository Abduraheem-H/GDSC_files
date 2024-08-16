from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        dire=deque()
        radiant=deque()
        lastIndex=len(senate)
        for i in range(len(senate)):
            if senate[i]=="R":
                radiant.append(i)
            else:
                dire.append(i)
        while dire and radiant:
            r=radiant.popleft()
            d=dire.popleft()
            if r<d:
                radiant.append(lastIndex)
            else:
                dire.append(lastIndex)
            

                
            
                
                
            lastIndex+=1
        if radiant:
            return "Radiant"
        else:
            return "Dire"
        