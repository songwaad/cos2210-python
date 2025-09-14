name = input("Enter you name : ")
year_of_birth = int(input("Enter your year of birth : "))
user_name = f"C{str(year_of_birth-543)[2:4]}{name}"

print(f"Your user name is {user_name}")