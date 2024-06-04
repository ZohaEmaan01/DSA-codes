class Stack:
    def __init__(self,size):
        self.size = size
        self.arr = [None] * size
        self.top = -1

    def push(self,val):
        if self.top == self.size - 1:
            raise Exception('stack overflow')
        self.top += 1
        self.arr[self.top] = val

    def pop(self):
        if self.top == -1:
            raise Exception('stack is empty')
        temp = self.arr[self.top]
        self.top -= 1
        return temp

    def peek(self):
        if self.top == -1:
            raise Exception('stack is empty')
        return self.arr[self.top]

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.size - 1

    def __str__(self):
        return str(self.arr[:self.top+1])
