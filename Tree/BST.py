from Node import Node
from Tree import Tree
class BST:
    def __init__(self):
        self.root=None


    def insert(self,data):
        self.root=self._insert(self.root,data)  


    def _insert(self,node,data):
        if node==None:
            return Node(data) 

        if data<node.data:
            node.left=self._insert(node.left,data)

        else:
            node.right=self._insert(node.right,data)

        return node    
    
    def search(self,node,target):
        if self.root is None:
            print("Error: tree is empty")
            return False
        
        if node is None:
            return False
        elif node.data==target:
            return True
        
        elif node.data>target:
            return self.search(node.left,target)
        else: 
            return  self.search(node.right,target)
           





    def display(self,node):
        if node is None:
            return
        self.display(node.left)
        print(node.data,"->")
        self.display(node.right)

        
    def delete(self, root, key):
        if root is None:
            print("Error: tree is empty")
            return None

        if root.data == key:

            if root.left is None and root.right is None:
                return None

            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            else:
                succ_parent = root
                succ = root.right
                while succ.left:
                    succ_parent = succ
                    succ = succ.left

                root.data = succ.data

                if succ_parent != root:
                    succ_parent.left = succ.right
                else:
                    succ_parent.right = succ.right

                return root

        elif key<root.data:
            root.left = self.delete(root.left, key)
        else:    
           root.right = self.delete(root.right, key)
        return root
    

    def findMin(self):
        if self.root==None:
            return None
        
        min_value=self.root
        while min_value.left!=None:
            min_value=min_value.left

        return min_value.data    
    

    def findMax(self):
        if self.root==None:
            return None
        
        max_value=self.root
        while max_value.right!=None:
            max_value=max_value.right

        return max_value.data    
    


def balanced(root):
    return check_balanced(root)!=-1


def check_balanced(node):
    if node==None:
        return 0
    
    left_height=check_balanced(node.left)
    if left_height==-1:
        return -1
    right_height=check_balanced(node.right)
    if right_height==-1:
        return -1
    diff=abs(left_height-right_height)
    if diff>1:
        return -1
    return 1+max(left_height,right_height)

    

    
    





bs=BST()
bs.insert(3)
bs.insert(10)
bs.insert(2)
bs.insert(20)
bs.insert(30)
bs.insert(40)

print(bs.findMin())
print(bs.findMax())
print(balanced(bs.root))
