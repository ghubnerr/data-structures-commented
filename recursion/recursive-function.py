# A recursive function is a function that calls itself -- until it doesn't

# In order for it to not be an infinite calling, thus overflowing the call stack, we need to have base cases.
# Base cases are conditionals with return statements that are evaluated for every separate recursion of the function.
# Eventually, the base case will break (return) the recursion. Therefore, it must eventually evaluate to true.

# The call stack (stack as in LIFO) keeps track of the function's calling and their respective namespaces.
# Whenever a function is called, that function calling is added to the top of the stack.
# With recursion, if there are no base cases, the stack overflows with function callings, crashing the program.

def factorial(n):
    # Base Case -> 4! = 4 * 3! = 4 * 3 * 2! = 4 * 3 * 2 * 1! -> 1 is the Base Case
    if n == 1: 
        return 1
    
    # Recursive Case 
    return n * factorial(n - 1) # Will get smaller and smaller

# Call stack:
# TOP: factorial(1)
#      factorial(2)
#      factorial(3)
#          ...
#      factorial(n) 