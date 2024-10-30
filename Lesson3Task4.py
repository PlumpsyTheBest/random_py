# Analyse the frequency of each character in the text
def analyze_frequency(text):
    characters = []
    frequency = []
    for counter_1 in range(len(text)):
        found = False
        for counter_2 in range(len(characters)):
            if characters[counter_2] == text[counter_1]:
                frequency[counter_2] += 1
                found = True
        if found == False:
            characters.append(text[counter_1])
            frequency.append(1)
    return characters, frequency


# Calculate the sum of ASCII values multiplied by their frequencies
def calculate_ascii_sum(characters, frequency):
    total = 0
    for counter in range(len(characters)):
        total += ord(characters[counter])*frequency[counter]
    return total


# Display the characters, their frequencies, and the total ASCII-based sum
def display_frequencies_and_sum(characters, frequency, sum):
    for counter in range(len(characters)):
        print(characters[counter])
        print(frequency[counter])
    print(sum)


# Main Program
if __name__ == "__main__":
    input_text = input("Give a text")
    all_characters, frequency_of_characters = analyze_frequency(input_text)
    ascii_sum = calculate_ascii_sum(all_characters, frequency_of_characters)
    display_frequencies_and_sum(all_characters, frequency_of_characters, ascii_sum)
