# A Dynamic Programming based Python Program for the Egg Dropping Puzzle
import sys

# Function to get minimum number of trials needed in worst
# case with n eggs and k floors
def eggDrop(n, k):
	# A 2D table where entry eggFloor[i][j] will represent minimum
	# number of trials needed for i eggs and j floors.
    eggFloor = [[0]*(k+1) for i in range(n+1)]
    first_floor_value = sys.maxsize
    first_floor = sys.maxsize

	# We need one trial for one floor and0 trials for 0 floors
    for i in range(1, n + 1):
        eggFloor[i][1] = 1
        eggFloor[i][0] = 0

	# We always need j trials for one egg and j floors.
    for j in range(1, k + 1):
        eggFloor[1][j] = j

	# Fill rest of the entries in table using optimal substructure
	# property
    for i in range(2, n + 1):
        for j in range(2, k + 1):
            eggFloor[i][j] = sys.maxsize
            res = sys.maxsize

            for x in range(1, j + 1):
                res = min( res, 1 + max(eggFloor[i-1][x-1], eggFloor[i][j-x]))
            
            eggFloor[i][j] = res

            if i==n and res != first_floor_value :
                first_floor = j
                first_floor_value = res

            

	# eggFloor[n][k] holds the result
    return first_floor, first_floor_value

# Driver program to test to print printDups
n = 1
k = 36
# print(
#     "Minimum number of trials in worst case with " 
#     + str(n) 
#     + " eggs and "
# 	+ str(k) 
#     + " floors is " 
#     + str(eggDrop(n, k))
# )

first_floor, first_floor_value = eggDrop(n, k)

print(first_floor, first_floor_value)

