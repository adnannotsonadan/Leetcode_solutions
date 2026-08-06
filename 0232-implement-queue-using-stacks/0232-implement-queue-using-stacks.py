class MyQueue:

    def __init__(self):
        self.st1=[]
        self.st2=[]

    def push(self, x: int) -> None:
        
        while self.st1:
            y=self.st1.pop()
            self.st2.append(y)
        self.st1.append(x)

        while self.st2:
            y=self.st2.pop()
            self.st1.append(y)

    def pop(self) -> int:
        if not self.st1:
            print("Empty")
            return -1
        if self.st1:
            return self.st1.pop()

    def peek(self) -> int:
        if self.st1:
            return self.st1[-1]

    def empty(self) -> bool:
        if not self.st1:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()