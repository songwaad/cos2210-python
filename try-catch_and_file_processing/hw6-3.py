def quad1(a, b, c):
    return (-b + (b**2 - (4 * a * c )) ** (0.5)) / (2 * a)

def quad2(a, b, c):
    return (-b - (b**2 - (4 * a * c )) ** (0.5)) / (2 * a)

def open_file(filename):
    try:
        with open(filename, encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        raise e
    
n = 2

filename = f"problems{n}.txt"
print(f"file : {filename}:")
file = open_file(filename)
print(file)

print(f"Choose your ploblem file:{filename}")

lines = file.splitlines()
a, b, c = [], [], []

for line in lines:
    nums = line.split()
    a.append(int(nums[0]))
    b.append(int(nums[1]))
    c.append(int(nums[2]))

for val_a, val_b, val_c in zip(a, b, c):
    if val_a == 0 or (val_b**2 - (4 * val_a * val_c )) < 0:
        print("Invalid problem")
        continue

    print(quad1(val_a, val_b, val_c), quad2(val_a, val_b, val_c))
