num = int(input("Enter the number of terms: "))

x = 0 
y = 1

print("Fibonacci Series:", end=" ")

for i in range(num):
    print(x, end=" ")
    x, y=y, x+y
