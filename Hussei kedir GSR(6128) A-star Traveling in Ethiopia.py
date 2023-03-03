#!/usr/bin/env python
# coding: utf-8

# In[8]:


from heapq import heappush, heappop
EthioMapWeighted = {
    'Asmara': [('Adigrat', 9), ('Axum', 5)],
    'Adigrat': [('Mekelle', 4), ('Adwa', 4), ('Asmara', 9)],
    'Adwa': [('Adigrat', 4), ('Mekelle', 7), ('Axum', 1)],
    'Axum': [('Asmara', 5), ('Adwa', 1), ('Shire', 2)],
    'Mekelle': [('Adigrat', 4), ('Adwa', 7), ('Sekota', 9), ('Alamata', 5)],
    'Shire': [('Debarke', 7), ('Humera', 8), ('Axum',2)],
    'Humera': [('Kartum', 21), ('Gondar', 9), ('Shire', 8)],
    'Debarke': [('Shire', 7), ('Gondar', 4)],
    'Kilbet Rasu': [('Fanti Rasu', 6)],
    'Fanti Rasu': [('Samara', 7), ('Kilbet Rasu', 6)],
    'Samara': [('Fanti Rasu',7 ), ('Alamata', 11), ('Woldiya', 8), ('Gabi Rasu', 9)],
    'Alamata': [('Samara', 11), ('Mekelle', 5), ('Sekota', 6), ('Woldiya', 3)],
    'Sekota': [('Lalibela', 6), ('Alamata', 6), ('Mekelle', 9)],
    'Woldiya': [('Samara', 8), ('Alamata', 3), ('Lalibela', 7), ('Dessie', 6)],
    'Lalibela': [('Woldiya', 7), ('Sekota', 6), ('Debre Tabor', 8)],
    'Debre Tabor': [('Lalibela', 8), ('Bahir Dar', 4)],
    'Gondar': [('Metema', 7), ('Azezo', 1), ('Debarke', 4), ('Humera', 9)],
    'Bahir Dar': [('Debre Tabor', 4), ('Azezo', 7), ('Metekel', 11), ('Injibara', 4), ('Finote Selam', 6)],
    'Azezo': [('Gondar', 1), ('Metema', 7), ('Bahir Dar', 7)],
    'Humera': [('Shire', 8), ('Kartum', 21), ('Gondar', 9)],
    'Kartum': [('Humera', 21), ('Metema', 19)],
    'Metema': [('Azezo', 7), ('Kartum', 19), ('Gondar', 7)],
    'Metekel': [('Bahir Dar', 11)],
    'Injibara': [('Bahir Dar', 4), ('Finote Selam', 2)],
    'Finote Selam': [('Injibara', 2), ('Debre Markos', 3), ('Bahir Dar', 6)],
    'Debre Markos': [('Finote Selam', 3), ('Debre Sina', 17)],
    'Debre Sina': [('Kemise', 6), ('Debre Markos', 17), ('Debre Birhan', 2)],
    'Kemise': [('Dessie', 4), ('Debre Sina', 6)],
    'Dessie': [('Woldiya', 6), ('Kemise', 4)],
    'Gabi Rasu': [('Awash', 5), ('Samara', 9)],
    'Assosa': [('Dembi Dolo', 12)],
    'Dembi Dolo': [('Gimbi', 6), ('Assosa', 12), ('Gambela', 4)],
    'Gimbi': [('Nekemete', 4), ('Dembi Dolo', 6)],
    'Nekemete': [('Ambo', 9), ('Gimbi', 4), ('Bedelle', 4)],
    'Debre Birhan': [('Debre Sina', 2), ('Addis Ababa', 5)],
    'Ambo': [('Addis Ababa', 5), ('Nekemete', 9), ('Wolkite', 6)],
    'Addis Ababa': [('Debre Birhan', 5), ('Ambo', 5), ('Adama', 3)],
    'Adama': [('Matahara', 3), ('Addis Ababa', 3), ('Batu', 4), ('Assella', 4)],
    'Matahara': [('Awash', 1), ('Adama', 3)],
    'Awash': [('Chiro', 4), ('Gabi Rasu', 5), ('Matahara', 1)],
    'Chiro': [('Awash', 4), ('Dire Dawa', 8)],
    'Dire Dawa': [('Harar', 4), ('Chiro', 8)],
    'Harar': [('Babile', 2), ('Dire Dawa', 4)],
    'Babile': [('Jigjiga', 3), ('Harar', 2), ('Goba', 28)],
    'Jigjiga': [('Dega Habur', 5), ('Babile', 3)],
    'Dega Habur': [('Kebri Dahar', 6), ('Jigjiga', 5)],
    'Werder': [('Kebri Dahar', 6)],
    'Kebri Dahar': [('Werder', 6), ('Dega Habur', 6), ('Gode', 5)],
    'Sof Oumar': [('Gode', 23), ('Goba', 6), ('Bale', 23)],
    'Goba': [('Sof Oumar', 6), ('Babile', 28), ('Bale', 18)],
    'Bale': [('Sof Oumar', 23), ('Goba', 18), ('Dodolla', 13), ('Liben', 11)],
    'Dodolla': [('Bale', 13), ('Assasa', 1), ('Shashemene', 3)],
    'Assasa': [('Dodolla', 1), ('Assella', 4)],
    'Assella': [('Assasa', 4), ('Adama', 4)],
    'Batu': [('Adama', 4), ('Buta Jira', 2), ('Shashemene', 3)],
    'Buta Jira': [('Batu', 2), ('Worabe', 2)],
    'Worabe': [('Wolkite', 5), ('Hossana', 2), ('Buta Jira', 2)],
    'Wolkite': [('Worabe', 5), ('Ambo', 6), ('Jimma', 8)],
    'Bedelle': [('Jimma', 7), ('Nekemete', 4), ('Gore', 6)],
    'Gambela': [('Gore', 5), ('Dembi Dolo', 4)],
    'Gore': [('Bedelle', 6), ('Gambela', 5), ('Tepi', 9)],
    'Tepi': [('Mezan Teferi', 4), ('Bonga', 8), ('Gore', 9)],
    'Mezan Teferi': [('Bonga', 4), ('Tepi', 4)],
    'Bonga': [('Jimma', 4), ('Tepi', 8), ('Mezan Teferi', 4), ('Dawro', 10)],
    'Jimma': [('Wolkite', 8), ('Bedelle', 7), ('Bonga', 4)],
    'Dawro': [('Wolaita Sodo', 6), ('Bonga', 10)],
    'Wolaita Sodo': [('Hossana', 4), ('Dawro', 6), ('Arba Minch', 4)],
    'Hossana': [('Wolaita Sodo', 4), ('Worabe', 2), ('Shashemene', 7)],
    'Shashemene': [('Hawassa', 1), ('Hossana',7 ), ('Batu', 3), ('Dodolla', 3)],
    'Hawassa': [('Shashemene', 1), ('Dilla', 3)],
    'Dilla': [('Hawassa', 3), ('Bule Hora', 4)],
    'Bule Hora': [('Dilla', 4), ('Yabello', 2)],
    'Konso': [('Arba Minch', 4), ('Yabello', 3)],
    'Arba Minch': [('Konso', 4), ('Basketo', 10), ('Wolaita Sodo', 4)],
    'Basketo': [('Bench Maji', 5), ('Arba Minch', 10)],
    'Bench Maji': [('Juba', 22), ('Basketo', 5)],
    'Juba': [('Bench Maji', 22)],
    'Yabello': [('Konso', 3), ('Bule Hora', 2), ('Moyale', 6)],
    'Moyale': [('Yabello', 6), ('Nairobi', 22)],
    'Nairobi': [('Moyale', 22)],
    'Liben': [('Bale', 11)],
    'Dollo': [('Gode', 17)],
    'Gode': [('Dollo', 17), ('Sof Oumar', 23), ('Kebri Dahar', 5), ('Mokadisho', 22)],
    'Mokadisho': [('Gode', 22)],
}
H = {
    'Asmara': 68,'Adigrat': 62,'Adwa': 65,'Axum': 66,'Mekelle': 58,'Shire': 67,'Humera': 65,'Debarke': 60,
    'Kilbet Rasu': 55,'Fanti Rasu': 49,'Samara': 42,'Alamata': 53,'Sekota': 59,'Woldiya': 50,'Lalibela': 57,
    'Debre Tabor': 52,'Gondar': 56,'Bahir Dar': 48,'Azezo': 55,'Humera': 65,'Kartum': 81,'Metema': 62,'Metekel': 59,
    'Injibara': 44,'Finote Selam': 42,'Debre Markos': 39,'Debre Sina': 33,'Kemise': 40,'Dessie': 44,'Gabi Rasu': 32,
    'Assosa': 51,'Dembi Dolo': 49,'Gimbi': 43,'Nekemete': 39,'Debre Birhan': 31,'Ambo': 31,'Addis Ababa': 26,
    'Adama': 23,'Matahara': 26,'Awash': 27,'Chiro': 31,'Dire Dawa': 31,'Harar': 35,'Babile': 37,'Jigjiga': 40,
    'Dega Habur': 45,'Werder': 46,'Kebri Dahar': 40,'Sof Oumar': 45,'Goba': 40,'Bale': 22,'Dodolla': 19,'Assasa': 18,
    'Assella': 22,'Batu': 19,'Buta Jira': 21,'Worabe': 22,'Wolkite': 25,'Bedelle': 40,'Gambela': 51,'Gore': 46,
    'Tepi': 41,'Mezan Teferi': 37,'Bonga': 33,'Jimma': 33,'Dawro': 23,'Wolaita Sodo': 17,'Hossana': 21,
    'Shashemene': 16,'Hawassa': 15,'Dilla': 12,'Bule Hora': 8,'Konso': 9,'Arba Minch': 13,'Basketo': 23,
    'Bench Maji': 28,'Juba': 50,'Yabello': 6,'Moyale': 0,'Nairobi': 22,'Liben': 11,'Dollo': 18,'Gode': 35,'Mokadisho': 40,
}

class PriorityQueue:
    
    def __init__(self, iterable=[]):
        self.heap = []
        for value in iterable:
            heappush(self.heap, (0, value))
    
    def add(self, value, priority=0):
        heappush(self.heap, (priority, value))
    
    def pop(self):
        priority, value = heappop(self.heap)
        return value
    
    def __len__(self):
        return len(self.heap)
    
def a_star_graph_search(graph,heuristic,start,goal):
    visited = set()
    parent = dict()
    distance = {start: 0}
    frontier = PriorityQueue()
    frontier.add(start)
    while frontier:
        node = frontier.pop()
        if node in visited:
            continue
        if node == goal:
            return (distance[node],Backtrace(parent, start, node))
        visited.add(node)
        for successor in graph[node]:
            if successor[0] in visited:
                continue
            frontier.add(successor[0], distance[node] + successor[1] + heuristic[successor[0]])
            if (successor[0] not in distance) or (distance[node] + successor[1] < distance[successor[0]]):
                distance[successor[0]] = distance[node] + successor[1]
                parent[successor[0]] = node
    return None

def Backtrace(parent, start, end): 
    path = [end]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()
    return path
print(a_star_graph_search(EthioMapWeighted, H, 'Addis Ababa', 'Moyale'))


# In[ ]:




