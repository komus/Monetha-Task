import itertools
def alternatingSort(a):
    half = len(a)//2
    a_1 = a[:half]
    a_2 = a[half:]
    newarray = []
    for i in range(half):
        newarray.append(a_1[0])
        newarray.append(a_2[-1])
        a_1.remove(a_1[0])
        a_2.remove(a_2[-1])
    v = [newarray[i+1]-newarray[i] for i in range(len(newarray)-1)]
    y = list(itertools.dropwhile(lambda x : x == 1, v ))
    
    if len(y) == 0:
        return True
    else:
        return False

#alternatingSort([1, 3, 5, 6, 4, 2])


def centuryFromYear(year):
    cent = year//100
    print(cent)
    ext = year %  100
    print(ext)
    
    if ext > 1:
        cent += 1
    return cent




def checkPalindrome(inputString):
    flat_list = list(itertools.chain(*inputString))
    flat_reverse = flat_list[::-1]
    if flat_list == flat_reverse:
        return True
    else:
        return False

def adjacentElementsProduct(inputArray):
    v = [inputArray[i+1] * inputArray[i] for i in range(len(inputArray)-1)]       
    return max(v)  


def shapeArea(n):
    if n == 1:
        return 1
    else:
        return (n*n) + ((n-1)*(n-1))

def makeArrayConsecutive2(statues):
    f = list(range(min(statues), max(statues), 1) )
    main_list = list(set(f) - set(statues))
    return len(main_list)



#print(makeArrayConsecutive2([6, 2, 3, 8]))
def almostIncreasingSequence(sequence):
    s = [sequence[i+1] - sequence[i] for i in range(len(sequence)-1)]

    
    if len(s) == 1:
        return True
    else:
        val = sum(map(lambda x : x != 1, s))
        ff = sum(s)
        print(s)
        print(ff)
        if val == 1:
            return True
        else:
            return False

print(almostIncreasingSequence([1, 2, 3, 4, 5, 3, 5, 6]))

