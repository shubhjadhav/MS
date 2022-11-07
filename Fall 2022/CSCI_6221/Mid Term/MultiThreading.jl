#---------------------------------------------------------------------
# Implemention of Concurrent Programming in Julia
# Advance Software Paradigms - Mid Terms Fall 2022
# Shubham Jadhav
#---------------------------------------------------------------------

# Note: By default, Julia starts up with a single thread of execution. 
# The number of threads can either be specified as an integer (--threads=4) 
# or as auto (--threads=auto), where auto sets the number of threads to the 
# number of local CPU threads
#
# When starting Julia in terminal enter the following command
# julia --threads [number of threads] ;in this case it will be 1000
# julia --threads 1000
#
# Some systems cannot run Julia with 1000 threads, and when you try to run the command with 1000
# It will return nothings. For many systems, 250 is the max threads that can be created
#
# you can test the implementation with fewers threads, but it wont return 1000 values
# as the code (at line 42) is dynamically coded to run nthreads times
# if you want to run the code to get 1000 prints with 4 threads
# update the code at line 42 from nthreads() to 1000 and start julia as following
# julia --threads 4

# Importing the modules
using Base.Threads

# Create a channel for data sharing
const counter = Channel{Int}(32);

# Initialize the value to 0
put!(counter, 0)

# Create a function to increment the value by 1
function increment()
    sleep(0.5)
    value = take!(counter) # retrieve the value from shared variable
    value += 1

    #Uncomment the below line to check which Threads are working on what task
    # println("Thread ",Threads.threadid()," incremented the value to ",value)

    print(value, " ")
    put!(counter, value) # insert the value to the shared variable
end

# Create tasks
concurrentTasks = [Task(increment) for i=1:nthreads()]

# Schedule the tasks
@threads for task in concurrentTasks
    schedule(task)
end