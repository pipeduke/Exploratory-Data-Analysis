#import
import pandas as pd
import numpy as np
import missingno as msno
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, date
import os

if not os.path.exists("Graphics"):
    os.mkdir("Graphics")
if not os.path.exists("FilesCsv"):
    os.mkdir("FilesCsv")

# Read csv files and save to dataframe
df_users_csv = pd.read_csv('users.csv')
df_users_raw_csv = pd.read_csv('users_raw.csv')

# Visually identify where null values are found
msno.matrix(df_users_csv)
msno.matrix(df_users_raw_csv)
msno.bar(df_users_csv)
msno.bar(df_users_raw_csv)

# null values control
df_users_null = df_users_csv.fillna(0)
df_users_raw_null = df_users_raw_csv.fillna(0)
df_users = df_users_null.replace(['[]','[None]','[None, None, None]','[[None, None, None]]'],0)
df_users_raw = df_users_raw_null.replace(['[]','[None]','[None, None, None]','[[None, None, None]]'],0)

# non-null check
msno.matrix(df_users)
msno.matrix(df_users_raw)

# Final dataframe
df_final = df_users.merge(df_users_raw, left_on= 'user_id', right_on='id')

#Export to csv
df_final.to_csv("FilesCsv/df_final.csv", index=False)

#Query1
query1 = df_final[['last_role', 'gender','average_feedback']].sort_values(['average_feedback'],ascending=False).head(5)
query1.to_csv("FilesCsv/query1.csv", index=False)

#Query2
query2 = df_final[df_final.connections_sent>10][['dreamt_companies','desired_state','level_last_study']].sort_values(['desired_state'],ascending=False).head(5)
query2.to_csv("FilesCsv/query2.csv", index=False)

#Query3
query3 = df_final[(df_final.profile_completed==100) & (df_final.gender.isin(['F','M']))].groupby(['gender']).agg({'gender':'count'})
query3.to_csv("FilesCsv/query3.csv", index=False)

#Graphic1
# Create dataframe
df_age_avg = df_final[['birthdate','average_feedback']]
# Format string to date
df_age_avg['birthdate'] = pd.to_datetime(df_age_avg['birthdate'], format='mixed')
pd.options.mode.chained_assignment = None
# Add column age 
df_age_avg.insert(2, 'age', round((pd.Timestamp.today() - df_age_avg["birthdate"]).dt.days / 365.25), allow_duplicates=False)
# Eliminate wrong ages, under 16 and over 100 years
df_graphic1 = df_age_avg[(df_age_avg.age>16) & (df_age_avg.age<100)]
# Data
y = np.array(df_graphic1['age'])
x = np.array(df_graphic1['average_feedback'])
# Graphic
fig, ax = plt.subplots()
ax.scatter(x = x, y = y)
plt.savefig("Graphics/Graphic1.png")
plt.clf()

#Graphic2
# Create dataframe
df_graphic2 = df_final[['views_to_resume_received','reactions_received','profile_completed']]
# data
x = np.array(df_graphic2['views_to_resume_received'])
y = np.array(df_graphic2['reactions_received'])
group = np.array(df_graphic2['profile_completed'])
df_data_graphic2 = {'x': x, 'y': y, 'group': group}
# Graphic
sns.scatterplot(x = 'x', y = 'y', hue = 'group', data = df_data_graphic2)
plt.savefig("Graphics/Graphic2.png")
plt.clf()
