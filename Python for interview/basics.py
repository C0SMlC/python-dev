n, m = 4, 5

print(f"The numbers are {n} and {m}")

if (n > m and n != 0):
    print("n is greater than m")
elif (m > n or m != 0):
    print("m is greater than n")
else:
    print("n and m are equal")

n = 0

while n < 10:
    print(n)
    n = n+1
