#q6_find_ascii_char.py
#displays character corresponding to ASCII value inputted

#input variable

ascii_value = int(input("Please enter an integer between 0 and 127:"))

#check validity

while ascii_value<0 or ascii_value>127:
    ascii_value = int(input("ERROR: Integer not between 0 and 127 \n Please enter an integer between 0 and 255: "))
    
#process

character = chr(ascii_value)

#display result

print("The character is:",character)
