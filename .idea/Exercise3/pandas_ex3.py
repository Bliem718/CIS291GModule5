#This program is made by Bryan Liem. This programpens a csv file of people involved in the Titanic event and alters and displays certain characteristics in a Data Frame.
#Imports the necessary modules csv, matplotlib.pyplot as plt for plotting a bar chart, and pandas as pd for creating data frames.
import csv
import matplotlib.pyplot as plt
import pandas as pd

#A function that prints out a data frame's first and last 10 lines when run.
def printHeadTail(DataFrame):
    print(pd.concat([DataFrame.head(10), DataFrame.tail(10)]))
    print()

#Opens TitanicSurvival.csv, which contains the raw Titanic data, as outputFile.
with open ('TitanicSurvival.csv', 'r') as outputFile:

#Reads outputFile using "," as a delimiter and sets rawTitanicFrame with the data.
    rawTitanicFrame = csv.DictReader(outputFile, delimiter=',')

#Creates a data frame called titanicFrame from rawTitanicFrame.
    titanicFrame = pd.DataFrame(rawTitanicFrame)

#Runs the printHeadTail() function to print the first and last 10 lines of the data frame.
#Note that one column may be displayed as ... due to there not being enough space to display all columns.
    printHeadTail(titanicFrame)

#Renames the necessary columns.
    titanicFrame = titanicFrame.rename(columns={'rownames':'Name',
                                                'survived':'Survival',
                                                'sex':'Sex',
                                                'age':'Age',
                                                'passengerClass':'Class'
                                                })

#Removes all rows of data which as no value for the Age column and prints the first and last 10 lines.
    titanicFrame = titanicFrame.loc[titanicFrame['Age'] != '']
    printHeadTail(titanicFrame)

#Creates a data frame that only contains the survivors of titanicFrame and prints the first and last 10 lines.
    titanicSurvivors = titanicFrame.loc[titanicFrame['Survival'] == 'yes']
    printHeadTail(titanicSurvivors)

#Creates and displays a histogram of titanicSurvivors using the Age column as a reference and uses 50 bins.
    hist = titanicSurvivors['Age'].hist(bins=50)
    plt.show()

#Creates and prints the names and ages of the first and last 10 lines of titanicFrame.
    titanicFirstAndLast10 = pd.concat([titanicFrame.head(10).loc[:, ['Name', 'Age']],
                                       titanicFrame.tail(10).loc[:, ['Name', 'Age']]])
    print(titanicFirstAndLast10)
    print()

#Creates and prints the names and ages of titanicSurvivors that has an age of under 25. Also displays how many survivors are under the age of 25.
    titanicSurvivorsUnder25 = titanicSurvivors.loc[titanicSurvivors['Age'].astype(float) < 25.0, ['Name', 'Age']]
    print(titanicSurvivorsUnder25)
    print(f'There are {len(titanicSurvivorsUnder25)} survivors of the Titanic that are under 25.')

#Creates and prints the names of survivors of titanicSurvivors that are in 1st class.
    titanicSurvivors1stClass = titanicSurvivors.loc[titanicSurvivors['Class'] == '1st', ['Name']]
    print(titanicSurvivors1stClass)

#Creates and prints the names of survivors of titanicSurvivors that are in 2nd class.
    titanicSurvivors2ndClass = titanicSurvivors.loc[titanicSurvivors['Class'] == '2nd', ['Name']]
    print(titanicSurvivors2ndClass)

#Creates and prints the names of survivors of titanicSurvivors that are in 3rd class.
    titanicSurvivors3rdClass = titanicSurvivors.loc[titanicSurvivors['Class'] == '3rd', ['Name']]
    print(titanicSurvivors3rdClass)

#Prints how many survivors that are in each of the three classes.
    print(f'There are {len(titanicSurvivors1stClass)} 1st class survivors, {len(titanicSurvivors2ndClass)} 2nd class survivors, and {len(titanicSurvivors3rdClass)} 3rd class survivors.')

#Creates a series using the total amount of survivors of each class along with an index that states each class position.
    titanicSurvivorsToPlot = pd.Series([len(titanicSurvivors1stClass), len(titanicSurvivors2ndClass), len(titanicSurvivors3rdClass)],
                                       index=['1st Class', '2nd Class', '3rd Class'])

#Creates and displays a vertical bar chart from series titanicSurvivorsToPlot that displays the population of survivors of each class.
    chart = titanicSurvivorsToPlot.plot.bar(x=0, rot=0)
    plt.show()
