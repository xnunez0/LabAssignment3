




"""
create a ;ist to store 5 numbers (float)
capture user's input 5 times for their grades
each time we captured the user's input, we append the number to the list
sort the lsit ascending, then splice the items staring at index 2
once we have three highest number in the list, we sum them up and devide by 3
output a message to the user 
end
"""


"""
create lsit 

capture input
append number to list 

capture input
append number to list 

capture input
append number to list 

capture input
append number to list 

capture input
append number to list 
sorth the list, then splice out the lowest 2 numbers
print message to user
"""

grades = []

grade = input("Enter the 1st grade: ")
grades.append(float(grade))

grade = input("Enter the 2nd grade: ")
grades.append(float(grade))

grade = input("Enter the 3rd grade: ")
grades.append(float(grade))

grade = input("Enter the 4th grade: ")
grades.append(float(grade))

grade = input("Enter the 5th grade: ")
grades.append(float(grade))


grades.sort()

grades = grades[2:]

grades = sum(grades)

result = grades / 3

print("Average Grade {0:.2f}%".format(result))

