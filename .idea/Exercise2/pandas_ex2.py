#This program is made by Bryan Liem. This program opens a csv file of student grades and alters and displays certain information in the Data Frame.
#Imports the necessary modules csv, matplotlib.pyplot as plt for plotting a pie chart, and pandas as pd for creating data frames.
import csv
import matplotlib.pyplot as plt
import pandas as pd

#Opens testgrades.csv, which contains the raw student grade data, as outputFile.
with open ('testgrades.csv', 'r') as outputFile:

#Reads outputFile using "," as a delimiter and sets rawTestGrades with the data.
    rawTestGrades = csv.DictReader(outputFile, delimiter=',')

#Creates a data frame called testGrades from rawTestGrades.
    testGrades = pd.DataFrame(rawTestGrades)

#Renames the Lastname and Firstname columns.
    testGrades = testGrades.rename(columns={'Lastname':'LName', 'Firstname':'FName'})

#Sets the data type for all test column data to int.
    testGrades['Test1'] = testGrades['Test1'].astype(int)
    testGrades['Test2'] = testGrades['Test2'].astype(int)
    testGrades['Test3'] = testGrades['Test3'].astype(int)
    testGrades['Test4'] = testGrades['Test4'].astype(int)
    testGrades['Final'] = testGrades['Final'].astype(int)

#Prints the testGrades data frame.
    print(testGrades)

#Prints the total number of students in the testGrades data frame.
    print(f'There are {len(testGrades)} students in the sample.')

#Sorts the testGrades row data by the order of their last names and prints their last names, first names, and SSNs.
    testGrades = testGrades.sort_values('LName')
    print(testGrades.loc[:, ['LName', 'FName', 'SSN']])

#Prints the last names, first names, and SSNs for students in testGrades who achieved a final grade of at least 90.
    print(testGrades.loc[testGrades['Final'] >= 90, ['LName', 'FName', 'Final']])

#Prints the percentage of students who achieved a final grade of at least 90.
    print(f'{len(testGrades.loc[testGrades["Final"] >= 90]) / len(testGrades):.2%} of students has a final grade of at least 90.')

#Prints the data for students with a failing grade.
    print(testGrades.loc[testGrades['Grade'] == 'F'])

#Prints the percentage of students who achieved a failing grade.
    print(f'{len(testGrades.loc[testGrades["Grade"] == "F"]) / len(testGrades):.2%} of students has a failing grade.')

#Prints the student with the lowest final grade.
    print(testGrades.loc[testGrades['Final'] == testGrades['Final'].min()])

#Prints the student with the highest final grade.
    print(testGrades.loc[testGrades['Final'] == testGrades['Final'].max()])

#Creates a new data frame testGradesLower that contains the data of students from testGrades who achieved a final grade of less than 70 and prints it.
    testGradesLower = testGrades.loc[testGrades['Final'] < 70]
    print(testGradesLower)

#Prints the total number of students in the testGradesLower data frame (students with a final grade lower than 70).
    print(f'There are {len(testGradesLower)} students in the new data frame.')

#Prints the percentage of students who scored less than 70 on the final and achieved a failing grade.
    print(f'{len(testGradesLower.loc[testGrades["Grade"] == "F"]) / len(testGrades):.2%} of students scored less than 70 on the final and achieved a failing grade.')

#Creates a new data frame testGradesA that contains the data of students from testGrades who achieved a grade of A of any type and prints it.
    testGradesA = testGrades.loc[testGrades['Grade'].str.contains('A')]
    print(testGradesA)

#Creates a new data frame testGradesB that contains the data of students from testGrades who achieved a grade of B of any type and prints it.
    testGradesB = testGrades.loc[testGrades['Grade'].str.contains('B')]
    print(testGradesB)

#Creates a new data frame testGradesB that contains the data of students from testGrades who achieved a grade of C of any type and prints it.
    testGradesC = testGrades.loc[testGrades['Grade'].str.contains('C')]
    print(testGradesC)

#Creates a new data frame testGradesToBePlotted that contains the number of students from testGradesA, testGradesB, testGradesC,
#And other students of testGrades with the indices "A", "B", "C", and "Others".
#This data frame will be used to plot the data onto a pie chart.
    testGradesToBePlotted = pd.Series([len(testGradesA), len(testGradesB), len(testGradesC),
                                       len(testGrades) - (len(testGradesA) + len(testGradesB) + len(testGradesC))],
                                      index=['A', 'B', 'C', 'Others'])

#Creates and displays a pie chart from data frame testGradesToBePlotted that uses the data frame's labels and is sized (5, 5).
#The plot is created andd displayed using matplotlib.pyplot.
    plot = testGradesToBePlotted.plot.pie(labels=testGradesToBePlotted.index, figsize=(5, 5))
    plt.show()

    
