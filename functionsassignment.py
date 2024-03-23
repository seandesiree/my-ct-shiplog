def addition(a, b): 
    added_numbers = a + b
    print(added_numbers)

def subtraction(a,b): 
    sub_numbers = a - b
    print(sub_numbers)

def multiply(a, b): 
    multiply_numbers = a * b
    print(multiply_numbers)

def divide(a,b): 
    divide_numbers = a / b
    print(divide_numbers)


numbers_input1 = int(input("What is the first number you would like to calculate? "))
numbers_input2 = int(input("What is the second number you would like to calculate? "))
calculation = input("What mathematical operation would you like to perform: Enter the letter [A]ddition, [S]ubtraction, [M]ulptication, [D]ivision ").upper()

if calculation == "A":
    addition(numbers_input1, numbers_input2)
elif calculation == "M":
    multiply(numbers_input1, numbers_input2)
elif calculation == "S":
    subtraction(numbers_input1, numbers_input2)
elif calculation == "D":
    divide(numbers_input1, numbers_input2)
else:
    print("Wrong input, try again")


   
grocery_list = []

def shopping_list(*items):
    while True:
        print("Grocery List Editor")
        print("1. Add Item")
        print("2. Delete Item")
        print("3. Print List")
        print("Type done to exit")
        option = input("Enter 1, 2 or 3 to continue ")

        if option == "1":
            new_items = input("What items would you like to add? ")
            grocery_list.append(new_items)
        elif option == "2":
            delete_items = input("What items would you like to remove? ")
            if delete_items in grocery_list:
                grocery_list.remove(delete_items)
            else:
                print("Item is not in grocery list")
        elif option == "3":
            print(grocery_list)
        elif option == "done":
            break
        else:
            print("Wrong input, please try again")

shopping_list()



grades = []

def average_grade():
     while True:
        print("Grading Assistant")
        print("1. Average")
        print("2. Letter grade")
        choice = input("Which option would you like to choose? ")

        if choice == "1":
            students = int(input("How many students did you enter grades for?"))
            for student in range(students):
                grade = int(input(f"Enter the grade for a student {student + 1}. "))
                grades.append(grade)
                print(grades)        
            average = sum(grades) / students
            highest_grade = max(grades)
            lowest_grade = min(grades)
            print(f"This is the highest grade {highest_grade} and this is the lowest grade {lowest_grade}")
            print(average)
        elif choice == "2":
            if grades:
                for grade in grades:
                    if grade >= 90:
                        print("A")
                    elif grade >= 80:
                        print("B")
                    elif grade >= 70:
                        print("C")
                    elif grade >= 60:
                        print("D")
                    else:
                        print("F")
            else:
                print("Add grades")

average_grade() 



questions = ["What is the capital of Alabama? ", "What is the capital of Alaska? ", "What is the capital of Arkansas? ", "What is the capital of Arizona?"]
answers = ["Montgomery", "Juneau", "Little Rock", "Phoenix"]

def quiz(questions, answers):
    score = 0
    for i in range(len(questions)):
        user_answer = input(questions[i]).capitalize() 
        print(user_answer == answers[i])
        if user_answer == answers[i]:
            score += 1
    print(f"You got {score} correct")

quiz(questions, answers)



activities = ["Did you walk today? ", "Did you rock climb today? ", "Did you box today? "] 
duration = [10, 50, 40]
calories_burned = duration * 3

def workout_tracker(activites, duration):
    time = 0
    for i in range(len(activities)):
        user_answer = input(activities[i]).capitalize() 
        if user_answer == "Yes":
            time += duration[i]
            calories_burned = time * 3.5
    print(f"You worked out for {time} minutes and burned {calories_burned}")

workout_tracker(activities, duration)