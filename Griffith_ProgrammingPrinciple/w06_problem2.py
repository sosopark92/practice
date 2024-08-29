#given an input number n, print a diamond shape with 2*n-1 rows.


n = int(input("Enter number: "))
rows = 2*n-1
i = 1

for i in range(i, rows, 2):
    for j in range(0, i):
        print("x", end="")
    print()