# Maximum value in nested lists

largestOfFourList = [[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]

comparison = 0
maxlist = []

for list in largestOfFourList:
    for number in list:
        if number > comparison:
            comparison = number
        else:
            pass
    maxlist.append(comparison)
       
print maxlist