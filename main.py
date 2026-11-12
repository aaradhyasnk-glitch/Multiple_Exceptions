try:
    num1= int(input("Enter the first number:"))
    num2= int (input ("Enter second number:"))
    result = num1/num2
    print ("Result is", result)

except ZeroDivisionError:
    print ("Division by zerp is an error!!")

except ValueError:
    print ("Please enter a valid whole number!")

except :
    print ("Wrong input")

else:
    print ("No exceptions!")

finally:
    print ("This will run no matter what!")