class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DoubleLinkedList:
    def __init__(self):
        self.head=None
    def append(self,data):
        new_node = Node(data)
        curr = self.head
        if not self.head:
            self.head = new_node
            return
        while curr.next:
            curr = curr.next
        curr.next=new_node
        new_node.prev = curr
        new_node.next=None
    def delete_node(self,data):
        curr = self.head
        while curr and curr.data != data:
            curr = curr.next
        if curr.prev:
            curr.prev.next=curr.next
        else:
            self.head = curr.next
        if curr.next:
            curr.next.prev = curr.prev
    def reverse_list(self):
        prev_node = None
        curr = self.head
        while curr:
            prev_node = curr.prev
            curr.prev = curr.next
            curr.next = prev_node
            curr = curr.prev
        if prev_node:
            self.head = prev_node.prev
            
            
    def print_list_forward(self):
        curr = self.head
        while curr is not None:
            print(curr.data,end="<->")
            curr = curr.next
        print("None")
if __name__ == "__main__":
    dll = DoubleLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.print_list_forward()
    dll.delete_node(2)
    dll.print_list_forward()
    dll.reverse_list()
    dll.print_list_forward()
            
