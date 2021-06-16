class Node:
    def __init__(self,data):

        self.data = data
        self.right = None
        self.left = None


class Tree:
    def __init__(self):
        self.root = None
        self.no_of_nodes = 0

    def insert_node(self,data,current_node):

        if current_node.data > data:

            if current_node.left is None:
                current_node.left = Node(data)

            else:
                current_node = current_node.left
                self.insert_node(data,current_node)

        else:

            if current_node.right is None:
                current_node.right = Node(data)

            else:
                current_node = current_node.right
                self.insert_node(data,current_node)



    def traverse_inorder(self,node):
        if node.left is not None:
            self.traverse_inorder(node.left)

        print(node.data)

        if node.right is not None:
            self.traverse_inorder(node.right)



    def traverse(self):
        if self.root is not None:
            self.traverse_inorder(self.root)



    def insert(self,data):
        self.no_of_nodes+=1

        if (self.root == None):
            self.root = Node(data)

        else:
            self.insert_node(data,self.root)



    def find_max(self):
        node = self.root
        while node.right is not None:
            node = node.right
        return node.data

    def find_min(self):
        node = self.root
        while node.left is not None:
            node = node.left
        return node.data


T = Tree()
T.insert(12)
T.insert(8)
T.insert(18)
T.insert(10)
T.insert(1)
T.insert(15)
T.insert(25)
T.insert(66)
T.insert(11)
T.insert(-5)

print(T.no_of_nodes)
T.traverse()
print("max",T.find_max())
print("min",T.find_min())