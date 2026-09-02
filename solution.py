def pig_it(text):
    words = text.split(" ")
    result = []
    
    for word in words: 
        punctuation = ""
        
        if word and word[-1] in "":
            punctuation = word[-1]
            word = word[:-1]
        
        if word:
            word = word[1:] + word[0] + "ay"
        
        result.append(word + punctuation)
        
    return " ".join(result)

print(pig_it("Pig latin is cool")) # igPay atinlay siay oolcay
print(pig_it("This is my string!"))    # elloHay orldway ! 