class Node:
    _id_counter = 0

    def __init__(self, priority, distance, next_node=None):
        Node._id_counter += 1
        self.id = Node._id_counter
        self.priority = priority
        self.distance = distance
        self.next = next_node


class RescueList:

    def __init__(self):
        self.head = None

    def add_element(self, node):
        if not self.head:
            self.head = node
            return

        if (node.priority > self.head.priority) or \
                (node.priority == self.head.priority and node.distance < self.head.distance):
            node.next = self.head
            self.head = node
            return
        current = self.head

        while current.next:
            if (node.priority > current.next.priority) or \
                    (node.priority == current.next.priority and node.distance < current.next.distance):
                break
            current = current.next

        node.next = current.next
        current.next = node

    def display(self):
        newline = ''

        current = self.head
        while current:
            print(f"ID: {current.id}, Priority: {current.priority}, Distance: {current.distance}")
            current = current.next


list1 = RescueList()
list1.add_element(Node(5, 52))
list1.add_element(Node(10, 2))
list1.add_element(Node(5, 10))
list1.add_element(Node(7, 30))

list1.display()
