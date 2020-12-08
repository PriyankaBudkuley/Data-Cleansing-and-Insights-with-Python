#!/usr/bin/env python
# coding: utf-8

# # Assignment \#4 the Olympic dataset 1/2
# 
# #### Features description
# - *City*: City
# - *Edition*: Year
# - *Sport*: Sport
# - *Discipline*: Discipline
# - *Athlete*: Athlete's last name and first name (generally separated by a comma and a space)
# - *NOC*: Country, National Olympic Committee, ISO 3166-1 alpha-3
# - *Gender*: Men, Women
# - *Event*: Event
# - *Event_gender*: Event gender (F = Women, M = Men, X = NA)
# - *Medal*: Metal of medal (Bronze, Silver, Gold)

# In[1]:


# usual import and options
import pandas as pd
pd.set_option("display.max_rows", 16)


# ### Loading the dataset
# 
# **file**: `'Summer Olympic medallists 1896 to 2008 - ALL MEDALISTS.txt'`
# 
# **separator**: tab: `\t`

# In[2]:


# LOADING THE DATASET
# DO NOT CHANGE THIS CELL FOR GRADING
# THE DATASET SHOULD BE ALONG WITH THE NOTEBOOK AND THE PYTHON FILE

df = pd.read_csv('Summer Olympic medallists 1896 to 2008 - ALL MEDALISTS.txt', sep='\t')
df.head(10)


# #### Questions
# 
# 1) How many different cities have organized Olympic games?
# 
# 2) How many different editions of Olympic games are in the dataset?
# 
# 3) How many cities have organized more than one edition of Olympic games?
# 
# 4) Which sport distributed the most medals?
# 
# 5) Which discipline distributed the most medals?
# 
# 6) How many gold medals have been distributed?
# 
# 7) Which edition distributed the most silver medals?
# 
# 8) In how many different disciplines did men received medals (°)?
# 
# 9) In how many different disciplines did women received medals (°)?
# 
# 10) How many disciplines are dedicated to women (°)?
# 
# 11) How many countries have won a medal with an event gender equal to 'X'?
# 
# 12) How many countries have won a gold medal with an event gender equal to 'X'?
# 
# 13) How many different countries have an athlete whose surname is 'SCHMIDT' (+)?
# 
# 14) How many different sports have the word 'ball' in their name?
# 
# 15) How many Bronze or Silver medals have been won by any athlete whose surname is 'KIM' (+)?
# 
# (°) Use the 'Gender' column.
# 
# (+) Most of athlene's names are in the form: 'SURNAME, Firstname'

# In[3]:


# 1) How many different cities have organized Olympic games?
def exercise_01():
    result = df['City'].nunique()
    return result

# run and check
exercise_01()


# In[4]:


# 2) How many different editions of Olympic games are in the dataset?
def exercise_02():
    result = df['Edition'].nunique()
    return result

# run and check
exercise_02()


# In[5]:


# 3) How many cities have organized more than one edition of Olympic games?

def exercise_03():
    result = (df.groupby('City')['Edition'].nunique()>(1)).sum()
    return result

# run and check
exercise_03()


# In[6]:


# 4) Which sport distributed the most medals?

def exercise_04():
    result = (df.groupby('Sport')['Medal'].count()).idxmax()
    return result

# run and check
exercise_04()


# In[7]:


# 5) Which discipline distributed the most medals?

def exercise_05():
    result = (df.groupby('Discipline')['Medal'].count()).idxmax()
    return result

# run and check
exercise_05()


# In[8]:


# 6) How many gold medals have been distributed?

def exercise_06():
    result = (df['Medal']=="Gold").sum()
    return result

# run and check
exercise_06()


# In[9]:


# 7) Which edition distributed the most silver medals?

def exercise_07():
    result = (df.loc[df.Medal == "Silver"].groupby('Edition')['Medal'].count()).idxmax()
    return result

# run and check
exercise_07()


# In[10]:


# 8) In how many different disciplines did men received medals (°)?

def exercise_08():
    result = len(df.loc[df.Gender == "Men"].groupby('Discipline')['Medal'].count())
    return result

# run and check
exercise_08()


# In[11]:


# 9) In how many different disciplines did women received medals (°)?

def exercise_09():
    result = len(df.loc[df.Gender == "Women"].groupby('Discipline')['Medal'].count())
    return result

# run and check
exercise_09()


# In[12]:


# 10) How many disciplines are dedicated **only** to women (°)?

def exercise_10():
    Women = set(df.loc[df.Gender == "Women"]['Discipline'])
    Men = set(df.loc[df.Gender == "Men"]['Discipline'])
    result = Women-Men 
    return len(result)

# run and check
exercise_10()


# In[13]:


# 11) How many countries have won a medal with an event gender equal to 'X'?

def exercise_11():
    result = len(df.loc[df.Event_gender == "X"].groupby('NOC')['Event_gender'].value_counts())
    return result

# run and check
exercise_11()


# In[14]:


# 12) How many countries have won a gold medal with an event gender equal to 'X'?

def exercise_12():
    result = len(df.loc[df.Event_gender == "X"][df.Medal == "Gold"].groupby('NOC')['Medal'].count())
    return result

# run and check
exercise_12()


# In[15]:


# 13) How many different countries have an athlete whose surname is 'SCHMIDT'?

def exercise_13():
    result = len(df.loc[df['Athlete'].str.startswith('SCHMIDT')].groupby('NOC')['Athlete'].count())
    return result
    
# run and check
exercise_13()


# In[104]:


# 14) How many different sports have the word 'ball' in their name?

def exercise_14():
    result = (pd.Series(df['Sport'].unique())).str.contains('ball').sum()
    return result

# run and check
exercise_14()


# In[115]:


# 15) How many Bronze or Silver medals have been won by any athlete whose surname is 'KIM'?

def exercise_15():
    result = (pd.Series(df['Athlete'])).str.startswith('KIM,')[df.Medal != "Gold"].sum()
    return result

# run and check
exercise_15()

