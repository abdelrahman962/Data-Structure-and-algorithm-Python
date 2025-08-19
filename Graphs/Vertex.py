

from Edge import Edge
class Vertex:
    def __init__(self,label):
        self.label=label
        self.edges=[]
    
    def add_edge(self,target,weight):
        new_edge=Edge(target,weight)
        self.edges.append(new_edge)

    def remove_edge(self,target):
        for e in self.edges:
            if e.target==target:
                self.edges.remove(e)
                return
    
    def remove_edge_version2(self,target):
        cop=[]
        for e in self.edges:
            if e.target!=target:
                cop.append(e)

        self.edges=cop        
                








def main():
   pass