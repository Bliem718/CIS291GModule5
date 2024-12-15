#This program is made by Bryan Liem. This program examines physical characteristics of major characters in the Star Wars trilogy.
#This program includes printing tables of characters based on eye color, as well as displaying bar and pie charts of the physical characteristics.
#Note that the genfromtxt method is not used here since genfromtxt only properly works with .txt files,
#and genfromtxt reads all data from a .csv file as NaN.

#Imports the necessary modules csv to read csv files, matplotlib.pyplot as plt for plotting charts, and pandas as pd for creating data frames.
import csv
import matplotlib.pyplot as plt
import pandas as pd

#Allows the full display of Data Frames of up to 100 rows. Note that the starwars.csv file has 87 values.
pd.options.display.max_rows = 100

#Used to hold eye colors used by the getFromEyeColor() function.
usedEyeColors = []

#Defines a function called getFromEyeColor() that prints a list of characters with a specified eye color from a specified Data Frame.
#Has special instructions if the eye color chosen is other.
def getFromEyeColor(DataFrame, eyeColor):
    if eyeColor == 'other':

    #Finds characters that have an eye color that is not in the usedEyeColors list and prints their details.
    #Also returns the amount of entries that do match the criteria. 
        print(f'\nCharacters with {eyeColor} colored eyes:')
        print(DataFrame.loc[~DataFrame['eye_color'].isin(usedEyeColors)])
        return len(DataFrame.loc[~DataFrame['eye_color'].isin(usedEyeColors)])

    else:
    #Finds characters that have an eye color that is specified and prints their details.
    #Also appends the eye color in the usedEyeColors list and returns the amount of entries that do match the criteria. 
        print(f'\nCharacters with {eyeColor} colored eyes:')
        print(DataFrame.loc[DataFrame['eye_color'] == eyeColor])
        usedEyeColors.append(eyeColor)
        return len(DataFrame.loc[DataFrame['eye_color'] == eyeColor])

#Opens starwars.csv, which contains the raw Star Wars character data, as outputFile.
#The encoding parameter ensures that some character's names, such as Padmé Amidala, do not show up as Mojibake.
with open ('starwars.csv', 'r', encoding='UTF-8') as outputFile:

#Reads outputFile using "," as a delimiter and sets rawStarWarsFrame with the data.
    rawStarWarsFrame = csv.DictReader(outputFile, delimiter=',')

#Creates a data frame called starWarsFrame based on the name, hair_color, eye_color, and gender columns of rawStarWarsFrame. 
    starWarsFrame = pd.DataFrame(rawStarWarsFrame)[['name', 'hair_color', 'eye_color', 'gender']]

#Replaces all incomplete data in the Data Frame with 'none' and prints the Data Frame.
    starWarsFrame = starWarsFrame.replace('', 'none')
    print(starWarsFrame)

#Assigns six variables, 5 of a specific color, 1 being other, to the returned value from the getFromEyeColor() function.
    blueEyeColor = getFromEyeColor(starWarsFrame, 'blue')
    brownEyeColor = getFromEyeColor(starWarsFrame, 'brown')
    blackEyeColor = getFromEyeColor(starWarsFrame, 'black')
    yellowEyeColor = getFromEyeColor(starWarsFrame, 'yellow')
    orangeEyeColor = getFromEyeColor(starWarsFrame, 'orange')
    otherEyeColor = getFromEyeColor(starWarsFrame, 'other')

#Creates a series using the number of characters possessing specific eye colors.
    pieChartData = pd.Series([blueEyeColor, brownEyeColor, blackEyeColor, yellowEyeColor, orangeEyeColor, otherEyeColor],
                             index=['Blue', 'Brown', 'Black', 'Yellow', 'Orange', 'Other'])

#Creates and displays a pie chart from the series with a matching title and a table for data.
    pieChart = pieChartData.plot.pie(title='Eye Color Distribution of Star Wars Characters', table=True)
    plt.show()

#Assigns three variables that determines how many characters belong in each gender.
    isMasculineGender = len(starWarsFrame.loc[starWarsFrame['gender'] == 'masculine'])
    isFeminineGender = len(starWarsFrame.loc[starWarsFrame['gender'] == 'feminine'])
    isOtherGender = len(starWarsFrame.loc[~starWarsFrame['gender'].isin(['masculine', 'feminine'])])

#Creates a series using the number of characters being specific genders.
    barChartData = pd.Series([isMasculineGender, isFeminineGender, isOtherGender],
                             index=['Masculine', 'Feminine', 'Other'])

#Creates and displays a bar chart from the series with a matching title and a table for data.
#The bar chart also include a Y-label that says "Frequency", a grid, and the font size is set to 0 to solve formatting issues with double labeling.
    barChart = barChartData.plot.bar(title='Gender Distribution of Star Wars Characters', ylabel='Frequency', rot=0, fontsize=0.0, grid=True, table=True)
    plt.show()

#Assigns three variables that determines how many blue-eyed characters posses specific hair colors.
    isBlondHaired = len(starWarsFrame.loc[(starWarsFrame['eye_color'] == 'blue') & (starWarsFrame['hair_color'] == 'blond')])
    isBrownHaired = len(starWarsFrame.loc[(starWarsFrame['eye_color'] == 'blue') & (starWarsFrame['hair_color'] == 'brown')])
    isBlackHaired = len(starWarsFrame.loc[(starWarsFrame['eye_color'] == 'blue') & (starWarsFrame['hair_color'] == 'black')])

#Creates a series using the number of blue-eyed characters possessing specific hair colors.
    barChartData = pd.Series([isBlondHaired, isBrownHaired, isBlackHaired],
                             index=['Blond', 'Brown/Brunette', 'Black'])

#Creates and displays a bar chart from the series with a matching title and a table for data.
#The bar chart also include a Y-label that says "Frequency", a grid, and the font size is set to 0 to solve formatting issues with double labeling.
    barChart = barChartData.plot.bar(title='Hair Color Distribution of Blue Eyed Star Wars Characters', ylabel='Frequency', rot=0, fontsize=0.0, grid=True, table=True)
    plt.show()
