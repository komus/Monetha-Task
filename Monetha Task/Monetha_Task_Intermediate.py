"""
    Monetha Intermediate Task
    Author: Komolafe Oyindolapo
"""

def Switch_Symbol(symbol):
    """
     A function that returns the numeric value of the passed symbol.
     Zero is returned for unidentified symbol
    """
    Switch = {
        "#":5,
        "O":3,
        "X":1,
        "!":-1,
        "!!":-3,
        "!!!":-5
        }
    return Switch.get(symbol,0)


def check_score(thelist):
    """
        A function that accepts a list and returns the total of the symbols in the list
    """
    totalscore = 0
    #Check whether the parameter is a list
    if type(thelist) == list:
        for i in range(len(thelist)):
            for j in range(len(thelist[i])):
                totalscore +=  Switch_Symbol(thelist[i][j])
        
    else:
        totalscore = "error"

    if totalscore < 0:
        return 0
    else:
        return totalscore



print(check_score([
  ["#", "O", "#", "!!", "X", "!!", "#", "O", "O", "!!", "#", "X", "#", "O"],
  ["!!!", "!!!", "!!", "!!", "!", "!", "X", "!", "!!!", "O", "!", "!!!", "X", "#"],
  ["#", "X", "#", "!!!", "!", "!!", "#", "#", "!!", "X", "!!", "!!!", "X", "O"],
  ["!!", "X", "!!", "!!", "!!!", "#", "O", "O", "!!!", "#", "O", "O", "#", "!!"],
  ["O", "X", "#", "!", "!", "X", "!!!", "O", "!!!", "!!", "O", "!", "O", "X"],
  ["!!", "!!!", "X", "!!!", "!!", "!!", "!!!", "X", "O", "!", "#", "!!", "!!", "!!!"],
  ["!!", "!!", "#", "O", "!", "!!", "!", "!!!", "#", "O", "#", "!", "#", "!!"],
  ["X", "X", "O", "X", "!!!", "#", "!!!", "!!!", "X", "X", "X", "!", "#", "!!"],
  ["O", "!!!", "!", "O", "#", "!", "!", "#", "X", "X", "#", "O", "!!", "!"],
  ["X", "!", "!!", "#", "#", "X", "!!", "O", "!!", "X", "X", "!!", "#", "X"],
  ["!", "!!", "!!", "O", "!!", "!!", "#", "#", "!", "!!!", "O", "!", "#", "#"],
  ["!", "!!!", "!!", "X", "!!", "!!", "#", "!!!", "O", "!!", "!!!", "!", "!", "!"],
  ["!!!", "!!!", "!!", "O", "!", "!", "!!!", "!!!", "!!", "!!", "X", "!", "#", "#"],
  ["O", "O", "#", "O", "#", "!", "!!!", "X", "X", "O", "!", "!!!", "X", "O"]
]))
