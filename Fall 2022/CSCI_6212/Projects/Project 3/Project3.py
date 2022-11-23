# A Dynamic Programming based Python Program for the Egg Dropping Puzzle

# Import libraries for capturing time and math functions
import math
import time
import matplotlib.pyplot as plt
import functools
import sys

# Initialize list to capture results for theoretical, experimental results and values of n
theoreticalTimeList = []
experimentalTimeList = []
nValuesList = []

# Function to get minimum number of trials needed in worst
# case with n eggs and k floors
def eggDrop(m, n):

	# A 2D table where entry eggFloor[i][j] will represent minimum
	# number of trials needed for i eggs and j floors.
    eggFloor = [[0]*(n+1) for i in range(m+1)]
    first_floor_value = sys.maxsize
    first_floor = sys.maxsize

	# We need one trial for one floor and0 trials for 0 floors
    for i in range(1, m + 1):
        eggFloor[i][1] = 1
        eggFloor[i][0] = 0

	# We always need j trials for one egg and j floors.
    for j in range(1, n + 1):
        eggFloor[1][j] = j

	# Fill rest of the entries in table using optimal substructure
	# property
    for i in range(2, m + 1):
        for j in range(2, n + 1):
            eggFloor[i][j] = sys.maxsize
            res = sys.maxsize

            for x in range(1, j + 1):
                res = min( res, 1 + max(eggFloor[i-1][x-1], eggFloor[i][j-x]))
            
            eggFloor[i][j] = res

            if i==n and res != first_floor_value :
                first_floor = j
                first_floor_value = res

            

	# eggFloor[n][k] holds the result
    return eggFloor[m][n]

def calculateTime(eggs, floors, var):

    # Capture the time, when the function's execution has begun
    startTime = time.time()

    # The algorithm to find staircase
    eggDrop(eggs, floors)


    # Capture the time, when the function's execution has ended
    endTime = time.time()

    # Calculate the time taken to execute the code snippet
    timeTaken = endTime-startTime

    # Append the values of n, experimental results and theoretical results in their corresponding lists

    nValuesList.append(var)
    experimentalTimeList.append(timeTaken)
    theoreticalTimeList.append((var)*math.log2(var)) # Theoretical results derived

# Having number of floors constant
floors = 1000
eggs = [2,4,6,8,10]

for num_of_egg in eggs:
    calculateTime(num_of_egg,floors, num_of_egg)

# Function to calculate mean of the results which will be used for normalization
def Average(lst):
    return functools.reduce(lambda val1, val2: val1 + val2, lst) / len(lst)

# Deriving scaling/normalizing constant by mean of theoretical results by experimental results
normalizingConstant = Average(theoreticalTimeList)/Average(experimentalTimeList)


print("\n\n-------------------------------------------------------------------------------------------------")
print("-------------------------------For variable eggs and fixed floors--------------------------------")
print("-------------------------------------------------------------------------------------------------\n\n")

print("\nThe number of floors is {}\n".format(floors))

print("\nThe normalizing Constant fixed number of floors is = {}".format(normalizingConstant))

# Creating a lnew ist of experimental results by scaling the existing with normalizing constant
adjustedexperimentalTimeList = [i * normalizingConstant for i in experimentalTimeList]

# Logs of values of n, Time taken Programatically and Theoretically which is derived in the project submission
for i,n in enumerate(eggs):
    print("\nFor number of eggs = {}".format(n))
    print("Theoretically Time taken = {}".format(theoreticalTimeList[i]))  # Theoretical results derived
    print("Programatically Time taken = {}".format(experimentalTimeList[i]))
    print("Adjusted Programatically Time taken = {}".format(adjustedexperimentalTimeList[i]))



floors = [10, 100, 500, 1000, 5000]
eggs = 2

for num_of_floor in floors:
    calculateTime(eggs,num_of_floor, num_of_floor)

# Deriving scaling/normalizing constant by mean of theoretical results by experimental results
normalizingConstant = Average(theoreticalTimeList)/Average(experimentalTimeList)

print("\n\n-------------------------------------------------------------------------------------------------")
print("-------------------------------For variable floors and fixed eggs--------------------------------")
print("-------------------------------------------------------------------------------------------------\n\n")

print("\nThe number of eggs is {}\n".format(eggs))

print("\nThe normalizing Constant for fixed number of eggs is = {}".format(normalizingConstant))

# Creating a lnew ist of experimental results by scaling the existing with normalizing constant
adjustedexperimentalTimeList = [i * normalizingConstant for i in experimentalTimeList]


# Logs of values of n, Time taken Programatically and Theoretically which is derived in the project submission
for i,n in enumerate(floors):
    print("\nFor number of floors = {}".format(n))
    print("Theoretically Time taken = {}".format(theoreticalTimeList[i]))  # Theoretical results derived
    print("Programatically Time taken = {}".format(experimentalTimeList[i]))
    print("Adjusted Programatically Time taken = {}".format(adjustedexperimentalTimeList[i]))