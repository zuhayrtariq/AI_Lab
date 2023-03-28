# Australian Map Problem
# Variables: ['WA', 'NT', 'Q', 'NSW', 'V', 'SA', 'T']
# Domain: ['red', 'green', 'blue']
# Constraints : No two neighbours should have same color

# Importing a python constraint module
import constraint

#Declaring a variable (object) of class problem  
problem = constraint.Problem()

# Define the variables
variables = ['WA', 'NT', 'Q', 'NSW', 'V', 'SA', 'T']

#Defining the domain
domain = ['red', 'green', 'blue']


# Add the variables to the problem
problem.addVariables(variables, domain)

# Add the constraints
#Use lamba to define 
problem.addConstraint(lambda a, b: a != b, ('WA', 'NT'))
problem.addConstraint(lambda a, b: a != b, ('WA', 'SA'))
problem.addConstraint(lambda a, b: a != b, ('NT', 'SA'))
problem.addConstraint(lambda a, b: a != b, ('NT', 'Q'))
problem.addConstraint(lambda a, b: a != b, ('SA', 'Q'))
problem.addConstraint(lambda a, b: a != b, ('SA', 'NSW'))
problem.addConstraint(lambda a, b: a != b, ('SA', 'V'))
problem.addConstraint(lambda a, b: a != b, ('NSW', 'Q'))
problem.addConstraint(lambda a, b: a != b, ('NSW', 'V'))
problem.addConstraint(lambda a: a == 'red', ('WA',))

# Solve the problem
solution = problem.getSolution()

# Print the solution
print(solution)
