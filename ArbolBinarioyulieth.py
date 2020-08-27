class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)


def traverse(root):
    current_level = [root]
    while current_level:
        print(" -------- "), print(" ----  ".join(str(node) for node in current_level))
        
        next_level = list()
        for n in current_level:
            if n.left:
                
                next_level.append(n.left)
            if n.right:
               
                next_level.append(n.right)
        current_level = next_level

t = Node(3,Node(5,Node(9),Node(4,Node(21))),Node(7,Node(10),Node(15)))

traverse(t) 