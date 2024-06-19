# Sentence as input and returns a new sentence with the words reversed in the same order that Master Yoda would use.
def master_speak(string):
    words = string.split()
    yoda_words = words[::-1]
    yoda_string = ' '.join(yoda_words)
    return yoda_string

print(master_speak("I am a Jedi Master"))