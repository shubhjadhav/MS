#---------------------------------------------------------------------
# Implemention of Stack in Julia with Concurrency
# Advance Software Paradigms - Mid Terms Fall 2022
# Shubham Jadhav
# To see cleaner code, please see Stack_Concurrency.jl at my GitHub
# https://github.com/shubhjadhav/MS/tree/main/Fall%202022/CSCI_6221/Mid%20Term
#---------------------------------------------------------------------

# Multithreading in julia needs, Julia to be installed in system as online IDE have
# only 1 threads
#
# To install Julia, go to: https://julialang.org/downloads/
#
# Note: By default, Julia starts up with a single thread of execution. 
# The number of threads can either be specified as an integer (--threads=4) 
# or as auto (--threads=auto), where auto sets the number of threads to the 
# number of local CPU threads
#
# When starting Julia in terminal enter the following command
# julia --threads [number of threads] ;in this case it will be 200
# julia --threads 200
#
# if you want to run the code with 4 threads
# julia --threads 4


# Importing the modules
using Base.Threads
using Random

# Creating a data structure to replicate stack behaviour
mutable struct JuliaStack
    maxsize::Int
    top::Int
    stack::AbstractArray
end

# This function checks if the stack is full or not
function checkFull(stackVar)
    return stackVar.top == stackVar.maxsize
end

# This function implements the push method for adding element to the stack
function push(stackVar, pushValue)
    # Check if the stack is full to its defined max value
    if checkFull(stackVar)
        println("Sorry, the stack is full!\n")
    else
        stackVar.top += 1                        # Increment the top counter
        insert!(stackVar.stack, stackVar.top, pushValue) # add the value to the stack
        println("Stack length -> ", stackVar.top)
    end
end

# This function checks if the stack is empty or not
function checkEmpty(stackVar)
    return stackVar.top == 0
end

# This function implements the pop method for removing element to the stack
function pop(stackVar)
    if checkEmpty(stackVar)
        println("Sorry, the stack is empty!\n")
    else
        deleteat!(stackVar.stack, stackVar.top)
        stackVar.top = stackVar.top - 1   # Decrement the top counter
        println("Stack length -> ", stackVar.top)
    end
end

# This function implements the top method for retrieving last entered element to the stack
function top(stackVar)
    if checkEmpty(stackVar)
        println("Sorry, the stack is empty!\n")
    else
        println("The top value from stack is ", stackVar.stack[length(stackVar.stack)],"\n")
    end
end

# This function implements the top method for retrieving last entered element to the stack
function empty(stackVar)
    if checkEmpty(stackVar)
        println("Sorry, the stack is empty!\n")
    else
        println("The stack is not empty\n")
    end
end


#---------------------------------------------------------------------
# Implementing Stack of Integers
#---------------------------------------------------------------------

integerStack = JuliaStack(100, 0, []);

#---------------------------------------------------------------------
# Create Threads for each pop/push task
#---------------------------------------------------------------------

# Create tasks for push
pushTasks = ["push" for i=1:100]

# Create tasks for pop
popTasks = ["pop" for i=1:100]

# Merging push and pops and shuffling them
tasks = vcat(pushTasks, popTasks)
tasks = shuffle(tasks)

@threads for task in tasks
    if task == "push" 
        if checkFull(integerStack)
            println("-1")
            sleep(1000)
            Task(push(integerStack, rand(1:100)))
        else  
            Task(push(integerStack, rand(1:100)))
        end
    else
        if checkEmpty(integerStack)
            println("-1")
            sleep(1000)
            Task(pop(integerStack))
        else
            Task(pop(integerStack))
        end
    end
end