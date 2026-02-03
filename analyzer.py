import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
data = pd.read_csv("data.csv")

print("Dataset:\n")
print(data)

# Basic analysis
print("\nBasic Statistics:")
print(data.describe())

# Highest and lowest marks
highest = data["Marks"].max()
lowest = data["Marks"].min()

print("\nHighest Marks:", highest)
print("Lowest Marks:", lowest)

# Plot graph
plt.plot(data["Name"], data["Marks"])
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks Analysis")
plt.show()
