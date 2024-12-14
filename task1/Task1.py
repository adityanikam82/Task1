def reverse_string(s):
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s

input_string = input("Enter a string: ")

print("Reversed String:", reverse_string(input_string))
