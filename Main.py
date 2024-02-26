#Authors: Jakobi Wells, Jackson Wray, Evan Shiveley
import networkx as nx
import sys
#from networkx.drawing.nx_agraph import to_agraph
#import matplotlib.pyplot as plt



#read in file inputs and return directed graph
def read_input(file_path):
    with open(file_path, 'r') as file:
        
        # Read the number of courses required to graduate
        classNum = int(file.readline().strip())

        G = nx.DiGraph()
        
        #make every node in graph
        for i in range(1, classNum + 1 ):
            G.add_node(int(i))
        
        for i in range(1, classNum + 1 ):
            line = file.readline().split(" ")
            for j in range(1, int(line[0])+1):
                G.add_edge(int(line[j]), i) #add an edge from each prereq class on line i to the class i
                
            
    return G , classNum

#ideally this function will draw the networkx graph using graphviz, networkx, and matlib
"""
def draw_graph(Graph):
    agraph = to_agraph(Graph)
    agraph.draw('graph.png', prog='dot')

    # Display the image
    img = plt.imread('graph.png')
    plt.imshow(img)
    plt.axis('off')
    plt.show()
"""

# returning boolean of if graph has a cycle
def Cycles(Graph):

    try:
        nx.find_cycle(Graph, orientation="original")
        return True

    except nx.exception.NetworkXNoCycle:
        return False
        
# returning number of nodes and which nodes to remove based on frequency in cycles
def RemoveCycles(Graph, classNum):
    G = Graph.copy()
    removeNum = 0
    removeList = []
    
    while Cycles(G) == True: #while cycles exist ...
        frequency = [0] * (classNum+1)
        cycList = list(nx.simple_cycles(G))
        for cycle in cycList:
            for node in cycle:
                frequency[int(node)] = frequency[int(node)] + 1
        mostFrequent = frequency.index(max(frequency))
        removeNum = removeNum + 1
        removeList.append(mostFrequent)
        G.remove_node(mostFrequent)

    return removeNum, removeList

# 
def CheckOutDegree(Graph):
    nodesList = list(Graph.nodes())
    highestOut = 0
    highestNode = nodesList[0]

    for node in Graph.nodes(): #iterates through every node in Graphs
        nodeDegree = Graph.out_degree(node) #finds out degree of each node
        #updates node with highest out degree 
        if nodeDegree > highestOut: 
            highestOut = nodeDegree
            highestNode = node
        
        
    return highestNode


def RemoveOutDegree(Graph):
    G = Graph.copy()
    removeNum = 0
    removeList = []
    count = 0
    while Cycles(G) == True:
        #print(count)
        count +=1
        node = CheckOutDegree(G)
        G.remove_node(node)
        removeNum = removeNum +1
        removeList.append(node)
    return removeNum, removeList




    
    
# beginning of main, currently set to check for input passed with program call
if __name__ == "__main__":
    if len(sys.argv) != 2:
        #print("Usage: python script.py input_file_path")
        sys.exit(1)

    file_path = sys.argv[1]

    Graph, classNum = read_input(file_path)

    cycleNum, cycleList = RemoveCycles(Graph, classNum)
    outNum, outList = RemoveOutDegree(Graph)
    
    if cycleNum < outNum:
        print(cycleNum)
        for i in range(len(cycleList)):
            print(f'{cycleList[i]}', end = ' ')
            
    else:
        print(outNum)
        for i in range(len(outList)):
            print(f'{outList[i]}', end = ' ')
        







   
