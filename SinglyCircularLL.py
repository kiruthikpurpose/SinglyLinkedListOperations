class CircularNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyCircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        new_node = CircularNode(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        new_node.next = self.head
        self.head = new_node
        temp.next = new_node

    def insert_at_end(self, data):
        new_node = CircularNode(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head

    def insert_at_middle(self, data, position):
        new_node = CircularNode(data)
        if position == 0:
            self.insert_at_start(data)
            return
        temp = self.head
        for _ in range(position - 1):
            if temp.next == self.head:
                raise Exception("Position out of bounds")
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

    def delete_at_start(self):
        if not self.head:
            raise Exception("List is empty")
        if self.head.next == self.head:
            self.head = None
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = self.head.next
        self.head = self.head.next

    def delete_at_end(self):
        if not self.head:
            raise Exception("List is empty")
        if self.head.next == self.head:
            self.head = None
            return
        temp = self.head
        while temp.next.next != self.head:
            temp = temp.next
        temp.next = self.head

    def delete_at_middle(self, position):
        if position == 0:
            self.delete_at_start()
            return
        temp = self.head
        for _ in range(position - 1):
            if temp.next == self.head:
                raise Exception("Position out of bounds")
            temp = temp.next
        temp.next = temp.next.next

    def traverse(self):
        if not self.head:
            print('List is empty')
            return
        temp = self.head
        while True:
            print(temp.data, end=' <-> ')
            temp = temp.next
            if temp == self.head:
                break
        print('(head)')


scll = SinglyCircularLinkedList()
scll.insert_at_start(1)
scll.insert_at_end(2)
scll.insert_at_middle(3, 1)
scll.delete_at_start()
scll.delete_at_end()
scll.delete_at_middle(0)
print(scll.traverse())
