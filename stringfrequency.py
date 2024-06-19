#Function that takes a string returns the character that appears most frequently
string_input = input("Enter a String: ")

string_input = "".join(string_input.split())

countCharacter_frequency = {}

for character in string_input:
    if character in countCharacter_frequency:
        countCharacter_frequency[character] +=1
    else:
        countCharacter_frequency[character] = 1

max_frequency  = max(countCharacter_frequency, key=countCharacter_frequency.get)

print(f"Character : {max_frequency} has the highest frequency")