# TWO + TWO = FOUR
# Example : {T = 2}, {W = 0}, {O = 0} , {F = 4}, {U = 0}, {R = 0} 
# Variables: [T,W,O,U] 
# Domain: [ {T: (1-9)},{F: (1-9)} {O: 0-9}, {U: 0-9}, {W: 0-9} ]
# Constraints : TWO + TWO === FOUR

# Importing a python constraint module
import constraint

#Declaring a variable (object) of class problem  
problem = constraint.Problem()

# We're using .addVariables() this time since we're adding
problem.addVariables("TF", range(1, 10))
problem.addVariables("WOUR", range(10))

# Telling Python that we need TWO + TWO = FOUR
def sum_constraint(t, w, o, f, u, r):
    if 2*(t*100 + w*10 + o) == f*1000 + o*100 + u*10 + r:
        return True

# Adding our custom constraint. The
# order of variables is important!
problem.addConstraint(sum_constraint, "TWOFUR")

# All the characters must represent different digits,
# there's a built-in constraint for that
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