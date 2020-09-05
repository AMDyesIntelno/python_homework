class Stack:
    def __init__(self,size=10):
        self.__size=size
        self.stack=[]
    def push(self,item):
        if len(self.stack)>=self.__size:
            print("Stack is full")
            return
        self.stack.append(item)
    def pop(self):
        try:
            return self.stack.pop()
        except IndexError:
            print("Stack is empty")
    def __str__(self):
        return str(self.stack)
s=Stack()
for i in range(1,12):
    s.push(i)
print(s)
for i in range(1,12):
    s.pop()
print(s)