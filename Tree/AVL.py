class AVLNode:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
        self.height=1

class AVLTree:


    def get_height(self,node):
        return node.height if node else 0


    def get_balance(self,node):
        return self.get_height(node.left)-self.get_height(node.right) if node else 0
      

    
    def rotate_right(self,y):
        x=y.left
        T2=x.right
        x.right=y
        y.left=T2
        y.height=max(self.get_height(y.left),self.get_height(y.right))+1
        x.height=max(self.get_height(x.left),self.get_height(x.right))+1
        return x


    def rotate_left(self,x):
        y=x.right
        T2=y.left
        y.left=x
        x.right=T2
        y.height=max(self.get_height(y.left),self.get_height(y.right))+1
        x.height=max(self.get_height(x.left),self.get_height(x.right))+1
        return y
    

    def rebalance(self,node):
        bf=self.get_balance(node)
        if bf>1:
            if self.get_balance(node.left)<0:
                node.left=self.rotate_left(node.left)
            return self.rotate_right(node)    
        
        elif bf<-1:
            if self.get_balance(node.right)>0:
                node.right=self.rotate_right(node.right)
            return self.rotate_left(node)    
        
        return node
    
    def insert(self,root,key):
        if root==None:
            return AVLNode(key)
        if key<root.key:
           root.left= self.insert(root.left,key)

        else:
           root.right= self.insert(root.right,key)    
        root.height=max(self.get_height(root.left),self.get_height(root.right))+1
        return self.rebalance(root)
    

    def find_min(self,root):
        while root.left:
            root=root.left

        return root 
        

    def delete(self,root,key):
        if root is None:
            return

        if key<root.key:
           root.left= self.delete(root.left,key)

        elif key>root.key:
           root.right= self.delete(root.right,key) 

        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            temp=self.find_min(root.right)
            root.key=temp.key
            root.right=self.delete(root.right,temp.key)      
        root.height=max(self.get_height(root.left),self.get_height(root.right))+1
        return self.rebalance(root)
    
    def K_Element(self,root):
        if self.root==None:
            return
        


def validate_AVL(node,avl):
    if not node:
        return True
    bf=avl.get_balance(node)
    if abs(bf)>1:
        return False
    
    return validate_AVL(node.left,avl) and validate_AVL(node.right,avl)
    

def range_search(root, low, high):
    result=[]
    if root is None:
        return
    
    def inOrder(node):
        if root.key>low:
            inOrder(node.left)
            
        if low<=node.key<=high:
            result.append(node.key)
        if node.key<high:
            inOrder(node.right)
    inOrder(root) 
    return result           

def main():
    avl = AVLTree()
    root = None

    # Insert elements
    keys_to_insert = [40, 20, 60, 10, 30, 50, 70.]
    print("Inserting:")
    for key in keys_to_insert:
        print(f"Inserting {key}")
        root = avl.insert(root, key)
    print(range_search(root,25,65))

main()