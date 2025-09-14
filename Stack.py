class Stack:
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Empty Stack"
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return "Empty stack"
    def is_empty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
    def print_stack(self):
        print(self.items)
if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.print_stack()
    s.pop()
    s.print_stack()
    element = s.peek()
    print(element)
    
    my_size = s.size()
    print(my_size)
            
            
