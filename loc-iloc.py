# import pandas
import pandas as pd

# List of Tuples
employees = [('Stuti', 28, 'Varanasi', 20000),
             ('Saumya', 32, 'Delhi', 25000),
             ('Aaditya', 25, 'Mumbai', 40000),
             ('Saumya', 32, 'Delhi', 35000),
             ('Saumya', 32, 'Delhi', 30000),
             ('Saumya', 32, 'Mumbai', 20000),
             ('Aaditya', 40, 'Dehradun', 24000),
             ('Seema', 32, 'Delhi', 70000)
             ]

# Create a DataFrame object from list
df = pd.DataFrame(employees,
                  columns=['Name', 'Age',
                           'City', 'Salary'])

# Set index on a Dataframe
df.set_index("Name",inplace=True)

# Using the operator .loc[]
# to select multiple rows
result = df.loc[["Stuti", "Saumya"],["City", "Salary"]]
result = df.iloc[0:2]
result = df.iloc[[2, 3, 5]]
result = df.iloc[[2, 3, 5],[0, 1]]
result = df.iloc[:, [0, 1]]
data = df
data.reset_index(inplace=True)

# Show the dataframe
print(result.shape[0])
print(result)
# selecting cars with brand 'Maruti' and Mileage > 25
print(df.loc[(df.City == 'Delhi') & (df.Age > 25)])
# print(data.loc[0:4])
data.loc[(data.City == 'Delhi'),['Age']] = 50
print('new','\n',data)
print(data.iloc[[0, 2, 4, 7]])
print(data.iloc[1: 5, 1: 3])

