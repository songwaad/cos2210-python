print("--- ID Checksum Calculator ---")
number_id = input("Enter 13-digit ID number: ")

sum = 0
j = 13
for i in range(12):
    sum += int(number_id[i]) * j
    j -= 1

fraction_of_sum = sum % 11
checksum = 11 - fraction_of_sum

print(f"Calculated checksum digit {checksum}")
