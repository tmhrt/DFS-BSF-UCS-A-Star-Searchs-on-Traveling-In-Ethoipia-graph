#!/usr/bin/env python
# coding: utf-8

# In[57]:


import numpy as np
from queue import PriorityQueue
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
    'Sof Oumer': [('Gode', 23), ('Goba', 6), ('Bale', 23)],
    'Goba': [('Sof Oumer', 6), ('Babile', 28), ('Bale', 18)],
    'Bale': [('Sof Oumer', 23), ('Goba', 18), ('Dodolla', 13), ('Liben', 11)],
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
    'Bule Hora': [('Dilla', 4), ('Yabello', 3)],
    'Konso': [('Arba Minch', 4), ('Yabello', 3)],
    'Arba Minch': [('Konso', 4), ('Basketo', 10), ('Wolaita Sodo', 4)],
    'Basketo': [('Bench Maji', 5), ('Arba Minch', 10)],
    'Bench Maji': [('Juba', 22), ('Basketo', 5)],
    'Juba': [('Bench Maji', 22)],
    'Yabello': [('Konso', 3), ('Bule Hora', 3), ('Moyale', 6)],
    'Moyale': [('Yabello', 6), ('Nairobi', 22)],
    'Nairobi': [('Moyale', 22)],
    'Liben': [('Bale', 11)],
    'Dollo': [('Gode', 17)],
    'Gode': [('Dollo', 17), ('Sof Oumer', 23), ('Kebri Dahar', 5), ('Mokadisho', 22)],
    'Mokadisho': [('Gode', 22)],
}
def Backtrace(parent, start, end): 
    path = [end]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()
    return path

def Search(graph, start, goal):
    if len(goal) == 1:
        return Uniform_cost_search(graph, start, goal)
    elif len(goal) > 1:
        total_path = []
        total_cost = 0
        while len(goal)>0:
            costs, path = Uniform_cost_search(graph, start, goal)
            total_path.append(path)  #append this path(best from the avalabe goals) to total path
            total_cost += min(costs)
            start = goal[np.argmin(costs)]  # new starting point will be theis reached goal
            del goal[np.argmin(costs)]  #remove the best goal from the avalabe goals
        return (total_cost, total_path)
            
def Uniform_cost_search(graph, start, goal):
     
    # minimum cost upto
    # goal state from starting
    parent = {}
    answer = []
 
    # create a priority queue
    queue = []
 
    # set the answer vector to max value
    for i in range(len(goal)):
        answer.append(10**8)
        
    # insert the starting index
    queue.append([0, start])
 
    # map to store visited node
    visited = []
 
    # count
    count = 0
 
    # while the queue is not empty
    while (len(queue) > 0):
        # get the top element of the
        queue = sorted(queue)
        p = queue[-1]
 
        # pop the element
        del queue[-1]
 
        # get the original value
        p[0] *= -1
 
        # check if the element is part of
        # the goal list
        if (p[1] in goal):
            # get the position
            index = goal.index(p[1])
 
            # if a new goal is reached
            if (answer[index] == 10**8):
                count += 1
 
            # if the cost is less
            if (answer[index] > p[0]):
                answer[index] = p[0]
 
            if (count == len(goal)):
                return (answer,Backtrace(parent, start, goal[np.argmin(answer)]))
            # pop the element
            del queue[-1]
            queue = sorted(queue)
        # check for the non visited nodes
        # which are adjacent to present node
        for i in range(len(graph[p[1]])):
            if graph[p[1]][i][0] not in visited:
                visited.append(graph[p[1]][i][0])
                queue.append( [(p[0] + graph[p[1]][i][1])* -1 , graph[p[1]][i][0]])
                parent[graph[p[1]][i][0]] = p[1]
    return (answer,Backtrace(parent, start, goal[np.argmin(answer)]))
print(Search(EthioMapWeighted, 'Addis Ababa', ['Lalibela']))
print(Search(EthioMapWeighted, 'Addis Ababa', ['Axum','Gondar','Lalibela','Babile','Jimma','Bale','Sof Oumer','Arba Minch']))


# In[ ]:




