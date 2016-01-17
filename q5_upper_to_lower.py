#q5_upper_to_lower.py
#converts an uppercase character to lowercase

#input variable

letter = input("Please input an upper case letter:")
print()

#check validity of variable

##while len(letter)!=1:
##    letter = input("ERROR: More than one letter \n Please input an upper case letter")
##
##ascii_value = ord(letter)
##
##while ascii_value<65 or ascii_value>90:
##    letter = input("ERROR: Letter not in upper case \n Please enter an upper case letter:")
##    ascii_value = ord(letter)

if len(letter) == 1:
    ascii_value = ord(letter)
else:
    ascii_value = 0

while len(letter) != 1 or ascii_value < 65 or ascii_value > 90:
    
    if len(letter)!=1:
        letter = input("ERROR: More than one letter \n Please input an upper case letter: ")
        print()
        if len(letter) == 1:
            ascii_value = ord(letter)
        else:
            ascii_value = 0

    if ascii_value<65 and ascii_value!=0 or ascii_value>90:
        letter = input("ERROR: Letter not in upper case \n Please enter an upper case letter:")
        print()
        if len(letter) == 1:
            ascii_value = ord(letter)

#conversion
        
ascii_value = ord(letter)
new_letter = chr(ascii_value + 32)

#display result

print("The letter in lower case is:", new_letter)
