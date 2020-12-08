#!/usr/bin/env python
# coding: utf-8

# # Assignment \#5 the Olympic dataset 2/2
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
df.head()


# #### Questions
# 
# 1) How many different events are in the dataset?
# 
# 2) How many different events including numbers in their description are in the dataset?
# 
# 3) Which athlete has participated in the most editions?
# 
# 4) How many sports have the same number of Gold, Silver and Bronze medals?
# 
# 5) How many athletes have strictly more Gold medals than Silver and more Silver medals than Bronze?
# 
# 6) Which country has won at least one medal in each olympic edition?
# 
# 7) Add a column named 'Score' with 1 for Bronze, 2 for Silver and 3 for Gold medals. What is the total sum of scores?
# 
# 8) Which athlete has the largest sum of scores?
# 
# 9) Which woman athlete has the largest sum of scores?
# 
# 10) For how many countries the sum of men's scores is equal to the sum of women's scores?
# 
# 11) Add a column named 'Trial' with the concatenation of columns 'Discipline', 'Sport' and 'Event' separated by a space. How many different trials are in the dataset?
# 
# 12) Which edition has the largest number of different trials?
# 
# 13) Add a column 'First Name' with the first name of athletes. How many different first names are in the dataset (+)?
# 
# 14) Which athlete's first name has the largest sum of scores (+)?
# 
# 15) Which woman athlete's first name has the largest sum of scores (°) (+)?
# 
# (°) Use the 'Gender' column.
# (+) Most of athlene's names are in the form: 'SURNAME, Firstname'

# In[3]:


# 1) How many different events are in the dataset?

def exercise_01():
    result = len(df['Event'].drop_duplicates())
    return result


# run and check
exercise_01()


# In[46]:


# 2) How many different events including numbers in their description are in the dataset?

def exercise_02():
    result = pd.Series(df.iloc[:,7].unique()).str.contains("\d").sum()
    return result

# run and check
exercise_02()


# In[5]:


# 3) Which athlete has participated in the most editions?

def exercise_03():
    result = (df.groupby('Athlete')['Edition'].nunique()).idxmax()
    return result

# run and check
exercise_03()


# In[7]:


# 4) How many sports distributed exactly the same number of Gold, Silver and Bronze medals?

def exercise_04():
    Medalcount = pd.crosstab(df['Sport'], df['Medal'])
    result = len(Medalcount.loc[ (Medalcount['Gold']==Medalcount['Silver']) & (Medalcount['Silver']==Medalcount['Bronze'])])
    return result
    
# run and check
exercise_04()


# In[9]:


# 5) How many athletes received strictly more Gold medals than Silver and strictly more Silver medals than Bronze?

def exercise_05():
    Medalcount = pd.crosstab(df['Athlete'], df['Medal'])
    result = len(Medalcount.loc[ (Medalcount['Gold']>Medalcount['Silver']) & (Medalcount['Silver']>Medalcount['Bronze'])])
    return result

# run and check
exercise_05()


# In[51]:


# 6) Which country has won at least one medal in each olympic edition?

def exercise_06():
    result=(df.pivot_table(index ="Medal", columns ="NOC", values ="Edition", aggfunc ="nunique").sum().sort_values()).index[-1]
    return result

# run and check
exercise_06()


# In[52]:


# 7) What is the total sum of scores?

def exercise_07():
    df['score'] = (((df['Medal']=="Gold") * 3) + ((df['Medal']=="Silver") * 2) + ((df['Medal']=="Bronze") * 1))
    result = df['score'].sum()
    return result

# run and check
exercise_07()


# In[53]:


# 8) Which athlete has the largest sum of scores?

def exercise_08():
    result = df.groupby('Athlete')['score'].sum().idxmax()
    return result

# run and check
exercise_08()


# In[54]:


# 9) Which woman athlete has the largest sum of scores (°)?

def exercise_09():
    result = df.loc[df.Gender == "Women"].groupby('Athlete')['score'].sum().idxmax()
    return result

# run and check
exercise_09()


# In[55]:


# 10) For how many countries the sum of men' scores is equal to the sum of women' scores?

def exercise_10():
    men_score = df[df['Gender']=='Men'].groupby ('NOC' )['score'].sum().reset_index()
    women_score = df[df['Gender']=='Women'].groupby ('NOC' )['score'].sum().reset_index()
    df_result = men_score.merge(women_score, on="NOC")
    df_result['diff'] = df_result['score_x'] - df_result['score_y']
    result = len(df_result[df_result['diff']==0])
    return result

# run and check
exercise_10()


# In[56]:


# 11) How many different trials are in the dataset?

def exercise_11():
    df['trial'] = df['Discipline'].astype(str)+' '+df['Sport']+' '+df['Event']
    result = (df['trial']).nunique()
    return result

# run and check
exercise_11()


# In[57]:


# 12) Which edition has the most different trials?

def exercise_12():
    result = df.groupby('Edition')['trial'].nunique().idxmax()
    return result

# run and check
exercise_12()


# In[58]:


# 13) How many different first names are in the dataset?

def exercise_13():
    df_new = df.Athlete.str.split(",", n=1, expand=True)
    df['Firstname'] = df_new[1]
    df['Firstname'] =df['Firstname'].str.strip('.,')
    result=len(df['Firstname'].value_counts())
    
    return result

# run and check
exercise_13()


# In[59]:


# 14) Which athlete's first name has the largest sum of scores?

def exercise_14():
    result = df.groupby('Firstname')['score'].sum().idxmax()
    return result

# run and check
exercise_14()


# In[60]:


# 15) Which woman athlete's first name has the largest sum of scores (°)?

def exercise_15():
    result = df.loc[df.Gender == "Women"].groupby('Firstname')['score'].sum().idxmax()
    return result

# run and check
exercise_15()

