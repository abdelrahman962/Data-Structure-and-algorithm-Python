from Vertex import Vertex
import heapq
class Graph:
    def  __init__(self):
        self.vertecis=[]
        


    def add_vertex(self,label):
        new_vertex=Vertex(label)
        for v in self.vertecis:
            if v.label==label:
                print("error")
                return
            
        self.vertecis.append(new_vertex)


    def find_vertex(self,label):
        for v in self.vertecis:
            if v.label==label:
                return v
            

        return None


    def add_edge(self,label,target,weight):
        v1=self.find_vertex(label)
        v2=self.find_vertex(target)

        if  v1 and v2:
           v1.add_edge(target,weight)
           v2.add_edge(label,weight)#undirected graph

        else:
            print("error")

    def remove_vertex(self,label):
        v1=self.find_vertex(label)
        if v1:
            for v in self.vertecis:

                if  v1!=v:
                    v1.remove_edge(v.label)
            self.vertecis.remove(v1)

    def remove_edge(self,from_label,to_label):
        from_vertex=self.find_vertex(from_label)
        to_vertex=self.find_vertex(to_label)
        if from_vertex and to_vertex:
            from_vertex.remove_edge(to_label)

        else:
            return None       



    def BFS(self,start_label):
        visited=set()
        queue=[]
        order=[]
        queue.append(start_label)

        while queue:
            v=queue.pop(0)
            if v not in visited:
                visited.add(v)
                order.append(v)
            v1=self.find_vertex(v)
    
            if not v1:
              return    
            for edge in v1.edges:
                target=edge.target
                if target not in queue and target not in visited:
                    queue.append(target)    
        return order


    def DFS(self,start_label):
        visited=set()
        stack=[start_label]
        order=[]

        while stack:
            v=stack.pop()
            if v not in visited:
                visited.add(v)
                order.append(v)
            v1=self.find_vertex(v)
            if not v1:
               return    
            for edge in  reversed(v1.edges):
                target=edge.target
                if target not in stack and target not in visited:
                 stack.append(edge.terget)
        return order         

    def Dijkstra(self,start_label):
    
        distances={}
        for v in self.vertecis:
            distances[v.label]=float('inf')

        distances[start_label]=0    
        visited=set()

        pq=[(0,start_label)]

        while pq:
            current_distance,current_label=heapq.heappop(pq)

            if current_label in visited:
                continue

            visited.add(current_label)
            current_vertex=self.find_vertex(current_label)
            for edge in current_vertex.edges:
                neighbor=edge.target
                weight=edge.weight

                if current_distance+weight<distances[neighbor]:
                    distances[neighbor]=current_distance+weight
                    heapq.heappush(pq, (distances[neighbor], neighbor))


        return distances             

    def path_exist(self,from_vertex,to_vertex):
        visited=set()
        queue=[]
        queue.append(from_vertex)

        while queue:
            v=queue.pop(0)

            if v==to_vertex:
                return True
            if v not in visited:
                visited.add(v)
            v1=self.find_vertex(v)
    
            if not v1:
              return    
            for edge in v1.edges:
                target=edge.target
                if target not in queue and target not in visited:
                    queue.append(target)   


        return False  

    def cycle_detection(self):
        visited=set()
        rec_stack=set()
        def dfs(v):
            visited.add(v)
            rec_stack.add(v)

            current_vertex=self.find_vertex(v)
            if not current_vertex:
                return False
            
            for edge in current_vertex.edges:
                neighbor=edge.target
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
                elif neighbor in rec_stack:
                    return True
                
            rec_stack.remove(v)

            return False    
        
        for vertex in self.vertecis:
            if vertex.label not in visited:
                if dfs(vertex.label):
                    return True

        return False   



    def cycle_detection2(self):
        visited=set()
        start_vertex=self.vertecis[0]
        stack=[start_vertex.label]
        if not start_vertex:
            return False
        
        while stack:
            current=stack.pop(0)

            if current in visited:
                return True
            
            visited.add(current)
            current_vertex=self.find_vertex(current)
            for edge in current_vertex.edges:
                if edge.target not in visited:
                    stack.append(edge.target)


        return False         





g = Graph()
# Add vertices
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')

# Add directed edges to form a cycle: B → C → D → B
g.find_vertex('A').add_edge('B', 1)
g.find_vertex('B').add_edge('C', 1)
g.find_vertex('C').add_edge('D', 1)
g.find_vertex('D').add_edge('B', 1)

# Check for cycle
print("Cycle Detected?" , g.cycle_detection())