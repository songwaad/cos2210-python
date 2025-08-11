students = {
    "001": "A",
    "002": "B",
    "003": "C"
}

def add_student(student_id, full_name):
    if students.get(student_id) is not None:
        print("Error : Student ID already exists.")
        return

    students[student_id] = full_name
    print("Student added successfully")

def view_student(student_id):
    full_name = students.get(student_id)

    if full_name is not None:
        print(f"Result: {full_name}")
    else:
        print("Result : Student ID not found")

def update_student(student_id):
    if students.get(student_id) is None:
        print("Student ID not found")
        return
    
    full_name = input("Enter new Full Name:")
    students[student_id] = full_name
    print("Error : Student data updated successfully.")

def delete_student(student_id):
    data = students.pop(student_id, None)
    if data == None:
        print("Error : Student ID not found")
        return
    
    print("Student data deleted successfully.")


def view_all_student():
    for student_id, full_name in students.items():
        print(f"Student ID : {student_id}")
        print(f"Full Name : {full_name}\n")
    
    

menu = "\n--- Student Profile Management ---\n" \
"1. Add Student\n" \
"2. View Students\n" \
"3. Update Student\n" \
"4. Delete Student\n" \
"5. View All Students\n" \
"6. Exit\n" \
"------------------------------\n" \
"Please choose an option :\n" \

# print(menu)

while True:
    choice = input(menu)
    match choice:
        case '1':
            student_id = input("Enter Student ID:")
            full_name = input("Enter Full Name:")
            add_student(student_id, full_name)
        case '2':
            student_id = input("Enter Student ID to view:")
            view_student(student_id)
        case '3':
            student_id = input("Enter Student ID to update:")
            update_student(student_id)
        case '4':
            student_id = input("Enter Student ID to delete:")
            delete_student(student_id)
        case '5':
            view_all_student()
        case '6':
            break
        case _:
            print("This number does not exist, please enter again")
    
