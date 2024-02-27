sentence = "This is a commom interview question"

charFrequency = {}

for char in sentence:
    if char in charFrequency: # if the character is already in the dictionary then increment the value by 1
        charFrequency[char] += 1
    else:
        charFrequency[char] = 1 # if the character is not in the dictionary then add it to the dictionary and set the value to 1
# what this above code does is it counts the frequency of each character in the sentence and stores it in a dictionary  
# print(charFrequency)

sortedCharFrequency = sorted(charFrequency.items(), key=lambda kv: kv[1], reverse=True) # sort the dictionary by value in descending order . kv is a tuple, key is the character and value is the frequency


print(sortedCharFrequency[0])