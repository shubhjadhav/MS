#---------------------------------------------------------------------
# Implemention of Stack in Julia
# Advance Software Paradigms - Mid Terms Fall 2022
# Shubham Jadhav
#---------------------------------------------------------------------

# Creating a data structure to replicate stack behaviour
mutable struct JuliaStack
    maxsize::Int
    top::Int
    stack::AbstractArray
end

# This function implements the push method for adding element to the stack
function push(stackVar, pushValue, inititalization=nothing)

    # A flag to ignore any unecessary prints wile inititalizing a stack
    if inititalization === nothing
        println("\nThe stack is in process of adding an element.....")
    end

    # Check if the stack is full to its defined max value
    if stackVar.top == stackVar.maxsize-1
        println("Sorry, the stack is full!\n")
    else
        push!(stackVar.stack, pushValue) # add the value to the stack
        stackVar.top += 1                # Increment the top counter
        if inititalization === nothing
            println("", pushValue, " is added to the stack")
            println("The updated stack is: ", stackVar.stack)
        end
    end
end

# This function checks if the stack is empty or not
function checkEmpty(stackVar)
    return stackVar.top == -1  
end

# This function implements the pop method for removing element to the stack
function pop(stackVar)

    println("\nThe stack is in process of removing an element.....")

    if checkEmpty(stackVar)
        println("Sorry, the stack is empty!\n")
    else
        popedValue = pop!(stackVar.stack) # remove the value from the stack
        stackVar.top = stackVar.top - 1   # Decrement the top counter
        println("", popedValue, " is removed from the stack")
        println("The updated stack is: ", stackVar.stack)
    end
end

# This function implements the top method for retrieving last entered element to the stack
function top(stackVar)

    println("\nThe stack is in process of retrieving the top element.....")

    if checkEmpty(stackVar)
        println("Sorry, the stack is empty!\n")
    else
        println("The top value from stack is ", stackVar.stack[length(stackVar.stack)],"\n")
    end
end

# This function implements the top method for retrieving last entered element to the stack
function empty(stackVar)

    println("\nThe stack is in process of checking if there are any elements in it.....")

    if checkEmpty(stackVar)
        println("Sorry, the stack is empty!\n")
    else
        println("The stack is not empty\n")
    end
end

#---------------------------------------------------------------------
# Implementing Stack of Integers
#---------------------------------------------------------------------

integerStack = JuliaStack(100, -1, [])

# Create a stack of 10 integer values
for i in 1:10
    push(integerStack,rand(1:100),1)
end

println("The integer stack is: ", integerStack.stack, "\n")

# Some operations to test the stack
empty(integerStack)
pop(integerStack)
pop(integerStack)
push(integerStack, 23)
top(integerStack)


#---------------------------------------------------------------------
# Implementing Stack of Strings
#---------------------------------------------------------------------

stringStack = JuliaStack(100, -1, [])

# Create a stack of string values
for i in split("Even in hard times there's a possibility to have fun"," ")
    push(stringStack,i,1)
end

println("The string stack is: ", stringStack.stack, "\n")

# Some operations to test the stack
empty(stringStack)
pop(stringStack)
push(stringStack, "amazing")
push(stringStack, "life")
top(stringStack)


#---------------------------------------------------------------------
# Testing exceptional cases
#---------------------------------------------------------------------

testStack = JuliaStack(100, -1, [])

for i in 1:1
    push(testStack,rand(1:100),1)
end

println("The testing stack is: ", testStack.stack, "\n")

# Trying to pop an element from empty stack 
pop(testStack)
pop(testStack)
empty(testStack)

# Trying to get top an empty stack 
top(testStack)

# Trying to push an element to full stack
for i in 1:100
    push(testStack,rand(1:100),1)
end

push(testStack, 1000)