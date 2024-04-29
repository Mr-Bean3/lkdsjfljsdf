x = int(input("Enter a value for x:"))
y = int(input("Enter a value for y:"))
z = int(input("Enter a value for z:"))
if x > 0 and y > 0:
    print("Both x and y are positive.")
elif x < 0 or y < 0:
    print("At least one of x or y is negative.")
else:
    print("Both x and y are non-positive.")

if x == 0 or y == 0:
    print("At least one of x or y is zero.")
elif x > 0 and z > 0:
    print("Both x and z are positive.")
else:
    print("Neither x nor z is positive.")

if x > 0 and y > 0 or z > 0:
    print("At least one of x, y, or z is positive.")
elif x < 0 or y < 0 and z < 0:
    print("All of x, y, and z are negative.")
else:
    print("Neither x, y, nor z is positive.")

if x != 0 and y != 0:
    print("Neither x nor y is zero.")
elif x == 0 and y == 0:
    print("Both x and y are zero.")
else:
    print("At least one of x or y is zero.")

if x == y and y == z:
    print("All three variables are equal.")
elif x != y and y != z and x != z:
    print("All three variables are different.")
else:
    print("Some variables are equal and some are different.")
