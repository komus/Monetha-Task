"""
    Monetha Basic Task
    Author: Komolafe Oyindolapo
"""

data = [['A1', 28], ['A2', 32], ['A3', 1], ['A4', 0],['A5', 10], ['A6', 22], ['A7', 30], ['A8', 19],
['B1', 145], ['B2', 27], ['B3', 36], ['B4', 25],['B5', 9], ['B6', 38], ['B7', 21], ['B8', 12],['C1', 122],
['C2', 87], ['C3', 36], ['C4', 3],['D1', 0], ['D2', 5], ['D3', 55], ['D4', 62],['D5', 98], ['D6', 32]]

##How many sites are there?
print(f"There are {len(data)} number of sites in the list")

##How many birds were counted at the 7th site?
print(f"The number of birds counted at the 7th site is  {data[6][1]}")

##How many birds were counted at the last site?
print(f"There are birds {data[-1][1]} birds counted at the last site {data[-1][0]}")

##What is the total number of birds counted across all sites?
total = 0
for i in range(len(data)):
    total += data[i][1]

print(f"The total number of birds counted across all sites is {total}")


##What is the average number of birds seen on a site?
print(f"The average number of birds is {total/len(data) :.0f}")

##What is the total number of birds counted on sites with codes beginning with C? (don’t just identify this sites by eye, in the real world there could be hundreds or thousands of sites)
hasC = []
totalC = 0
for i in range(len(data)):
    if data[i][0].startswith('C'):
        hasC.append(data[i][0])
        totalC += data[i][1]

print(f"The sites which begin with C are: {hasC}, with a total number of {totalC} birds ")
