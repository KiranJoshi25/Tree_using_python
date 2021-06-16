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



    def insert(self,data):
        self.no_of_nodes+=1

        if (self.root == None):
            self.root = Node(data)

        else:
            self.insert_node(data,self.root)




T = Tree()
T.insert(12)
T.insert(8)
T.insert(18)
print(T.no_of_nodes)
print(T.root.data)
print(T.root.left.data)
print(T.root.right.data)
