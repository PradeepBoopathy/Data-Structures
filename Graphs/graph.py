class Graph:
    def __init__(self,edges):
        self.edges = edges
        self.graph_dict = {}

        for start, end in self.edges:
            if start not in self.graph_dict:
                self.graph_dict[start] = [end]
            else:
                self.graph_dict[start].append(end)
        print('Constructed Graph:',self.graph_dict)

    def get_paths(self,start,end,path=[]):
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []

        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_path = self.get_paths(node,end,path)
                for p in new_path:
                    paths.append(p)
        return paths

    def get_shortest_paths(self,start,end,path=[]):
        path = path + [start]

        if start == end:
            return path

        if start not in self.graph_dict:
            return None

        shortest_path= None
        for node in self.graph_dict[start]:
            current_path = self.get_shortest_paths(node,end,path)
            if current_path:
                if shortest_path is None or len(current_path) < len(shortest_path):
                    shortest_path = current_path

        return shortest_path



if __name__ == '__main__':
    routes = [
        ('Mumbai', 'Paris'),
        ('Mumbai', 'Dubai'),
        ('Paris', 'Dubai'),
        ('Paris', 'New York'),
        ('Dubai', 'New York'),
        ('New York', 'Toronto')
    ]

    route = Graph(routes)

    print('Get Every Paths :',route.get_paths('Mumbai','New York'))
    print('Get Shortest Path :',route.get_shortest_paths('Mumbai', 'New York'))
    
    
    
'''
Output:
Constructed Graph: {'Mumbai': ['Paris', 'Dubai'], 'Paris': ['Dubai', 'New York'], 'Dubai': ['New York'], 'New York': ['Toronto']}
Get Every Paths : [['Mumbai', 'Paris', 'Dubai', 'New York'], ['Mumbai', 'Paris', 'New York'], ['Mumbai', 'Dubai', 'New York']]
Get Shortest Path : ['Mumbai', 'Paris', 'New York']
'''
