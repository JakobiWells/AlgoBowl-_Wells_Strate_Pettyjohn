





def two_cycle_input(size):
    #this function will return a list storing the inputs for the graph, in this case, the graph is a bunch of 2 class cycles, 
    #where each class is a prerequisite for each other, in theory, the optimal solution will remove exactly have of the number of class
    #as of right now, neither of our heuristics would have any advantage over this type of input and may take an incredibly long time to find a solution.
    string_list = []
    string_list.append(str(size))
    for i in range(1,size+1):
        
        if(i % 2 == 0):
            stringInput = "1 " + str(i-1)
        else:
            stringInput = "1 " + str(i+1)

        string_list.append(stringInput)
        
    return string_list



def create_inputFile(string_list,output_file):
    with open(output_file, 'w') as file:
        # Iterate over the string list
        for string in string_list:
            # Write each string followed by a newline character to the file
            file.write(string + '\n')




if __name__ == "__main__":
    
    maxN = 10000
    maxE = 100000

    string_list = two_cycle_input(10000)
    output_file = "twoCycleInput"

    create_inputFile(string_list,output_file)



    #need algorithm to generate tough input.
    
