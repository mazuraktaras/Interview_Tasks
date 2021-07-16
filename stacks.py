class Stack:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if len(self.data) == 0:
            print('Stack is empty')
            return
        return self.data.pop(-1)

    @property
    def peek(self):
        if len(self.data) == 0:
            print('Stack is empty')
            return
        return self.data[-1]

    @property
    def stack(self):
        if len(self.data) == 0:
            print('Stack is empty')
            return
        return self.data


stack = Stack()
other_stack = Stack()

stack.push(7)
stack.push('new item')
other_stack.push(True)
other_stack.push(727)
print(stack.pop())

print(stack.peek)
print(other_stack.peek)
print(other_stack.stack)