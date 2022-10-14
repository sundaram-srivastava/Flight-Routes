class Graph:


    def __init__(self,edge):
        self.edge=edge
        self.graph_dict={}
        for start, end in self.edge:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start]=[end]
        print("Graphh dict:",self.graph_dict)


    def get_paths(self,start,end,path=[]):
        path=path+[start]
        if start==end:
            return [path]
        if start not in self.graph_dict:
            return []
        paths=[]

        for node in self.graph_dict[start]:
            if node not in path:
                new_path=self.get_paths(node,end,path)
                for p in new_path:
                    paths.append(p)
        return paths
    
    def get_shortest_path(self,start,end,path=[]):
        path =path +[start]
        if start==end:
            return path
        if start not in self.graph_dict:
            return None

        shortest_path=None
        for node in self.graph_dict[start]:
            if node not in path:
                sp=self.get_shortest_path(node,end,path)
                if sp:
                    if shortest_path is None or len(sp)<len(shortest_path):
                        shortest_path=sp
        return shortest_path



if __name__=='__main__':
    routes=[
        ("Gorakhpur","Delhi"),
        ("Gorakhpur","Indore"),
        ("Delhi","Indore"),
        ("Delhi","Pune"),
        ("Indore","Pune"),
        ("Pune","Mumbai")
    ]

    route_graph=Graph(routes)

    start="Mumbai"
    end="New York"

    print(f"shortest Paths between {start} and {end}:",route_graph.get_shortest_path(start,end))