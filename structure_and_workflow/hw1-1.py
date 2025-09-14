name = input("Enter the name of the rectangle: ")
length_of_one_side = float(input("Enter the length of one side (cm.) : "))
length_of_other_side = float(input("Enter the length of the other side (cm.) : "))
area = length_of_one_side * length_of_other_side
diagonal = (length_of_one_side ** 2 + length_of_other_side ** 2) ** 0.5

print(f"The area of {name} is {area} sq. cm.")
print(f"The diagonal of {name} is {diagonal} cm.")