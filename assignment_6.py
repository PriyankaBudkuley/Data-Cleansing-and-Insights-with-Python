#!/usr/bin/env python
# coding: utf-8

# # Assignment \#7 French names
# 
# Download page: https://www.insee.fr/fr/statistiques/2540004/
# 
# Section: `Fichiers France hors Mayotte`
# 
# File format: `csv`
# 
# File size: `2 Mo`
# 
# Zip name: `nat2019_csv.zip`
# 
# Semi-colon delimited CSV file name: `nat2019.csv`

# #### Objective
# 
# The objective of this assignment is to download the dataset, and to load and transform the `DataFrame` so that **it has exactly the same characteristics** than the full US `DataFrame` that we have studied in the Python coding bootcamp.
# 
# To read properly the file, you should use the pandas `read_csv()` function with the appropriate arguments, please refer to the pandas documentation.
# 
# Requirements (in any order):
# 
# - The `DataFrame` has the appropriate shape: N rows x 4 columns
# 
# - The column names are properly set
# 
# - Columns are properly ordered: `year`, `name`, `gender` and `births`
# 
# - The data type, or `dtype`, of each column is properly set
# 
# - The values of the `gender` column are properly set: `'F'` for female and `'M'` for male
# 
# - Names with a single character are discarded
# 
# - The case of all names is properly modified: all initials are upper case and other letters lower case
# 
# - Rows with unusable values are discarded
# 
# - Data are properly sorted: `year`, `gender`, `births` (descending) and `name`
# 
# - The index of the `DataFrame` is properly set: 0 to N-1. For this last requirement you should use the `reset_index()` method of `DataFrame`  with the appropriate arguments, please refer to the pandas documentation.
# 
# You should program the manipulations in a single Python function which should return the transformed `DataFrame`. The aim of the assignment is to get a `DataFrame` that exactly conforms to the US one.
# 
# *Nota bene*: The French dataset discarded names with fewer than 3 occurrences instead of 5 for the US one. We let the limit of 3 since the French dataset is smaller than the US one. Therefore, there is no requirements for this point.
# 
# There are 10 requirements. In fact, the grading system will check 13 control points bringing each 2.3 points, since 3 requirements have been split in 2 tests, so as partial resolutions of these requirements will be taken into consideration.
# 
# Floating point grades will be rounded up to the next integer according to the number of control points that are passed.
# 
# Number of control points | Grade
# - | -
# 0 | 0
# 1 | 3
# 2 | 5
# 3 | 7
# 4 | 10
# 5 | 12
# 6 | 14
# 7 | 17
# 8 | 19
# 9 | 21
# 10 | 23
# 11 | 26
# 12 | 28
# 13 | 30

# In[1]:


import pandas as pd


# In[16]:


# YOU SHOULD IMPLEMENT A SINGLE FUNCTION
# DO NOT CHANGE ITS NAME
# IT SHOULD READ THE DATASET FROM THE FILE ALONG WITH THE NOTEBOOK
# IT SHOULD PERFORM THE APPROPRIATE TRANSFORMATIONS TO THE DATAFRAME
# IT SHOULD RETURN THE TRANSFORMED DATAFRAME

def exercise_01():
    df = pd.read_csv('nat2019.csv', sep=';')
    df = df.rename(columns={'sexe': 'Gender','preusuel': 'Name','annais': 'Year','nombre': 'Births'})
    df = df.reindex(['Year','Name','Gender','Births'],axis=1)
    df['Gender'] = df['Gender'].replace([1,2],["M","F"])
    df = df[df['Name'].apply(lambda x: len(str(x))>1)]
    df['Name']= ((df['Name']).str.title().replace(["!","‰","_","œ","~","`"],"")).replace(["_Prenoms_Rares"],"None")
    df['Year']= df['Year'].replace("XXXX","None")
    df1 = df.dropna()
    df2 = df1.mask(df1.eq('None')).dropna()
    result = df2.sort_values(by=['Year','Gender','Births'], ascending=False).reset_index(drop=True)
    return result

exercise_01()


# **Homework, out of the scope of the assignment**
# 
# After that you may use this dataset within the notebook 4 in order to perform with the French names the same analysis than we did perform with the US one.
# 
# For instance,
# - Exercise 3: Graph of diversity of names which end by a given letter, for the 7 letters which have the most diversity in 2018. What are the top 7 letters for the French names? Compare with the US ones.
# - Exercises 4 & 5: Study of names switching gender. You may try with the following names: Camille, Dominique, Alix, Yaël.
