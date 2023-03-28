# pip install python-constraint
# Find all (x,y) where x ∈ {1,2,3} and 0 <= y < 5, and x + y >= 5
 
# Variables: [x,y] 
# Domain: [{x: 1,2,3}, {y: range(0,5)}]
# Constraints : x + y >= 5
# Importing a python constraint module
import constraint

problem = constraint.Problem()

problem.addVariable('x', [1,2,3]) #Defining the variable and its domain x = [1,2,3]
problem.addVariable('y', range(5)) #Defining the variable and its domain y = [0,1,2,3,4]

#Defining the constraint and checking if the constraint is satisfied 
def our_constraint(x, y):
    if x + y >= 5:
        return True

problem.addConstraint(our_constraint, ['x','y']) #Adding the constraint into our problem

solutions = problem.getSolutions() #Storing the values that satisfy the constaint in variable i.e solutions

#Storing the total number of solutions found in variable i.e length
length = len(solutions)

#Displaying the total number of solution
print("Total Solutions found : ",length)
print("Solutions that satisfy the constraints are:")

#Iteraitng over solutions
for solution in solutions:
   #Displaying the solutions one by one
   print(solution)
