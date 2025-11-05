import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('players.csv')
'''print(df.columns)
print(df.isnull().sum())
(df.fillna(0,inplace=True))
print(df.isnull().sum())
print(df.describe())'''
#player who r 35
'''print(df[df['Age']<=35].head(10))
#player with the highest salary
print(df[ ['Name','Wage']].max())'''
#player based on wage & skills
x=df['Wage'].head(10)
df['Skillset']=((0.3*df['Skill Moves'])+(0.2*df['Weak Foot'])+(0.1*df['Potential'])+(0.1*df['Finishing'])+(0.1*df['Strength'])+(0.1*df['Stamina'])+(0.1*df['Agility'])).head(10)
y=df['Skillset']
'''plt.xlabel('Wage')
plt.ylabel('Skills Set')
plt.bar(x,y,color='blue')
plt.show()'''
#top player based on skills
'''print("Top players based on Skillset")
Top_players=df.sort_values(by='Skillset',ascending=False)[['Name','Skillset']].head(10)
print(Top_players)
#skill comparision of top players
plt.bar(Top_players['Name'],Top_players['Skillset'],color='pink')
plt.show()'''
# 10 best forward players
'''df['forward']=((0.3*df['Finishing'])+(0.2*df['Dribbling'])+(0.1*df['BallControl'])+(0.2*df['Skill Moves'])+(0.1*df['SprintSpeed'])+(0.5*df['Acceleration'])+(0.5*df['Stamina']))
print(df.sort_values(by='forward',ascending=False)[['Name','forward']].head(10))
#10 best Mid-Fielders
df['Midfielders']=(0.15*df['ShortPassing'])+(0.15*df['LongPassing'])+(0.2*df['BallControl'])+(0.1*df['Dribbling'])+(0.1*df['Agility'])+(0.5*df['Balance'])+(0.1*df["Stamina"])+(0.15*df['Skill Moves'])
print(df.sort_values(by='Midfielders',ascending=False)[['Name','Midfielders']].head(10))
#10 best defender
df['Defender']=(0.3*df['HeadingAccuracy'])+(0.2*df['ShortPassing'])+(0.1*df['Agility'])+(0.1*df['Skill Moves'])+(0.5*df['Acceleration'])+(0.5*df['Jumping'])+(0.1*df['Reactions'])+(0.1*df['Strength'])
print(df.sort_values(by='Defender',ascending=False)[['Name','Defender']].head(10))'''
#correlation
#age vs skill analysis
x=df['Skillset']
y=df['Age']
plt.bar(x,y,color='yellow')
plt.xlabel('Skillset')
plt.ylabel('Age')
plt.show()
#pie chart of top 5 countries with most players
'''a=df['Nationality'].value_counts().head(5)
plt.pie(a.values,labels=a.index,autopct='%1.1f%%',colors=['green','yellow','blue','red','pink'])
plt.show()'''
#compare between rolando and messi