class MyQueue:

    def __init__(self):
        self.queue=[]
        self.queue_new=[]
        

    def push(self, x: int) -> None:
        
        self.queue.append(x)
        

    def pop(self) -> int:
        if not self.queue_new:
            while self.queue:
                self.queue_new.append(self.queue.pop())
        
        return self.queue_new.pop()

        

    def peek(self) -> int:
        if not self.queue_new:
            while self.queue:
                self.queue_new.append(self.queue.pop())
        return self.queue_new[-1]
        

    def empty(self) -> bool:
        if not (self.queue_new or self.queue):
            return True
        
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()