#This program is made by Bryan Liem. This program creates a Panda Series from a dictionary and alters and displays certain information in the Panda Series.
#Imports the necessary module pandas as pd.
import pandas as pd

#Creates a new Panda Series called Vowels with the following information and prints it.
#Every dictionary value is set to 0.
Vowels = pd.Series({'a':0, 'e':0, 'i':0, 'o':0, 'u':0})
print(Vowels)

#Sets all dictionary values in the Panda Series to 10 by selecting every label value and prints it.
Vowels[:] = 10
print(Vowels)

#Dividdes all dictionary values in the Panda Series by 2 by selecting every label value and prints it.
Vowels[:] /= 2
print(Vowels)

#Creates a new Panda Series called Vowels1 with the following information.
Vowels1 = pd.Series({'a':2, 'e':5, 'i':6, 'o':3, 'u':8})

#Creates a new Panda Series called Vowels3 by merging Vowels with Vowels1 and prints it.
Vowels3 = Vowels + Vowels1
print(Vowels3)

#Subtracts all values of Vowels from Vowels1 based on matching labels and prints it.
Vowels1 -= Vowels
print(Vowels1)

#Changes the labels of Vowels1 into their capital form and prints it.
Vowels1.index = ['A', 'E', 'I', 'O', 'U']
print(Vowels1)

