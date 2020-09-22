
# --------------------------------------------------------
#           PYTHON PROGRAM
# Here is where we are going to define our set of...
# - Imports
# - Global Variables
# - Functions
# ...to achieve the functionality required.
# When executing > python 'this_file'.py in a terminal,
# the Python interpreter will load our program,
# but it will execute nothing yet.
# --------------------------------------------------------
import numpy as np
# ------------------------------------------
# FUNCTION parse_in
# ------------------------------------------
def parse_in(input_name):
    myfile = open(input_name, "r")
    fl = myfile.readline()
    rows, columns = fl.split(' ')
    num_rows = int(rows)
    num_columns = int(columns)
    mat1 = []
    for line in myfile:
        mat1.append(line.split('\n')[:-1])
    # print(mat1)
    matrix = []
    for i in range(num_rows):
        matrix.append(mat1[i][0].split(' '))
    return matrix, num_rows, num_columns
    pass

# ------------------------------------------
# FUNCTION solve
# ------------------------------------------

def solve(my_data):
    num_rows = my_data[1]
    num_columns = my_data[2]
    array_2D = np.array(my_data[0])
    # print(array_2D)
    # print(type(array_2D))
    for r in range(num_rows):
        for c in range(num_columns):
            if(array_2D[r][c]!='x'):
                count=0
                for rr in range(r-1, r+2):
                    if(rr>=0 and rr<num_rows):
                        for cc in range(c-1, c+2):
                            if(cc>=0 and cc<num_columns and array_2D[rr][cc]=='x'):
                                count+=1
                array_2D[r][c]=str(count)
    # print(array_2D)
    return array_2D
    pass

# ------------------------------------------
# FUNCTION parse_out
# ------------------------------------------
def parse_out(output_name, my_solution):
    print(my_solution)
    np.savetxt(output_name, my_solution, fmt="%s")
    pass


# ------------------------------------------
# FUNCTION my_main
# ------------------------------------------
def my_main(input_name, output_name):
    # 1. We do the parseIn from the input file
    my_data = parse_in(input_name)

    # 2. We do the strategy to solve the problem
    my_solution = solve(my_data)

    # 3. We do the parse out to the output file
    parse_out(output_name, my_solution)


# ---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
# ---------------------------------------------------------------
if __name__ == '__main__':
    # 1. Name of input and output files
    input_name = "input_1.txt"
    output_name = "output_1.txt"
    # input_name = "input_2.txt"
    # output_name = "output_2.txt"

    # 2. Main function
    my_main(input_name, output_name)
