#This program is made by Bryan Liem. This program examines the fastfood.csv and outputs six tables andd two bar plots relevant to fast food data.

#Imports the necessary modules csv to read csv files, matplotlib.pyplot as plt for plotting charts, and pandas as pd for creating data frames.
import csv
import matplotlib.pyplot as plt
import pandas as pd


#Defines a function called printFirstSixFromRestaurants that requires a Data Frame parameter and an optional table of column names.
#This function prints the first six items from each restaurant with their respective columns if the columnNames is called.
def printFirstSixFromRestaurants(dataFrame, columnNames=None):

#Creates an empty Data Frame holding the data that will be printed.
    printableDataFrame = pd.DataFrame()

#Calls for every unique restaurant name in the Data Frame. 
    for restaurantName in dataFrame['restaurant'].unique():

    #Sets dataBlock as a Data Frame that contains the first six entries of each restaurant and concats the data to printableDataFrame. 
        dataBlock = pd.DataFrame(dataFrame.loc[dataFrame['restaurant'] == restaurantName].head(6))
        printableDataFrame = pd.concat([printableDataFrame, dataBlock])

#If the columnNames parameter uses default None, then prints every column of printableDataFrame.
    if columnNames == None:
        print(printableDataFrame[:])

#If the columnNames parameter is called, then prints the chosen columns of printableDataFrame.
    else:
        print(printableDataFrame[columnNames])

#Prints a newline before ending the function.
    print()


#Defines a function called printFirstFiveFromRestaurant that requires a Data Frame parameter, a restaurant name parameter, and an optional table of column names.
#This function prints every item from a specified restaurant with their respective columns if the columnNames is called.
def printAllFromRestaurant(dataFrame, restaurantName, columnNames):

#Sets dataBlock as a Data Frame that contains every item from a specific restaurant by restaurantName.
    dataBlock = pd.DataFrame(dataFrame.loc[dataFrame['restaurant'] == restaurantName])

#Prints the Data Frame withe the chosen columns.
    print(dataBlock[columnNames])
    
#Prints a newline before ending the function.
    print()


#Defines a function called printFirstFiveFromRestaurant that requires a Data Frame parameter, a restaurant name parameter, and a column name.
def getAvgFromColumn(dataFrame, restaurantName, columnNames):

#Sets dataBlock as a Data Frame that contains the specified column from a specific restaurant by restaurantName.
    dataBlock = pd.DataFrame(dataFrame.loc[dataFrame['restaurant'] == restaurantName][columnNames].astype(float))

#Gets the average value of dataBlock.
    averageValue = dataBlock.mean()

#Returns the 0th index of averageValue, which is the float average number.
    return averageValue.iat[0]

#Opens fastfood.csv, which contains the raw fast food character data, as outputFile.
#The encoding parameter ensures that some item's names, such as 1/2 lb. FlameThrower® GrillBurger, do not show up as Mojibake.
with open('fastfood.csv', 'r', encoding='UTF-8') as outputFile:

#Introduces how the program works and prompts the user to start it by pressing the enter button.
    print('This program examines the fastfood.csv and outputs six tables andd two bar plots relevant to fast food data.')
    input('Press Enter to start the program.')

#Reads outputFile using "," as a delimiter and sets rawFastFoodFrame with the dictionary data.
    rawFastFoodFrame = csv.DictReader(outputFile, delimiter=',')

#Creates a Data Frame called fastFoodFrame with rawFastFoodFrame as a reference.
    fastFoodFrame = pd.DataFrame(rawFastFoodFrame)

#Removes the rownames, vit_a, vit_c, calcium, and salad columns of the Data Frame. Axis=1 determines to drop labels from the column axis. 
    fastFoodFrame = fastFoodFrame.drop(['rownames', 'vit_a', 'vit_c', 'calcium', 'salad'], axis=1)

#Removes any rows with a restaurant name Taco Bell or Subway.
    fastFoodFrame = fastFoodFrame.loc[~fastFoodFrame['restaurant'].isin(['Subway', 'Taco Bell'])]

#Uses the printFirstSixFromRestaurants function to print the restaurant name, item, calories, and cal_fat columns of the Data Frame.
    print('Calories for specific restaurant items:')
    printFirstSixFromRestaurants(fastFoodFrame, ['restaurant', 'item', 'calories', 'cal_fat'])

#Uses the printAllFromRestaurant to print the item, total_fat, sat_fat, and trans_fat columns of McDonald's items in the Data Frame.
#Note that in some smaller viewports, some columns are replaced by an ellipsis (...).
    print('Fat content for McDonald\'s items:')
    printAllFromRestaurant(fastFoodFrame, 'Mcdonalds', ['item', 'total_fat', 'sat_fat', 'trans_fat'])

#Uses the printAllFromRestaurant to print the item, total_carb, fiber, and sugar columns of Dairy Queen items in the Data Frame.
    print('Carb content for Dairy Queen items:')
    printAllFromRestaurant(fastFoodFrame, 'Dairy Queen', ['item', 'total_carb', 'fiber', 'sugar'])

#Creates a series using the average sodium levels of each restaurant.
#The getAvgFromColumn helps in getting the average sodium levels of each restaurant along with an index that states each restaurant name.
    barChartData = pd.Series([getAvgFromColumn(fastFoodFrame, 'Mcdonalds', ['sodium']),
                              getAvgFromColumn(fastFoodFrame, 'Chick Fil-A', ['sodium']),
                              getAvgFromColumn(fastFoodFrame, 'Sonic', ['sodium']),
                              getAvgFromColumn(fastFoodFrame, 'Arbys', ['sodium']),
                              getAvgFromColumn(fastFoodFrame, 'Burger King', ['sodium']),
                              getAvgFromColumn(fastFoodFrame, 'Dairy Queen', ['sodium'])],
                              index=['McDonald\'s', 'Chick Fil-A', 'Sonic', 'Arby\'s', 'Burger King', 'Dairy Queen']
                              )
#Creates and displays a bar chart from the series with a matching title and a table for data.
#The bar chart also include a Y-label that says "Amount" and a grid.
    barChart = barChartData.plot.bar(title='Average Sodium Levels of Fast Food Restaurants', ylabel='Amount', rot=0, fontsize=9.0, grid=True, table=True, figsize=(10, 7))
    plt.show()

#Uses the printFirstSixFromRestaurants function to print the restaurant name, item, and protein columns of the Data Frame.
    print('Calories for specific restaurant items:')
    printFirstSixFromRestaurants(fastFoodFrame, ['restaurant', 'item', 'protein'])

#Uses the printAllFromRestaurant to print the item and cholesterol columns of Chick Fil-A items in the Data Frame.
    print('Cholesterol content for Chick Fil-A items:')
    printAllFromRestaurant(fastFoodFrame, 'Chick Fil-A', ['item', 'cholesterol'])

#Prints the item and cholesterol columns of Arby's items under 70g of cholesterol in the Data Frame.
    print('Cholesterol content for Chick Fil-A items under 70g:')

#Assigns printFrame to fastFoodFrame and removes any data with a cholesterol level of 70 or above.
#Note that .astype(float) sets the cholesterol values to float values since they appear as a string type in the original Data Frame.
    printFrame = fastFoodFrame.loc[fastFoodFrame['cholesterol'].astype(float) < 70]

#Sets two variables containg only the item names and cholesterol levels of Arby's items.
    printFrame1 = printFrame.loc[printFrame['restaurant'] == 'Arbys']['item']
    printFrame2 = printFrame.loc[printFrame['restaurant'] == 'Arbys']['cholesterol'].astype(float)

#Merges and prints the two Data Frames with an axis of 1.
    printFrame = pd.concat([printFrame1, printFrame2], axis=1)
    print(printFrame)
    

#Creates a series using the average calorie levels of each restaurant.
#The getAvgFromColumn helps in getting the average sodium levels of each restaurant along with an index that states each restaurant name.
    barChartData = pd.Series([getAvgFromColumn(fastFoodFrame, 'Mcdonalds', ['calories']),
                              getAvgFromColumn(fastFoodFrame, 'Chick Fil-A', ['calories']),
                              getAvgFromColumn(fastFoodFrame, 'Sonic', ['calories']),
                              getAvgFromColumn(fastFoodFrame, 'Arbys', ['calories']),
                              getAvgFromColumn(fastFoodFrame, 'Burger King', ['calories']),
                              getAvgFromColumn(fastFoodFrame, 'Dairy Queen', ['calories'])],
                              index=['McDonald\'s', 'Chick Fil-A', 'Sonic', 'Arby\'s', 'Burger King', 'Dairy Queen']
                              )
#Creates and displays a bar chart from the series with a matching title and a table for data.
#The bar chart also include a Y-label that says "Amount" and a grid.
    barChart = barChartData.plot.bar(title='Average Calorie Levels of Fast Food Restaurants', ylabel='Amount', rot=0, fontsize=9.0, grid=True, table=True, figsize=(10, 7))
    plt.show()

#A possible save before the user can exit out of the program by pressing the enter button. 
    input()


