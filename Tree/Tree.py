from Node import Node

class Tree:
    def __init__(self):
        self.root=None


    def insert(self,data):
        if self.root==None:
            self.root=Node(data) 

        else :
            self._insert(self.root,data)

    def _insert(self,node,data):
        if node.left is None:
            node.left=Node(data)
        elif node.right is None:
            node.right=Node(data)
        else:
            self._insert(node.left,data)        
    

    def search(self,node,target):
        if self.root is None:
            print("Error: tree is empty")
            return False
        
        if node is None:
            return False
        elif node.data==target:
            return True
        return self.search(node.left,target) or self.search(node.right,target)
           

     
    def delete(self, root, key):
        if root is None:
            print("Error: tree is empty")
            return None

        if root.data == key:
            # Case 1: No children
            if root.left is None and root.right is None:
                return None
            # Case 2: One child
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            # Case 3: Two children
            else:
                # Find in-order successor (smallest in right subtree)
                succ_parent = root
                succ = root.right
                while succ.left:
                    succ_parent = succ
                    succ = succ.left

                # ✅ Step you missed: Replace root's data with successor's data
                root.data = succ.data

                # Remove successor node
                if succ_parent != root:
                    succ_parent.left = succ.right
                else:
                    succ_parent.right = succ.right

                return root

        # Recurse into left and right subtrees
        root.left = self.delete(root.left, key)
        root.right = self.delete(root.right, key)
        return root

    

    def display(self,node):
        if node is None:
            return
        self.display(node.left)
        print(node.data,"->")
        self.display(node.right)



def valid_Bst(node):
    return validate(node,float('-inf'),float('inf'))

def validate(node,min_value,max_value):
    if node==None:
        return True
    
    if not(min_value<node.data<max_value):
        return False
    return(validate(node.left,min_value,node.data))and(validate(node.right,node.data,max_value))




tree = Tree()
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(3)
print(tree.search(tree.root, 5))  # True
tree.display(tree.root)
tree.root = tree.delete(tree.root, 5)
print(tree.search(tree.root, 5))  # False
tree.display(tree.root)
