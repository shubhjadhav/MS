# Import libraries for capturing time and math functions
import math
import time
import matplotlib.pyplot as plt
import functools

# Initialize list to capture results for theoretical, experimental results and values of n
theoreticalTimeList = []
experimentalTimeList = []
nValuesList = []

def pareto(n):

    if n<=1:
        return

    for i in range(n):
        None

    for i in range(n):
        None

    pareto(math.ceil(n/2))
    pareto(math.ceil(n/2))

# Function to calculate Time taken to execute for given value of n
def calculateTime(n):

    # Capture the time, when the function's execution has begun
    startTime = time.time()

    # The algorithm to find staircase
    pareto(n)


    # Capture the time, when the function's execution has ended
    endTime = time.time()

    # Calculate the time taken to execute the code snippet
    timeTaken = endTime-startTime

    # Append the values of n, experimental results and theoretical results in their corresponding lists
    nValuesList.append(n)
    experimentalTimeList.append(timeTaken)
    theoreticalTimeList.append((n)*math.log2(n)) # Theoretical results derived

# Function calls for each value on n
calculateTime(100)
calculateTime(1000)
calculateTime(10000)
calculateTime(100000)
calculateTime(1000000)

# Function to calculate mean of the results which will be used for normalization
def Average(lst):
    return functools.reduce(lambda val1, val2: val1 + val2, lst) / len(lst)

# Deriving scaling/normalizing constant by mean of theoretical results by experimental results
normalizingConstant = Average(theoreticalTimeList)/Average(experimentalTimeList)

print("\nThe normalizing Constant is ={}".format(normalizingConstant))

# Creating a lnew ist of experimental results by scaling the existing with normalizing constant
adjustedexperimentalTimeList = [i * normalizingConstant for i in experimentalTimeList]

 # Logs of values of n, Time taken Programatically and Theoretically which is derived in the project submission
for i,n in enumerate([100,1000,10000,100000,1000000]):
    print("\nFor n={}".format(n))
    print("Theoretically Time taken = {}".format(theoreticalTimeList[i]))  # Theoretical results derived
    print("Programatically Time taken = {}".format(experimentalTimeList[i]))
    print("Adjusted Programatically Time taken = {}".format(adjustedexperimentalTimeList[i]))

# Plot a line chart to vizualize and compare results from Experimental and Theoretical analysis

# Plot the first line graph for Theoretical results against n values
plt.plot(nValuesList, theoreticalTimeList, label = "Theoretical Time")

# Plot the second line graph for Experimental results against n values
plt.plot(nValuesList, adjustedexperimentalTimeList, label = "Experimental Time")

# Assigning title to the chart
plt.title('Experimental vs Theoretical Time Values')

# Adding grid for easy mappings
plt.grid()

# Displaying legends for each line for accurate insights
plt.legend()

# Presenting the line chart
plt.show()