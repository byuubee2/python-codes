spam = [1,2,3,4,5,6,1,2,3]
numberOfStreaks = 0
def checkPattern(list):
    for i in range(len(list)):
        if list[i] + list[i+1] + list[i+2] == [1,2,3]:
            numberOfStreaks += 1
    print(numberofStreaks)
checkPattern(spam)
