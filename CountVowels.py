   
# Part 2   
# Task 1 - count vowels

word = input(str("elephanteieieio"))
vowels = "aeiou"        
counter = 0

for letters in word:
    if letters.lower() in word:
        counter += 1
        print("The number of vowels in the word: " + str(vowels)) # 81 numbers