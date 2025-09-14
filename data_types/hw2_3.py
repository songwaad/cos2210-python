print("--- Multiple Choice Answer Checker ---")

correct_answers = input("Enter the string of correct answers: ")
while True:
    student_answers = input("Enter the string of student's answers: ")
    number_of_correct = 0

    if len(correct_answers) != len(student_answers):
        print("Incomplete answers")
    else:
        for i in range(len(student_answers)):
            if correct_answers[i].lower() == student_answers[i].lower():
                number_of_correct += 1
        print(f"Number of correct answers: {number_of_correct}")
    
    correct_answers = input(f"Enter the correct answers (type 'exit') to quit")
    if correct_answers.lower() == 'exit':
        break

print("Exiting program. Goodbye!")