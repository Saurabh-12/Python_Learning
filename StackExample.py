class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)


    def pop(self):
        return self.items.pop()


    def size(self):
        return len(self.items)


stacks = Stack()
stacks.push("April")
stacks.push("May")
stacks.push("June")

print(stacks.items)
print(stacks.pop())
