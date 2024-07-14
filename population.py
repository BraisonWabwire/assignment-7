import pandas as pd

# Step 1: Read the population.csv file
file_path = 'C:/Users/braisonW/Desktop/G/assignment#7/population.csv'  # Update this to the correct path of the population.csv file
df = pd.read_csv(file_path, header=None, names=['State', 'County', 'Population'])

# Step 2: Calculate the average population of counties for each state
state_avg_population = df.groupby('State')['Population'].mean()

# Step 3: Sort the series by the average population in ascending order
sorted_state_avg_population = state_avg_population.sort_values()

# Step 4: Print the sorted series
print(sorted_state_avg_population)

