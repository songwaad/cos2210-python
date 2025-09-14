def open_file(filename):
    try:
        with open(filename, encoding="utf-8") as file:
            return file.read()
        
    except Exception as e:
        raise e
    
def is_equal(v1, v2):
    return len(v1) == len(v2)

def dot(v1, v2):
    sum = 0
    for val1, val2 in zip(v1, v2):
        sum = sum + (val1 * val2)
    return sum


n = 3
filename = f"vector{n}.txt"
file = open_file(filename)

print(f"File {filename}:")
print(file)

lines = file.splitlines()
v1 = [float(x) for x in lines[0].split()]
v2 = [float(x) for x in lines[1].split()]

print(f"Choose your vector file: {filename}")
print(f"v1 = {v1}")
print(f"v1 = {v2}")

if not is_equal(v1, v2):
    print("Incompatible size")
else:
    print(f"v1*v2 = {dot(v1, v2)}")