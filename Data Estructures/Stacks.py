class Stacks:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():         #sin este nuevo argumento si el stack esta vacio tira error
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():         #sin este nuevo argumento si el stack esta vacio tira error
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)
s = Stacks()
s.push("A")
s.push("B")
s.push("C")
#print(s)
s.peek()
#print(s.peek())
s.pop()
#print(s)