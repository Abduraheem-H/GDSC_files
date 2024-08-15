class RecentCounter:

    def __init__(self):
        self.inputs=[]
        

    def ping(self, t: int) -> int:
        range = t-3000

        self.inputs.append(t)
        while self.inputs and self.inputs[0]< range:
            self.inputs.pop(0)
        return len(self.inputs)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)