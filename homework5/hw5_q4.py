from ArrayStack import ArrayStack


class Queue:
    def __init__(self):
        self.psh_opt = ArrayStack()
        self.pop_opt = ArrayStack()
        self.n = 0

    def __len__(self):
        return self.n

    def is_empty(self):
        return self.n == 0

    def enqueue(self, el):
        if self.n == 0:
            self.psh_opt.push(el)
        elif self.psh_opt.is_empty():
            while not self.pop_opt.is_empty():
                temp = self.pop_opt.pop()
                self.psh_opt.push(temp)
            self.psh_opt.push(el)
        else:
            self.psh_opt.push(el)
        self.n += 1

    def dequeue(self):
        if self.n == 0:
            raise Exception("Queue is empty")
        if self.pop_opt.is_empty():
            while not self.psh_opt.is_empty():
                temp = self.psh_opt.pop()
                self.pop_opt.push(temp)
        self.n -= 1
        return self.pop_opt.pop()

    def first(self):
        if self.n == 0:
            raise Exception("Queue is empty")
        if self.pop_opt.is_empty():
            while not self.psh_opt.is_empty():
                temp = self.psh_opt.pop()
                self.pop_opt.push(temp)
        return self.pop_opt.top()
