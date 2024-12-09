#This program is made by Bryan Liem. This program creates a Data Frame from a dictionary and alters and displays certain information in the Data Frame.
#Imports the necessary module pandas as pd.
import pandas as pd

#Creates a new dictionary called data with the following information on Courses, No of Students, and Department.
data = { 'Course': [ 'Financial Accounting', 'Microeconomics', 'Programming Fundamentals', 'Statistics', 'Data Science'],
         'No of Students': [150, 75, 200, 175, 125],
         'Department': ['Accountancy', 'Economics', 'CIS', 'Math', 'Math' ] }

#Creates a new Data Frame called schoolClasses using the data dictionary and prints it.
schoolClasses = pd.DataFrame(data)
print(schoolClasses)

#Prints only the Course and Department columns of schoolClasses.
print(schoolClasses.loc[:, ['Course', 'Department']])

#Prints only rows 0, 3, and 4 from the Course and Department columns of schoolClasses.
print(schoolClasses.loc[[0, 3, 4], ['Course', 'Department']])

#Prints the amount of rows and columns schoolClasses has. Row amount: schoolClasses[0]. Column amount: schoolClasses[1].
print(f'Table "schoolClasses" has {schoolClasses.shape[0]} rows and {schoolClasses.shape[1]} columns.')

#Creates a new column called Professor in schoolClasses that displays the professor names and prints the Data Frame.
schoolClasses['Professor'] = ['Brown', 'Griffin', 'Sanchez', 'Chen', 'Pavone']
print(schoolClasses)

#Creates a new row of the schoolClasses Data Frame using the below information.
schoolClasses.loc[len(schoolClasses)] = ['Discrete Math', 65, 'Math', 'Hasson']
print(schoolClasses)

#Creates a new column called Capacity in schoolClasses that displays the max capacity of each course and prints the Data Frame.
#Note that the capacity of all classes is 200 .
schoolClasses['Capacity'] = 200
print(schoolClasses)

#Renames the No of Students column to Students in the Data Frame.
schoolClasses = schoolClasses.rename(columns={'No of Students':'Students'})
print(schoolClasses)

#Creates a new column called Avail in schoolClasses that displays the available seats of each course and prints the Data Frame.
#The Avail of each course is Capacity - Students.
schoolClasses['Avail'] = schoolClasses['Capacity'] - schoolClasses['Students']
print(schoolClasses)

#Prints the average class size of the Data Frame.
print(f'Average class size: {schoolClasses["Students"].mean()}')

#Prints the class with the most available seats, or the course with the highest Avail.
print(f'Class with the most available seats: {schoolClasses["Course"][schoolClasses["Avail"].idxmax()]}')

#Drops the row for the Financial Accounting course and prints the Data Frame.
schoolClasses = schoolClasses.drop(schoolClasses[schoolClasses['Course'] == 'Financial Accounting'].index)
print(schoolClasses)
