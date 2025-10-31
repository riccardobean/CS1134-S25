from ArrayDeque import ArrayDeque
from ArrayStack import ArrayStack


class MidStack:
    def __init__(self):
        self.stack = ArrayStack()
        self.deque = ArrayDeque()

    def __len__(self):
        return len(self.stack) + len(self.deque)

    def is_empty(self):
        return len(self) == 0

    def push(self, el):
        if self.stack.is_empty():
            self.stack.push(el)
        else:
            if len(self.deque) == len(self.stack):
                temp = self.deque.dequeue_first()
                self.stack.push(temp)
            self.deque.enqueue_last(el)

    def pop(self):
        if self.is_empty():
            raise Exception("MidStack is empty")
        if not self.deque.is_empty():
            pop_val = self.deque.dequeue_last()
        else:
            pop_val = self.stack.pop()
        if len(self.deque) != len(self.stack):
            temp = self.stack.pop()
            self.deque.enqueue_first(temp)
        return pop_val

    def top(self):
        if self.is_empty():
            raise Exception("MidStack is empty")
        return self.deque.last()

    def mid_push(self, el):
        if self.stack.is_empty():
            self.stack.push(el)
        else:
            self.deque.enqueue_first(el)
