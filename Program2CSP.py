# Find all (a,b,c,d) where a,b ∈ {1,2,3} and c,d ∈ {1,2,3,4}, and a !== b !== c !== d
 
# Variables: [a,b,c,d] 
# Domain: [ {a: 1,2,3}, {b: 1,2,3}, {c: 1,2,3,4}, {d: 1,2,3,4} ]
# Constraints : a !== b !== c !== d
# Importing a python constraint module
import constraint

#Declaring a variable (object) of class problem  
problem = constraint.Problem()


problem.addVariables(["a", "b"], [1, 2, 3]) #Defining the variables (a and b) and its domain = [1,2,3]
problem.addVariables(["c", "d"], [1, 2, 3, 4])#Defining the variables (c and d) and its domain = [1,2,3,4]

#Adding a built in constraints that makes sure that all the variables have different valuess
problem.addConstraint(constraint.AllDifferentConstraint())

#Getting all the solutions to the problem defined above
solutions = problem.getSolutions()
#Storing the total number of solutions found in variable i.e length
length = len(solutions)

#Displaying the total number of solution
print("Total Solutions found : ",length)
print("Solutions that satisfy the constraints are:")

#Iteraitng over solutions
for solution in solutions:
   #Displaying the solutions one by one
   print(solution)
