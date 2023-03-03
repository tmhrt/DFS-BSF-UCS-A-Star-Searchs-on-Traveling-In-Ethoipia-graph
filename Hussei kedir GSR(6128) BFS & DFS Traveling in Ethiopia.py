#!/usr/bin/env python
# coding: utf-8

# In[70]:


EthioMap = {
    'Asmara': ['Adigrat', 'Axum'],
    'Adigrat': ['Mekelle', 'Adwa', 'Asmara'],
    'Adwa': ['Mekelle', 'Adigrat', 'Axum'],
    'Axum': ['Asmara', 'Adwa', 'Shire'],
    'Mekelle': ['Adigrat', 'Adwa', 'Sekota', 'Alamata'],
    'Shire': ['Debarke', 'Humera', 'Axum'],
    'Humera': ['Kartum', 'Gondar', 'Shire'],
    'Debarke': ['Shire', 'Gondar'],
    'Kilbet Rasu': ['Fanti Rasu'],
    'Fanti Rasu': ['Samara', 'Kilbet Rasu'],
    'Samara': ['Fanti Rasu', 'Alamata', 'Woldiya', 'Gabi Rasu'],
    'Alamata': ['Samara', 'Mekelle', 'Sekota', 'Woldiya'],
    'Sekota': ['Lalibela', 'Alamata', 'Mekelle'],
    'Woldiya': ['Samara', 'Alamata', 'Lalibela', 'Dessie'],
    'Lalibela': ['Woldiya', 'Sekota', 'Debre Tabor'],
    'Debre Tabor': ['Lalibela', 'Bahir Dar'],
    'Gondar': ['Metema', 'Azezo', 'Debarke', 'Humera'],
    'Bahir Dar': ['Debre Tabor', 'Azezo', 'Metekel', 'Injibara', 'Finote Selam'],
    'Azezo': ['Gondar', 'Metema', 'Bahir Dar'],
    'Humera': ['Shire', 'Kartum', 'Gondar'],
    'Kartum': ['Humera', 'Metema'],
    'Metema': ['Azezo', 'Kartum', 'Gondar'],
    'Metekel': ['Bahir Dar', 'Assosa'],
    'Injibara': ['Bahir Dar', 'Finote Selam'],
    'Finote Selam': ['Injibara', 'Debre Markos', 'Bahir Dar'],
    'Debre Markos': ['Finote Selam', 'Debre Sina'],
    'Debre Sina': ['Kemise', 'Debre Markos', 'Debre Birhan'],
    'Kemise': ['Dessie', 'Debre Sina'],
    'Dessie': ['Woldiya', 'Kemise'],
    'Gabi Rasu': ['Awash', 'Samara'],
    'Assosa': ['Metekel', 'Dembi Dolo'],
    'Dembi Dolo': ['Gimbi', 'Assosa', 'Gambela'],
    'Gimbi': ['Nekemete', 'Dembi Dolo'],
    'Nekemete': ['Ambo', 'Gimbi', 'Bedelle'],
    'Debre Birhan': ['Debre Sina', 'Addis Ababa'],
    'Ambo': ['Addis Ababa', 'Nekemete', 'Wolkite'],
    'Addis Ababa': ['Debre Birhan', 'Ambo', 'Adama'],
    'Adama': ['Matahara', 'Addis Ababa', 'Batu', 'Assella'],
    'Matahara': ['Awash', 'Adama'],
    'Awash': ['Chiro', 'Gabi Rasu', 'Matahara'],
    'Chiro': ['Awash', 'Dire Dawa'],
    'Dire Dawa': ['Harar', 'Chiro'],
    'Harar': ['Babile', 'Dire Dawa'],
    'Babile': ['Jigjiga', 'Harar'],
    'Jigjiga': ['Dega Habur', 'Babile'],
    'Dega Habur': ['Kebri Dahar', 'Jigjiga', 'Goba'],
    'Werder': ['Kebri Dahar'],
    'Kebri Dahar': ['Werder', 'Dega Habur', 'Sof Oumar', 'Gode'],
    'Sof Oumar': ['Kebri Dahar', 'Goba', 'Bale'],
    'Goba': ['Sof Oumar', 'Dega Habur', 'Bale'],
    'Bale': ['Sof Oumar', 'Goba', 'Dodolla', 'Liben'],
    'Dodolla': ['Bale', 'Assasa', 'Shashemene'],
    'Assasa': ['Dodolla', 'Assella'],
    'Assella': ['Assasa', 'Adama'],
    'Batu': ['Adama', 'Buta Jira', 'Shashemene'],
    'Buta Jira': ['Batu', 'Worabe'],
    'Worabe': ['Wolkite', 'Hossana', 'Buta Jira'],
    'Wolkite': ['Worabe', 'Ambo', 'Jimma'],
    'Bedelle': ['Jimma', 'Nekemete', 'Gore'],
    'Gambela': ['Gore', 'Dembi Dolo'],
    'Gore': ['Bedelle', 'Gambela', 'Tepi'],
    'Tepi': ['Mezan Teferi', 'Bonga', 'Gore'],
    'Mezan Teferi': ['Bonga', 'Tepi', 'Basketo'],
    'Bonga': ['Jimma', 'Tepi', 'Mezan Teferi', 'Dawro'],
    'Jimma': ['Wolkite', 'Bedelle', 'Bonga'],
    'Dawro': ['Wolaita Sodo', 'Bonga', 'Basketo'],
    'Wolaita Sodo': ['Hossana', 'Dawro', 'Arba Minch'],
    'Hossana': ['Wolaita Sodo', 'Worabe', 'Shashemene'],
    'Shashemene': ['Hawassa', 'Hossana', 'Batu', 'Dodolla'],
    'Hawassa': ['Shashemene', 'Dilla'],
    'Dilla': ['Hawassa', 'Bule Hora'],
    'Bule Hora': ['Dilla', 'Yabello'],
    'Konso': ['Arba Minch', 'Yabello'],
    'Arba Minch': ['Konso', 'Basketo', 'Wolaita Sodo'],
    'Basketo': ['Bench Maji', 'Mezan Teferi', 'Dawro', 'Arba Minch'],
    'Bench Maji': ['Juba', 'Basketo'],
    'Juba': ['Bench Maji'],
    'Yabello': ['Konso', 'Bule Hora', 'Moyale'],
    'Moyale': ['Yabello', 'Nairobi'],
    'Nairobi': ['Moyale'],
    'Liben': ['Bale'],
    'Dollo': ['Gode'],
    'Gode': ['Dollo', 'Kebri Dahar', 'Mokadisho'],
    'Mokadisho': ['Gode'],
}
class Graph:
 
    # Constructor
    def __init__(self, g):
 
        # default dictionary to store graph
        self.graph = g
        self.visited = set()
        self.traversal_output = []
        self.frontier = []
        
    def Search(self, start, goal, strategy):
        if (start in self.graph.keys()) and (goal in self.graph.keys()):
            if strategy == "DFS":
                print("Performing depth-forst-search***")
                return self.DFS(start, goal)
            if strategy == "BFS":
                print("Performing breadth-forst-search***")
                return self.BFS(start, goal)
        else:
            print("city not in graph")
                
    def DFSUtil(self, start, goal):
        self.visited.add(start)
        self.traversal_output.append(start)
        if start == goal:
            return self.traversal_output
        for city in self.graph[start]:
            if city not in self.visited:
                result = self.DFSUtil(city, goal)
                if result is not None:
                    return result
        self.traversal_output.pop()
    
    def DFS(self, startingNode, destinationNode):
        self.traversal_output.clear()
        self.visited.clear()
        if startingNode == destinationNode:
            return [destinationNode]
        else:
            return self.DFSUtil(startingNode,destinationNode)
        
    def Backtrace(self, parent, start, end):
        path = [end]
        while path[-1] != start:
            path.append(parent[path[-1]])
        path.reverse()
        return path
    
    def BFS(self, startingNode, destinationNode):
        parent = {}
        self.traversal_output.clear()
        self.frontier.clear()
        self.visited.clear()
        if startingNode == destinationNode:
            return [destinationNode]
        self.frontier.append(startingNode)
        self.visited.add(startingNode)
        while self.frontier:
            city = self.frontier.pop(0)
            if city == destinationNode:
                return self.Backtrace(parent, startingNode, destinationNode)
            for adjacent in self.graph[city]:
                if adjacent not in self.visited:
                    self.visited.add(adjacent)
                    self.frontier.append(adjacent)
                    parent[adjacent] = city

Ethio = Graph(EthioMap)
print(Ethio.Search('Asmara', 'Nairobi', "DFS"))
print(Ethio.Search('Asmara', 'Nairobi', "BFS"))


# In[ ]:




