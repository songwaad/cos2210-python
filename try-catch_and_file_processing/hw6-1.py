def open_file(filename):
    try:
        with open(filename, encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        raise e
    
def robot_move(position, move):
    match move:
        case 'L':
            position[0] = position[0] - 1
        case 'R':
            position[0] = position[0] + 1
        case 'U':
            position[1] = position[1] + 1
        case 'D':
            position[1] = position[1] - 1

x = 10
y = 20
n = 2

filename = f"move{n}.txt"
print(f"file : {filename}:")
file = open_file(filename)
print(file)
moves = file.splitlines()

robot_stop_point = [x, y]

print(f"Choose your movefile: {filename}")
print(f"Initial position : {x},{y}")

for move in moves:
    if move not in ['L', 'R', 'U', 'D']:
        print("Invalid command")
        break
    robot_move(robot_stop_point, move)
else:
    print(f"Robot stops at {robot_stop_point[0]},{robot_stop_point[1]}")