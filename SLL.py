class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def append(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr=curr.next
        curr.next=new_node
        return new_node
    def insert_after(self,prev_val,data):
        curr = self.head
        while curr and curr.data != prev_val:
            curr=curr.next
        if not curr:
            print("Not found!")
        new_node = Node(data)
        new_node.next = curr.next
        curr.next=new_node
    def delete_node(self,data):
        curr = self.head
        if not curr:
            return
        if curr.data == data:
            self.head = curr.next
        prev = None
        while curr and curr.data != data:
            prev = curr
            curr = curr.next
        prev.next = curr.next
    def print_node(self):
        curr = self.head
        while curr:
            print(curr.data,end="->")
            curr=curr.next
        print("None")
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.insert_after(2,4)
    ll.print_node()
    ll.delete_node(4)
    ll.print_node()
            
            
