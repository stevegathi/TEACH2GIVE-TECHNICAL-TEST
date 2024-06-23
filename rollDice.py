import random
import pandas as pd
import matplotlib.pyplot as plt

data = []

def rollDice():
	roll = random.randint(1,6)
	return roll

x = 0
while x < 24:
	result = rollDice()
	data.append(result)
	x += 1

# display the list
print("This is the content of the list")
for i in data:
	print(i)

# records available
print("The 4's in the data are: ", data.count(4))

# create a dataframe
df = pd.DataFrame(data, columns=['Rolls'])
print(df)

# Analysis
# Plot
# Counting
# Reporting

# Plotting
plt.figure(figsize=(8, 6))
plt.hist(df['Rolls'], bins=range(1, 8), align='left', edgecolor='black')
plt.title('Dice Rolls Distribution')
plt.xlabel('Dice Value')
plt.ylabel('Frequency')
plt.xticks(range(1, 7))
plt.grid(True)
# plt.show()

# Reporting
print("\nSummary Statistics:")
print(df.describe())