#!/usr/bin/env python
# coding: utf-8

# In[19]:


import numpy as np
CoffeMap = {
    'Addis Ababa': ['Ambo', 'Buta Jirra','Adama'],
    'Ambo': ['Gode','Nekemte'],
    'Buta Jirra': ['Worabe','Welkite'],
    'Adama': ['Mojo','Dire Dawa'],
    'Gode': ['Fiche','Shambu'],
    'Nekemte': ['Gimbi','Limu'],
    'Worabe': ['Hossana','Durame'],
    'Welkite': ['Bench Maji','Tepi'],
    'Mojo': ['Kaffa','Dilla'],
    'Dire Dawa': ['Chiro','Harar'],
}
Leaf = {
    'Fiche': 5,
    'Shambu': 4,
    'Gimbi': 8,
    'Limu': 8,
    'Hossana': 6,
    'Durame': 5,
    'Bench Maji': 5,
    'Tepi': 6,
    'Kaffa': 7,
    'Dilla': 9,   
    'Chiro': 6,
    'Harar': 10,
}
class MinMax:
    # Constructor
    def __init__(self, g, l):
        self.graph = g
        self.leaf = l
        self.last_choosen_path = None        
    def Value(self, state, isMax):
        if state in self.leaf:#leaf node
            return self.leaf[state]
        val = []
        for child in self.graph[state]:
            val.append(self.Value(child, not isMax))
        if isMax:
            self.last_choosen_path = self.graph[state][np.argmax(val)]
            return max(val)
        else:
            self.last_choosen_path = self.graph[state][np.argmin(val)]
            return min(val)
    def Search(self, state):
        path = [state]
        self.last_choosen_path = state
        while self.last_choosen_path in self.graph: #repeat untill reaching leaf node
            self.Value(self.last_choosen_path, True)
            path.append(self.last_choosen_path)
        return path
                
CoffeRace = MinMax(CoffeMap, Leaf)
print(CoffeRace.Search('Addis Ababa'))


# In[ ]:




