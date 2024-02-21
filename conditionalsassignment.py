x = input("Enter a number:")
number = int(x)

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")


choice = input("Do you choose the path to the left or right? ")

if choice == "left":
    print("You find a treasure chest!")
elif choice == "right":
    print("You encounter a dragon!")
else:
    print("Invalid choice!")


num1 = input("Input the first integer",)
num2 = input("Input the second integer")
num3 = input("Input the third integer")

if num1 > num2 and num1 > num3:
    print("This number is the largest", num1)
elif num2 > num1 and num2 > num3:
    print("this is the largest number", num2)
else:
    print("this is the largest number", num3)


if num1 < num2 and num1 < num3:
    print("This number is the smallest", num1)
elif num2 < num1 and num2 < num3:
    print("this is the smallest number", num2)
else:
    print("this is the smallest number", num3)


if num1 == num2 and num1 == num3:
    print("All three are equal")
elif num1 == num2 or num1 == num3:
    print("Two numbers are equal")
elif num2 == num3:
    print("Two numbers are equal")
else:
    print(0)

year = int(input())

if (year % 400 == 0) and (year % 100 == 0):
    print("This is a leap year")

elif (year % 4 == 0) and (year % 100 != 0):
    print("This is a leap year")
else:
    print("This is not a leap year")

if year % 100 == 0:
    print("Century")

if year == 2024:
    print("Current Year")
elif year > 2024:
    print("Future")
else:
    print("Past")



