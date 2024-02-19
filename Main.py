#Authors: Jakobi Wells
import networkx as nx
import sys


#code is not finished yet, just getting a template down for what were gonna need to do.


#get n and prereqs from file returns an int and list
def read_input(file_path):
    with open(file_path, 'r') as file:
        # Read the number of courses required to graduate
        n = int(file.readline().strip())

        # Initialize list to store prerequisites
        prerequisites = []

        # Read prerequisites for each course
        for _ in range(n):
            line = file.readline().strip().split()
            mi = int(line[0])
            prerequisites.append(list(map(int, line[1:])))

    return n, prerequisites



    











#creates a Directed Graph using the networkx library, returns the graph
def create_state_graph():
    G = nx.DiGraph()
    
    return G




# beginning of main, currently set to check for input passed with program call
if __name__ == "__main__":
    if len(sys.argv) != 2:
        #print("Usage: python script.py input_file_path")
        sys.exit(1)

file_path = sys.argv[1]





#were going to need to use dfs or the networkx find_cycle function
# find_cycle will probably be the easiest
#psuedo
#find_cycle(G, source = start node, source = orientation = original/directed)
    # if cycle found, graph contains further nodes that need to be removed
    #else throws NetworkXNoCycle

