grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort()
grades.reverse()
print(grades)

total_grades = sum(grades) 
average = total_grades / len(grades) 
print(average)


grades = input("Enter your grade")
if grades < "80":
    print("Failed")
else:
    print("Passed")


submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

submitted_attended = []
for x in submitted:
    if x in attended:
        submitted_attended.append(x)
print(submitted_attended)

print(submitted is attended)

attended_update = []
for student_submitted in attended:
    if student_submitted not in submitted:
        attended.remove(student_submitted)
print(attended)


temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
print(temperatures[7:14]) 

temperatures_high = [x for x in temperatures if x > 100]
print(temperatures_high)

temperatures.reverse()
print(temperatures[4:9])


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)

if 7 in numbers:
    print(True)

# The lesson hasn't gone over dictionaries yet, therefore I'm not able to do this assignment yet. 

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]