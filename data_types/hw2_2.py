travel_distance = float(input("Enter travel distance (km): "))
type_of_car = int(input("Enter the type of car: "))
driving_pattern = int(input("Enter driving pattern: "))
fuel_required = 0.0

fuel_rate = {
    1: {1: 12, 2:10},
    2: {1: 10, 2:8},
    3: {1: 9, 2:7}
}

fuel_required = travel_distance / fuel_rate[type_of_car][driving_pattern]
print(f"Fuel required: {fuel_required:.2f} liters.")
        