import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/students.csv")

print("Student Data:")
print(df)

# Calculate average marks
print("\nAverage Marks:")
print(df.mean(numeric_only=True))

# Total and top student
df["Total"] = df["Math"] + df["Science"] + df["English"]
topper = df.loc[df["Total"].idxmax()]
print("\nTop Performer:")
print(topper)

# Visualization
df.plot(x="Name", y=["Math", "Science", "English"], kind="bar")
plt.title("Student Performance Analysis")
plt.show()
