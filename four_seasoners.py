# find epicenter of triangle

x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))
x3 = int(input("Enter x3: "))
y3 = int(input("Enter y3: "))

x = (x1 + x2 + x3)/3
y = (y1 + y2 + y3)/3

print (f"Denesh's House is at: ({round(x,1)}, {round(y,1)})")
