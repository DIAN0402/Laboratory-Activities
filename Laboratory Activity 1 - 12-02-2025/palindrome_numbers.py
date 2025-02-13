num = int(input("Enter a number: "))

orig = str(num)

reversed_num = orig[::-1]

if(orig == reversed_num):
    print("Palindrome")
else:
    print("Not a Palindrome")