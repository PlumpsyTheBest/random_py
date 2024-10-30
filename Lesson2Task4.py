# Converts a letter to uppercase if it is a lowercase letter.
def to_upper_case(letter):
    letter = ord(letter)
    if letter >= 97 and letter <= 122:
        letter = letter - 32
    letter = chr(letter)
    return letter

# Converts a letter to lowercase if it is an uppercase letter.
def to_lower_case(letter):
    letter = ord(letter)
    if letter >= 65 and letter <= 91:
        letter = letter + 32
    letter = chr(letter)
    return letter

# Formats the sentence by converting odd-positioned letters to lowercase and even-positioned letters to uppercase.
def format_sentence(input_sentence):
    finalised_sentence = ""
    for counter in range(0, len(input_sentence)):
        if counter % 2 == 0:
            finalised_sentence += to_upper_case(input_sentence[counter])
        else:
            finalised_sentence += to_lower_case(input_sentence[counter])
    return finalised_sentence



# Main Program
if __name__ == "__main__":
    sentence = input("Input a sentence")
    formatted_sentence = format_sentence(sentence)