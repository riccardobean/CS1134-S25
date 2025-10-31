from ArrayStack import ArrayStack


class MaxStack:
    def __init__(self):
        self.st = ArrayStack()
        self.highest = None

    def __len__(self):
        return len(self.st)

    def is_empty(self):
        return len(self.st) == 0

    def push(self, el):
        if self.highest is None:
            self.highest = el
        elif el > self.highest:
            self.highest = el
        new = (el, self.highest)
        self.st.push(new)

    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.st.top()[0]

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.st.pop()[0]

    def max(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.st.top()[1]


mx = MaxStack()
mx.push(12)
mx.push(13)
mx.push(8)
mx.pop()
mx.pop()
mx.pop()
print(mx.max())