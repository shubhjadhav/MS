# Import libraries for capturing time and math functions
import math
import time
import matplotlib.pyplot as plt
import functools

# Initialize list to capture results for theoretical, experimental results and values of n
theoreticalTimeList = []
experimentalTimeList = []
nValuesList = []

# Function to calculate Time taken to execute for given value of n
def calculateTime(n):

    # Capture the time, when the function's execution has begun
    startTime = time.time()

    # The code snipped from the project question
    j = 2
    while (j < n):
        k=2
        while (k < n):
            # Sum += a[i]*b[j]*c[k]  - ignoring the equation as the it can be considered as a constant
            k = k * math.sqrt(k)
        j += j/2

    # Capture the time, when the function's execution has ended
    endTime = time.time()

    # Calculate the time taken to execute the code snippet
    timeTaken = endTime-startTime

    # Logs of values of n, Time taken Programatically and Theoretically which is derived in the project submission
    print("\nFor n={}".format(n))
    print("Programatically Time taken = {}".format(timeTaken))
    print("Theoretically Time taken = {}\n".format(math.log10(n)*math.log10(math.log10(n))))  # Theoretical results derived

    # Append the values of n, experimental results and theoretical results in their corresponding lists
    nValuesList.append(n)
    experimentalTimeList.append(timeTaken)
    theoreticalTimeList.append(math.log10(n)*math.log10(math.log10(n))) # Theoretical results derived

# Function calls for each value on n
calculateTime(10)
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

# Creating a lnew ist of experimental results by scaling the existing with normalizing constant
adjustedexperimentalTimeList = [i * normalizingConstant for i in experimentalTimeList]

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