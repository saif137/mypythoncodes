import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Create a dataframe from the file data
df = pd.read_csv("universities_uk.txt", sep='\t', header=0);
#To print data on console
#print(df)
#To display descriptive statistics
#print(df.describe())
#To list the keys
#print(df.keys())
#Counting elements in each column
print("No of institution: "),
print(df['Institution '].nunique())
print(df['Institution '].value_counts(ascending=True))
print("No of Undergraduates: "),
print(df['Undergraduates '].sum())
# print("No of Postgraduates: "),
# print(df['Postgraduates '].sum())
# print("No of Total students: "),
# print(df['Total students'].sum())