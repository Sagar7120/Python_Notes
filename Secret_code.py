sampinput = str(input("Enter the message:- "))
spinput = sampinput.split(" ")
condition = int(input("Enter the condition ( 1 for Coding )/(2 for Decoding):- "))

if (condition == 1):
    nword = []
    for word in spinput:
        if (len(word)>= 3):
            r1 = "uha"
            r2 = "hsi"
            raninp = r1 + word[1:] + word[0] + r2
            nword.append(raninp)
            #print(nword)  
        else:
            nword[::-1]
    print (" ".join(nword))

else:
    if (condition == 2):
        nword = []
        for word in spinput:
            if (len(word)>=3):
                new = word[3:-3]
                snew = new [-1]+ new [:-1]
                print(snew,end=(' '))
            else:
                nword[::-1]
    print (" ".join(nword))

# hey vedant

#ghteyhhjk ghyedantvhjk

#hey  eyh