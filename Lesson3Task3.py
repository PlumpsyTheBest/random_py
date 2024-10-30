# Get details for a number of dogs
def get_dog_details(number_of_dogs):
    name_array = []
    breed_array = []
    Obedience_array = []
    Behaviour_array = []
    Obstacle_Course_array = []
    Looks_array = []


    for counter in range(number_of_dogs):
        name_array.append(input("What is the name of dog " + str(counter+1)))
        breed_array.append(input("What is the breed of dog " + str(counter+1)))
        Obedience_array.append(get_valid_score("Obedience"))
        Behaviour_array.append(get_valid_score("Behaviour"))
        Obstacle_Course_array.append(get_valid_score("Obstacle Course"))
        Looks_array.append(get_valid_score("Looks"))
    return name_array, breed_array, Obedience_array, Behaviour_array, Obstacle_Course_array, Looks_array


# Ensure a valid score from the user for the given category
def get_valid_score(question):
    answer = -1
    while answer >100 or answer < 0:
        answer = int(input("What is the score for " + question))
    return answer


# Calculate the overall score for each dog, rounded to 2 dp
def calculate_overall_scores(obedience, behaviour, obstacle_course, looks):
    average = [0]*len(obedience)
    for counter in range(len(obedience)):
        average[counter] = (obedience[counter] + behaviour[counter] + obstacle_course[counter] + looks[counter])/4
    return average

# Function to display the details of each dog with their overall score
def display_dog_results(name, breed, overall_score):
    for counter in range(len(name)):
        print(name[counter])
        print(breed[counter])
        print(overall_score[counter])

# Main Program
if __name__ == "__main__":
    no_dogs = int(input())
    dog_names, dog_breeds, dog_scores_Obedience, dog_scores_Behaviour, dog_scores_Obstacle_Course, dog_scores_Looks = get_dog_details(no_dogs)
    average_scores = calculate_overall_scores(dog_scores_Obedience,dog_scores_Behaviour,dog_scores_Obstacle_Course, dog_scores_Looks)
    display_dog_results(dog_names, dog_breeds, average_scores)