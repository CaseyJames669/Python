## Casey Bladow
## 11/30/12

#2
s = "123456789"
print(s[1:5])

#3
first = "casey".title()
last = "james".title()
fullName = last + ", " + first
print(fullName)

#5
secondword = "Broccoli is delicious.".split()[1]
print(secondword)

#BONUS
def myVowels(s):
    vowels = "aeiouAEIOU"
    smyVowels = ""
    for eachChar in s:
        if eachChar in vowels:
            smyVowels = smyVowels + eachChar
    return smyVowels
sentence = "sentence"
print(myVowels(sentence))

#BONUS-SET
vowels = "aeiouAEIOU"
x = set()
sentence = "whatever"
for eachchar in sentence:
    if eachchar in vowels:
        x.add(eachchar)
print(x)
