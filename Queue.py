class Queue:
    def __init__(self):
        self.items = []

    # Enqueue item (insert at end)
    def enqueue(self, item):
        self.items.append(item)

    # Dequeue item (remove from front)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return "Queue is empty"

    # Peek first item
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return "Queue is empty"

    # Check if queue is empty
    def is_empty(self):
        return len(self.items) == 0

    # Get size
    def size(self):
        return len(self.items)

    # Print queue
    def print_queue(self):
        print(self.items)


# ---------------- Example Usage ----------------
if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.print_queue()    # [10, 20, 30]
    print(q.dequeue()) # 10
    print(q.peek())    # 20
    print(q.size())    # 2
