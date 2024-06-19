#Determines whether a given string is a pangram
def is_pangram(input_string):
    unique_chars = set()
    lowercase_string = input_string.lower()
    for char in lowercase_string:
        if char.isalpha():
            unique_chars.add(char)
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    if len(unique_chars) == len(alphabet):
        return True 
    else:
        return False
    
print(is_pangram("Pack my box with five dozen liquor jugs")) 
print(is_pangram("This is not a pangram"))  