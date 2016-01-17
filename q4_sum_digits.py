#q4_sum_digits.py
#Summing digits in an integer

#get input variables
value_to_process = int(input("Please input an integer between 0 and 1000:"))

#check validity of integer

while value_to_process<0 or value_to_process >1000:

    value_to_process = int(input("FAILED. Please input a valid integer between 0 and 1000:"))
    

#process integer

if 0<=value_to_process<=1000:
    fourth_digit = value_to_process%10
    value_to_process = value_to_process // 10

    third_digit = value_to_process%10
    value_to_process = value_to_process // 10

    second_digit = value_to_process%10
    value_to_process = value_to_process // 10

    first_digit = value_to_process

sum_of_integer = first_digit + second_digit + third_digit + fourth_digit


#show result
    
print(sum_of_integer)
