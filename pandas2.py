import pandas as pd
data = {
    'Name' : ['Anthony', 'Benedict', 'Colin', 'Daphne', 'Eloise'],
    'Age' : [31, 28, 26, 24, 20],
    'City' : ['London', "San Fransisco", "Madrid", "Copenhagen", "Rio de Janeiro"]
    }
df = pd.DataFrame(data)
print (df)
print (df ['Name'])
print (df[df['Age']>25])
print (df['Age'].describe())
df ['Gender']= ['Male', 'Male', 'Male', 'Female', 'Female']
print (df)
grouped_data = df.groupby ('Gender')['Age'].mean()
print (grouped_data)
df_sorted = df.sort_values(by='Age', ascending =False)
print (df_sorted)
df.to_csv('output.csv', index = False)