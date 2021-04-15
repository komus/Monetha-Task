

def Switch_Symbol(symbol):
    Switch = {
        "#":5,
        "O":3,
        "X":1,
        "!":-1,
        "!!":-3,
        "!!!":-5
        }
    return Switch.get(symbol,0)
#Zero added as a default value in the instance where an invalid data is passed


def check_score(thelist):
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
  ["!!!", "O", "!"],
  ["X", "#", "!!!"],
  ["!!", "X", "O"]
]))