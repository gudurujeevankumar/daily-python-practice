n = int(input("Enter the number : ")) # for getting user input
last = 0 # For storing last digit
count = 0 #for storing count of the digits in number
am = 0 # To store calculated armstrong number

num = n # Reassigning the user input value to another variable 
        # because after counting we loss the main number

Arm = num

if n > 0 :
    while n > 0:  # To calculate the count of digits in given number
        count += 1
        n //= 10

    for i in range(count): # To calculate the armstrong number
        last = num % 10
        am += last ** count
        num //= 10

    if Arm == am: print("Given number is an amstrong number") 
    else: print("Given number is not an amstrong number because the output is : " ,am)
    
