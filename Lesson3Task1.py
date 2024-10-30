# Get student names and scores
def get_names_and_scores():
    names_array = [""]*10
    score_array = [0]*len(names_array)
    for counter in range(len(names_array)):
        names_array[counter] = input("What is the name of student " + str(counter+1))
        score_array[counter] = get_valid_score()
    return names_array, score_array


# Get a valid score between 0 and 110
def get_valid_score():
    score = -1
    while score > 110 or score < 0:
        score = int(input("What is the score for this student"))
    return score



# Calculate the percentage for each score
def calculate_percentage(scores):
    percentage_array = [0]*len(scores)
    for counter in range(len(scores)):
        percentage_array[counter] = (scores[counter]/110)*100
    return percentage_array



# Determine grades based on each percentage
def determine_grade(percent):
    grade_array = [""]*len(percent)
    for counter in range(len(percent)):
        if percent[counter] > 80:
            grade_array[counter] = "A"
        elif percent[counter] > 70:
            grade_array[counter] = "B"
        elif percent[counter] > 60:
            grade_array[counter] = "C"
        elif percent[counter] > 50:
            grade_array[counter] = "D"
        else:
            grade_array[counter] = "F"
    return grade_array


# Display student information
def display_student_info(names, scores, percentages, grades):
    print("Student Exam Results:")
    print("Name\t\tScore\t\tPercentage\t\tGrade")
    for counter in range(len(names)):
        print(names[counter] + "\t\t" + str(scores[counter]) + "\t\t" + str(round(percentages[counter], 2)) + "\t\t" + grades[counter])


# Main Program
if __name__ == "__main__":
    student_names, student_scores = get_names_and_scores()
    student_percentages = calculate_percentage(student_scores)
    student_grades = determine_grade(student_percentages)
    display_student_info(student_names, student_scores, student_percentages, student_grades)
