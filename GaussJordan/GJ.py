import copy

def checkColumn(column, matrix): 
    for row in matrix:
        if row[column] != 0:
            return True
    return False

def swapRows(r,s,matrix):
    tempArr = matrix[r].copy()
    matrix[r] = matrix[s].copy()
    matrix[s] = tempArr

    return matrix

def multConstant(row, alpha, matrix):
    matrix[row] = list(map(lambda element : element*alpha, matrix[row]))
    return matrix

def addTimesRow(r, s, alpha, matrix):
    matrix[s] = list(map()) 

def prettyPrint(matrix):
    for row in matrix:
        print(f'{row[0]:>6}{row[1]:>6}{row[2]:>6}{row[3]:>6}')


matrix = [[8, 2, 3, 1],[1, 3, 2, 1], [3, 2, 1, 1]]
numRows = len(matrix)
numColumns = len(matrix[0])
prettyPrint(matrix)
startColumn = 0

targetEntry = {}

# find first non-zero column
for i in range(0, numColumns-1):
    if checkColumn(i, matrix):
        startColumn = i
        print("Start column is: " + str(startColumn))
        break

# Put into RREF

# find non-zero entry
for j in range(0, numRows):
    row = matrix[j]

    if row[i] != 0:
        targetEntry = {
            "value": row[i],
            "row": j,
            "column": i
        }
        break

print(targetEntry)
# For the rth row, with r != 1, swap rows 1 and r such that there is a non-zero entry at the top of the first non-zero column.
if targetEntry["row"] != 0:
    matrix = swapRows(0, targetEntry["row"], matrix)

multConstant(0,1/targetEntry["value"],matrix)

# Clear every other entry.

for i in (range(0, numRows) - targetEntry["row"]):
    # stuff...
    print(".")

prettyPrint(matrix)