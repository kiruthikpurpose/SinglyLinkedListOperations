class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_at_middle(self, data, position):
        new_node = Node(data)
        if position == 0:
            self.insert_at_start(data)
            return
        temp = self.head
        for i in range(position - 1):
            if temp is None:
                print("Position out of bounds")
                return
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

    def delete_at_start(self):
        if not self.head:
            raise Exception("List is empty")
        self.head = self.head.next

    def delete_at_end(self):
        if not self.head:
            raise Exception("List is empty")
        if not self.head.next:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    def delete_at_middle(self, position):
        if position == 0:
            self.delete_at_start()
            return
        temp = self.head
        for _ in range(position - 1):
            if temp is None or temp.next is None:
                raise Exception("Position out of bounds")
            temp = temp.next
        temp.next = temp.next.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=' -> ')
            temp = temp.next
        print('None')


sll = SinglyLinkedList()
sll.insert_at_start(1)
sll.insert_at_start(5)
sll.insert_at_end(2)
sll.insert_at_middle(3, 1)
sll.delete_at_start()
sll.delete_at_end()
sll.delete_at_middle(0)
print(sll.traverse())
