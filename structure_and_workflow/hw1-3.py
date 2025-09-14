max_weight = int(input("Enter the maximum weight the lift can carry (kg): "))
avg_weight_per_person = int(input("Enter the average weight per person (kg): "))
max_people = max_weight // avg_weight_per_person

print(f"Maximum number of people the lift can carry: {max_people}")