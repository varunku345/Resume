num1 = float(input("enter the first number here: "))
num2 = float(input("enter the second number here: "))

print("press 1 for addition\n press 2 for substraction \n press 3 for multiplication\n press 4 for divide")

choice = int(input("enter the choice number from 1 to 4: "))

if choice == 1: 
      print("the sum of number" ,num1+num2)
elif choice == 2:
      print("substraction of two number", num1-num2)
elif choice == 3:
      print("multiplication of two number",num1*num2)
elif choice == 4:
      print("divide the two number", num1/num2)
else:
      print("invalid input")
      