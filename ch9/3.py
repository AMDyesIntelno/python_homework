class stack:
    def __init__(self, stack_max_length):
        self.stack_max_length = stack_max_length
        self.stack_list = []

    def push(self, element):
        if self.full():
            print("ERROR:Stack is full")
        else:
            self.stack_list.append(element)

    def pop(self):
        if self.empty():
            print("ERROR:Stack is empty")
        else:
            tmp = self.stack_list[len(self.stack_list) - 1]
            del self.stack_list[len(self.stack_list) - 1]
            return tmp

    def empty(self):
        if len(self.stack_list) == 0:
            return True
        else:
            return False

    def full(self):
        if len(self.stack_list) >= self.stack_max_length:
            return True
        else:
            return False

    def find(self, element):
        try:
            posi = self.stack_list.index(element)
        except ValueError:
            return "ERROR: " + str(element) + " is not in stack"
        else:
            return posi

    def peek(self):
        return self.stack_list[len(self.stack_list) - 1]


s = stack(10)
s.pop()
for i in range(11):
    s.push(i)
print(s.peek())
print(s.pop())
print(s.find(9))
print(s.find(8))