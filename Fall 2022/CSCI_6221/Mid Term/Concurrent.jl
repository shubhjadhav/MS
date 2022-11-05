const jobs = Channel{Int}(32);
const counter = Channel{Int}(32);
put!(counter, 0)

n = 10;

#make jobs
@sync for j in 1:n
    put!(jobs, j)
end

#execute jobs
function execute()
    for job_id in jobs   
        sleep(rand()+0.5)
        value = take!(counter)
        value += 1
        @async print(value, " ")
        put!(counter, value)
    end
end;

errormonitor(@sync execute())