def solve(wordList, target) :
    for i in range(len(wordList)) :
        for j in range(i+1,len(wordList)) : 
            if wordList[i]+wordList[j] == target :
                return (wordList[i],wordList[j])
    return

wordList = input("wordList :").split()
target = input("target :")
print(solve(wordList, target))


