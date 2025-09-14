
x1, y1, radius1 = map(int, input("Enter x, y, radius for Circle 1: ").split())
x2, y2, radius2 = map(int, input("Enter x, y, radius for Circle 2: ").split())

d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
if d < radius1 + radius2:
    print("overlap")
elif d == radius1 + radius2:
    print("touch")
elif d > radius1 + radius2:
    print("free")