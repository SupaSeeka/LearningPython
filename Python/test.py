n = 1000
compareNumbers = range(2, n+1)
nums = range(2, n + 1)
numSet = set(nums)
primesArray = []
isPrime = True

for i in numSet:
    isPrime = True
    # compare to each number from 2 through 25

    for j in compareNumbers:
        if (i % j == 0):
            if (i != j):
                isPrime = False

    if isPrime:
        primesArray.append(i)

    removeNumbers = set(range(i, n+1, i))
    numSet = numSet - removeNumbers
    

print (primesArray)

