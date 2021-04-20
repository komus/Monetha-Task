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

print(centuryFromYear(2005))


def checkPalindrome(inputString):
    flat_list = list(itertools.chain(*inputString))
    flat_reverse = flat_list[::-1]
    if flat_list == flat_reverse:
        return True
    else:
        return False



