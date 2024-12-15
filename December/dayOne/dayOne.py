#open and read the input
data = open('puzzleinput.txt', 'r').read().split()

#split the lists into the two separate lists
listOne = data[::2]
listTwo = data[1::2]

#find length of listOne
listOneLength = len(listOne)
#find length of listTwo
listTwoLength = len(listTwo)
#each list has 1000 numbers in it

#create an empty list for all small numbers in listOne
listOneSmallNums = []

#this while loop goes through every number in listOne
#if it's the smallest number, add it to the empty list
#and then remove it so it doesnt iterate over it again
i = 0
while i < listOneLength:
    minNumbersInOne = min(listOne)
    listOneSmallNums.append(minNumbersInOne)
    listOne.remove(minNumbersInOne)
    i += 1

#iterate and organize listTwo like we did with listOne
listTwoSmallNums = []
i = 0
while i < listTwoLength:
    minNumbersInTwo = min(listTwo)
    listTwoSmallNums.append(minNumbersInTwo)
    listTwo.remove(minNumbersInTwo)
    i += 1

#get the total list length between the two for iteration
#since there are two lists
totalListLength = listOneLength + listTwoLength

#now that I have the two lists organized, I need to find the distance between the
#numbers in the same spot on different lists

#first, convert the lists of small numbers to a list of ints and not strs
oneSmallInts = [int(x) for x in listOneSmallNums]
twoSmallInts = [int(x) for x in listTwoSmallNums]

#we now have the two lists as ints and they are organizaed

#create a list of the numbers in the same spot subtracted from eachother
#make sure to use abs for no negatives
distanceNumbersNotAddedTogether = []

for i in range(listOneLength):
    distanceNumbersNotAddedTogether.append(abs(oneSmallInts[i] - twoSmallInts[i]))

#add the new list of all the distances together to get your answer
totalDistance = sum(distanceNumbersNotAddedTogether)

#print(totalDistance)

#######################Part Two####################################
#took all the code from part one 

#create an empty list that will be used for adding all the numbers and their count
simNums = []

#iterate through the list length
#get the first number in the first list and save it as firstNum
#set the count variable to count how often firstNum appears in the second list
#get the firstNum and multipy it by the count (how often it appears * the number itself)
#append this to the empty list
#make sure to remove it after appending it to the empty list
#increase the iteration
i = 0
while i < listOneLength:
    firstNum = oneSmallInts[0]
    count = twoSmallInts.count(firstNum)
    simNums.append(count * firstNum)
    oneSmallInts.remove(firstNum)
    i += 1

#this while loop gets the number and how many times it appears
#now we just add the numbers in the list together
similarityScore = sum(simNums)
print(similarityScore)

#Congrats! Day One is now complete!




