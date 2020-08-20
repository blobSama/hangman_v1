wrdLst = []
currWord = ""
for i in range(0, 3):
    ans = input("Enter a word:")
    wrdLst.append(ans)
ans = wrdLst[2]
wrongGuesses = 0
while((wrongGuesses < len(ans)*2) and ans != ""):
    currGuess = input("guess letters:")
    if(currGuess not in ans):
        print("Wrong")
        wrongGuesses += 1
    else:
        ans = ans.replace(currGuess, "")
print("congrats!")
