#Clase LDE (Lista Doblemente Entrelazada)
class lde:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# Function to insert a node at the beginning of a doubly linked list
def list_insert(head, data):
    new_node = lde(data)
    new_node.next = head
    if head:
        head.prev = new_node
    return new_node

# Function to display the elements of the doubly linked list
def display(head):
    current = head
    while current:
        print(current.data, end=" <-> ")
        current = current.next
    print("None")



