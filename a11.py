def is_palindrome_number(n):
    num_str=str(n)
    return num_str==num_str[::-1]

input=int(input("enter a number:"))
if is_palindrome_number(input):
    print(f"{input}is palindrome")
else:
     print(f"{input}is not a palindrome")

    