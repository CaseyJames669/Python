wordList=["an","an","an","a","a","the","as","apple","and","day"]
results=[]
def countGrades(wordList,articles):
    results.append(wordList.count("a"))
    results.append(wordList.count("an"))
    results.append(wordList.count("the"))
countGrades(wordList,results)
print(results)
    
