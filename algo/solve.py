import bisect

def solve(wordList,target) :
    wordList.sort()
    for i in wordList :
        tmp = target[len(i):]
        if wordList[bisect.bisect_left(wordList,tmp)] == tmp :
            return (i,tmp)

wordList = input("wordList :").split()
target = input("target :")
print(solve(wordList, target))