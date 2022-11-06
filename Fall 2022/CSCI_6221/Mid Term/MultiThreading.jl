using Base.Threads

const counter = Channel{Int}(32);
put!(counter, 0)

function increment()
    sleep(0.5)
    value = take!(counter)
    value += 1
    # println("Thread ",Threads.threadid()," incremented the value to ",value)
    print(value, " ")
    put!(counter, value)
end

concurrentTasks = [Task(increment) for i=1:nthreads()]

@threads for task in concurrentTasks
    schedule(task)
end