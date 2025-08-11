def swapped(points):
    new_points = []
    
    for point in points:
        y, x = point
        new_points.append((x, y))
    
    return new_points

points = [(5, 2), (3, 8), (4, 4), (3, 9), (25, 5), (10, 1), (2, 4), (9, 3)]

swapped = [(y, x) for x, y in points]
x_more_than_y = [(x, y) for x, y in points if x > y]
x_less_than_y = [(x, y) for x, y in points if x < y]
x_equal_y = [(x, y) for x, y in points if x == y]
x_power_two_equal_y = [(x, y) for x, y in points if x**2 == y]
y_power_two_equal_x = [(x, y) for x, y in points if y**2 == x]

print(f"Original data: {points} \n")
print(f"a. Swapped (y, x): {swapped}")
print(f"b. Where x > y: {x_more_than_y}")
print(f"c. Where x < y: {x_less_than_y}")
print(f"d. Where x == y: {x_equal_y}")
print(f"e. Where x^2 == y: {x_power_two_equal_y}")
print(f"f. Where y^2 == x: {y_power_two_equal_x}")
