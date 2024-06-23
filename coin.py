import random
import pandas as pd
import matplotlib.pyplot as plt

# Function to simulate a coin toss
def tossCoin():
    # 1 is heads, 2 is tails
    return random.randint(1, 2)

# Simulating 1000 coin tosses
data = [tossCoin() for _ in range(1000)]

# Displaying the content of the list
print("This is the content of the list:")
for i in data:
    print(i)

# Counting the occurrence of heads (1's)
print("The number of heads (1's) in the list:", data.count(1))

# Creating a DataFrame
df = pd.DataFrame(data, columns=['Toss'])

# Plotting the distribution of coin tosses
plt.figure(figsize=(8, 6))
plt.hist(df['Toss'], bins=range(1, 4), align='left', edgecolor='black', rwidth=0.5)
plt.title("Coin Toss Distribution")
plt.xlabel("Coin Value (1=Heads, 2=Tails)")
plt.ylabel("Frequency")
plt.xticks([1, 2])
plt.grid(True)
plt.show()

# Reporting summary statistics
print("\nSummary Statistics:")
print(df.describe())
